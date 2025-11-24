
"""
Student Submission File Organizer
Processes student submission files and organizes them by student.
"""

import os
import re
import shutil
from datetime import datetime
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class Submission:
    """Represents a single submission file"""
    student_id: str
    student_name: str
    timestamp: datetime
    original_filename: str
    file_path: Path
    assignment_file: str
    
    def __str__(self):
        return f"{self.student_name} ({self.student_id}) - {self.assignment_file}"

class SubmissionOrganizer:
    """Organizes student submission files"""
    
    def __init__(self, source_directory: str = "."):
        self.source_directory = Path(source_directory)
        self.submissions: List[Submission] = []
        self.students: Dict[str, List[Submission]] = defaultdict(list)
        
        # Regex pattern to parse filenames
        # Pattern: student_id-course_id - Student Name- timestamp - filename
        self.filename_pattern = re.compile(
            r'^(\d+)-(\d+)\s*-\s*([^-]+?)-\s*([^-]+?)\s*-\s*(.+)$'
        )
    
    def parse_filename(self, filename: str) -> Optional[Submission]:
        """Parse a submission filename and extract components"""
        match = self.filename_pattern.match(filename)
        if not match:
            print(f"Warning: Could not parse filename: {filename}")
            return None
        
        student_id, course_id, student_name, timestamp_str, assignment_file = match.groups()
        
        # Clean up student name
        student_name = student_name.strip()
        
        # Parse timestamp (format appears to be: Sep 3, 2025 302 PM)
        try:
            # Handle various timestamp formats
            timestamp_str = timestamp_str.strip()
            # Convert format like "Sep 3, 2025 302 PM" to "Sep 3, 2025 3:02 PM"
            if re.match(r'.+ \d{3,4} [AP]M$', timestamp_str):
                # Extract time part and format it properly
                parts = timestamp_str.split()
                time_part = parts[-2]  # e.g., "302"
                ampm = parts[-1]       # e.g., "PM"
                
                # Format time properly
                if len(time_part) == 3:
                    formatted_time = f"{time_part[0]}:{time_part[1:]} {ampm}"
                elif len(time_part) == 4:
                    formatted_time = f"{time_part[:2]}:{time_part[2:]} {ampm}"
                else:
                    formatted_time = f"{time_part} {ampm}"
                
                # Reconstruct timestamp
                date_part = " ".join(parts[:-2])
                timestamp_str = f"{date_part} {formatted_time}"
            
            timestamp = datetime.strptime(timestamp_str, "%b %d, %Y %I:%M %p")
        except ValueError as e:
            print(f"Warning: Could not parse timestamp '{timestamp_str}': {e}")
            timestamp = datetime.now()
        
        return Submission(
            student_id=student_id,
            student_name=student_name,
            timestamp=timestamp,
            original_filename=filename,
            file_path=self.source_directory / filename,
            assignment_file=assignment_file.strip()
        )
    
    def scan_directory(self) -> None:
        """Scan directory for submission files"""
        print(f"Scanning directory: {self.source_directory}")
        
        files = [f for f in os.listdir(self.source_directory) 
                if os.path.isfile(os.path.join(self.source_directory, f))]
        
        print(f"Found {len(files)} files")
        
        for filename in files:
            submission = self.parse_filename(filename)
            if submission:
                self.submissions.append(submission)
                self.students[submission.student_id].append(submission)
        
        print(f"Successfully parsed {len(self.submissions)} submissions from {len(self.students)} students")
    
    def organize_by_student(self, output_directory: str = "organized_submissions") -> None:
        """Organize files into student directories"""
        output_path = Path(output_directory)
        output_path.mkdir(exist_ok=True)
        
        for student_id, submissions in self.students.items():
            if not submissions:
                continue
            
            # Use first submission for student name
            student_name = submissions[0].student_name
            # Clean student name for directory
            clean_name = re.sub(r'[^\w\s-]', '', student_name).strip()
            clean_name = re.sub(r'\s+', '_', clean_name)
            
            student_dir = output_path / f"{clean_name}_E00{student_id}"
            student_dir.mkdir(exist_ok=True)
            
            print(f"\nOrganizing files for {student_name} ({student_id}):")
            
            # Sort submissions by timestamp
            submissions.sort(key=lambda x: x.timestamp)
            
            for i, submission in enumerate(submissions, 1):
                # Create new filename with sequence number
                file_extension = Path(submission.assignment_file).suffix
                new_filename = f"{i:02d}_{submission.assignment_file}"
                
                source_path = submission.file_path
                dest_path = student_dir / new_filename
                
                try:
                    if source_path.exists():
                        shutil.copy2(source_path, dest_path)
                        print(f"  {submission.assignment_file} -> {new_filename}")
                    else:
                        print(f"  Warning: Source file not found: {source_path}")
                except Exception as e:
                    print(f"  Error copying {submission.assignment_file}: {e}")
    
    def generate_report(self) -> str:
        """Generate a summary report"""
        report = []
        report.append("STUDENT SUBMISSION REPORT")
        report.append("=" * 50)
        report.append(f"Total submissions: {len(self.submissions)}")
        report.append(f"Total students: {len(self.students)}")
        report.append("")
        
        # Sort students by name
        sorted_students = sorted(self.students.items(), 
                               key=lambda x: x[1][0].student_name if x[1] else "")
        
        for student_id, submissions in sorted_students:
            if not submissions:
                continue
                
            student_name = submissions[0].student_name
            report.append(f"{student_name} (ID: {student_id})")
            report.append(f"  Files submitted: {len(submissions)}")
            
            # Sort by timestamp
            submissions.sort(key=lambda x: x.timestamp)
            
            for submission in submissions:
                timestamp_str = submission.timestamp.strftime("%Y-%m-%d %H:%M")
                report.append(f"    {timestamp_str} - {submission.assignment_file}")
            
            report.append("")
        
        return "\n".join(report)
    
    def find_missing_submissions(self, expected_files: List[str]) -> Dict[str, List[str]]:
        """Find students missing expected submission files"""
        missing = {}
        
        for student_id, submissions in self.students.items():
            student_name = submissions[0].student_name if submissions else "Unknown"
            submitted_files = [s.assignment_file.lower() for s in submissions]
            
            missing_files = []
            for expected in expected_files:
                # Check if any submitted file contains the expected filename
                if not any(expected.lower() in submitted for submitted in submitted_files):
                    missing_files.append(expected)
            
            if missing_files:
                missing[f"{student_name} ({student_id})"] = missing_files
        
        return missing

def main():
    """Main execution function"""
    organizer = SubmissionOrganizer(".")
    
    # Scan for submissions
    organizer.scan_directory()
    
    # Generate and display report
    print("\n" + organizer.generate_report())
    
    # Check for missing submissions (customize expected files as needed)
    expected_files = ["grade_calculator1.py", "grade_calculator2.py", "grade_calculator3.py"]
    missing = organizer.find_missing_submissions(expected_files)
    
    if missing:
        print("\nMISSING SUBMISSIONS:")
        print("=" * 30)
        for student, missing_files in missing.items():
            print(f"{student}: {', '.join(missing_files)}")
    
    # Organize files by student
    print(f"\nOrganizing files...")
    organizer.organize_by_student()
    print(f"\nFiles organized in 'organized_submissions' directory")

if __name__ == "__main__":
    main()
