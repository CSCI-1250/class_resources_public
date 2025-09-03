# CSCI 1250 Lab 2: Computational Thinking & Problem Solving

## Learning Objectives
By the end of this lab, you will be able to:
- **Apply** the four pillars of computational thinking to real-world problems
- **Design** algorithms using pseudocode before implementing in Python
- **Create** simple models that represent real-world entities
- **Implement** decision-making structures in Python programs
- **Decompose** complex problems into manageable sub-problems
- **Recognize patterns** in programming solutions

---

## Setup and Review (15 minutes)

### Quick Review: Last Week's Grade Calculator
Let's connect last week's work to today's computational thinking concepts:

1. **Decomposition**: We broke the grade calculation into parts (get inputs, calculate weights, display result)
2. **Pattern Recognition**: Each input followed the same pattern (prompt → input → convert)  
3. **Abstraction**: We focused only on grades, not student names or course details
4. **Algorithm Design**: We created step-by-step instructions that became our code

### Today's Focus
We'll practice these skills with new problems and learn two additional concepts:
- **Pseudocode**: Planning our programs in plain English
- **Decision Making**: Having our programs make choices based on conditions

---

# Activity 1: Decomposition & Modeling (25 minutes)

## Scenario: ETSU Campus Navigation System
You're designing a mobile app to help new students navigate campus. The app should help students find buildings, calculate walking times, and provide helpful information.

### Part A: Decomposition (10 minutes)
Working in groups of 3-4, break down this complex problem into smaller sub-problems.

**Your Task**: List at least 8 smaller problems that need to be solved to create this navigation system.

Example sub-problems:
- Store building locations
- Calculate distances between buildings
- [Continue the list...]

### Part B: Modeling (15 minutes)
Create a new file named `models.txt` to create simple models for the entities in your navigation system.

**Your Task**: Design models (data representations) for:

1. **Building Model** - What information do you need about each building?
2. **Student Model** - What do you need to know about the user?
3. **Route Model** - How do you represent a path between buildings?

**Template**:
```
Building Model:
- Name: (e.g., "Brinkley Center")
- Location: (e.g., coordinates or address)
- Building Code: (e.g., "BRIN")
- [Add 3-4 more attributes]

Student Model:
- [List 4-5 important attributes]

Route Model:
- [List 3-4 important attributes]
```

**Discussion Questions**:
- What information did you choose to leave out? Why?
- How is this an example of abstraction?

---

# Activity 2: Pattern Recognition & Data Processing (30 minutes)

## Scenario: Student Records Management
You work in the registrar's office and need to process student enrollment data. Let's identify patterns in how we handle similar data and create reusable solutions.

### Part A: Recognizing Data Patterns (10 minutes)
Look at these three different data processing tasks:

**Task 1: Calculate class size**
```python
cs1250_enrolled = 23
cs1100_enrolled = 31  
cs2400_enrolled = 18
total_students = cs1250_enrolled + cs1100_enrolled + cs2400_enrolled
```

**Task 2: Calculate average temperature**
```python
monday_temp = 68
tuesday_temp = 72
wednesday_temp = 70
average_temp = (monday_temp + tuesday_temp + wednesday_temp) / 3
```

**Task 3: Calculate total study hours**
```python
math_hours = 4
science_hours = 6
english_hours = 3
total_hours = math_hours + science_hours + english_hours
```

**Discussion Questions** (with your group):
1. What pattern do you see across all three tasks?
2. What's similar about the operations being performed?
3. How could we create a reusable solution?

### Part B: Creating Pattern Solutions (20 minutes)

**Your Task**: Create `data_processor.py` and implement the following functions. Focus on completing the calculation functions first, then use the provided helper functions.

**Functions for You to Complete**:

```python
def calculate_total(value1, value2, value3, data_type="items"):
    """Calculate total of three values with descriptive output"""
    # TODO: Calculate the total of the three values
    total = 0  # Replace this line with your calculation
    
    # This print statement is provided for you
    print(f"Total {data_type}: {total}")
    return total

def calculate_average(value1, value2, value3, data_type="items"):
    """Calculate average of three values with descriptive output"""
    # TODO: Calculate the total first (hint: you can call calculate_total!)
    # TODO: Then calculate the average (total divided by 3)
    average = 0  # Replace this line with your calculation
    
    # This print statement is provided for you
    print(f"Average {data_type}: {average:.1f}")
    return average
```

**Complete Functions Provided for You**:

```python
def process_course_data():
    """Process enrollment data for three courses"""
    print("=== Course Enrollment Processor ===")
    
    # Get course enrollment numbers
    course1 = int(input("Enter CSCI 1250 enrollment: "))
    course2 = int(input("Enter CSCI 1100 enrollment: "))
    course3 = int(input("Enter CSCI 2400 enrollment: "))
    
    # Use your pattern functions
    total_enrolled = calculate_total(course1, course2, course3, "students enrolled")
    avg_class_size = calculate_average(course1, course2, course3, "class size")
    
    return total_enrolled, avg_class_size

def process_temperature_data():
    """Process daily temperature readings"""
    print("\n=== Temperature Data Processor ===")
    
    # Get temperature data
    day1_temp = float(input("Enter Monday temperature: "))
    day2_temp = float(input("Enter Tuesday temperature: "))
    day3_temp = float(input("Enter Wednesday temperature: "))
    
    # Use your pattern functions
    total_temp = calculate_total(day1_temp, day2_temp, day3_temp, "degrees")
    avg_temp = calculate_average(day1_temp, day2_temp, day3_temp, "temperature")
    
    return avg_temp

def main():
    """Main program demonstrating pattern reuse"""
    # TODO: Call process_course_data() and store the returned values
    # course_total, course_avg = process_course_data()
    
    # TODO: Call process_temperature_data() and store the returned value  
    # temp_avg = process_temperature_data()
    
    print("\n=== Summary Report ===")
    # TODO: Print summary information using the values you stored above
    # print(f"Total students across all courses: {course_total}")
    # print(f"Average class size: {course_avg:.1f}")
    # print(f"Average temperature: {temp_avg:.1f}°F")

if __name__ == "__main__":
    main()
```

**Your Tasks**:
1. **Complete `calculate_total()`**: Add the three values together
2. **Complete `calculate_average()`**: Calculate total, then divide by 3
3. **Complete `main()`**: Uncomment and complete the TODO sections

**Hints**:
- For `calculate_average()`, you can reuse your `calculate_total()` function
- The print statements and return statements are already provided
- Focus on the mathematical operations: addition and division

**Test Your Program**: 
Try these inputs to verify your functions work:
- Course enrollments: 23, 31, 18 (should total 72, average 24.0)
- Temperatures: 68.5, 72.0, 70.5 (should average 70.3)

---

# Activity 3: Algorithm Design with Pseudocode (35 minutes)

## Scenario: Academic Advisor Program
Design a program that acts like an academic advisor, helping students understand their grade status and what they need to improve.

### Part A: Understanding the Problem (10 minutes)
Your advisor program should:
1. Calculate a student's current grade
2. Tell them what letter grade they have
3. If they're failing, suggest which assignments to focus on
4. Calculate what they need on the final project to reach their desired grade

### Part B: Algorithm Design in Pseudocode (15 minutes)

Create a new file named `pseudocode.txt`. Write pseudocode for the academic advisor. Use these pseudocode conventions:

```
BEGIN ProgramName
    DISPLAY "message"
    READ variable
    SET variable = calculation
    IF condition THEN
        action
    ELSE
        different action
    END IF
END ProgramName
```

**Your Task**: Write complete pseudocode for the academic advisor program.

**Starter Template**:
```
BEGIN Academic_Advisor
    DISPLAY "=== Academic Advisor ==="
    
    // Get current grades
    DISPLAY "Enter your exit tickets average: "
    READ exit_tickets
    // Add more inputs...
    
    // Calculate current grade
    SET current_grade = ...
    
    // Determine letter grade
    IF current_grade >= 90 THEN
        SET letter_grade = "A"
    ELSE IF ...
        // Complete this logic
    END IF
    
    // Display current status
    DISPLAY "Your current grade is: " + current_grade + "% (" + letter_grade + ")"
    
    // Add advisor suggestions...
    
END Academic_Advisor
```

### Part C: Review and Refine (10 minutes)
Trade pseudocode with another group. Can you understand their algorithm? Suggest improvements and get feedback on yours.

---

# Activity 4: Implementation with Decision Making (40 minutes)
*Create a new file: `academic_advisor.py`*

## Convert Your Pseudocode to Python
Now implement your academic advisor as a Python program.

### Part A: Basic Implementation (20 minutes)
Create `academic_advisor.py` and translate your pseudocode to Python:

```python
def get_letter_grade(percentage):
    """Convert percentage to letter grade"""
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

def calculate_current_grade(exit_tickets, quizzes, labs, final_project):
    """Calculate weighted average - reuse from the grade calculator lab"""
    # Your implementation here
    pass

def main():
    print("=== Academic Advisor ===")
    
    # Get current grades
    # Your code here
    
    # Calculate current grade
    current_grade = calculate_current_grade(exit_tickets, quizzes, labs, final_project)
    letter_grade = get_letter_grade(current_grade)
    
    # Display current status
    print(f"Your current grade is: {current_grade:.2f}% ({letter_grade})")
    
    # Provide advice based on grade
    if letter_grade == "F":
        print("⚠️ You are currently failing. Consider:")
        print("- Meeting with your professor during office hours")
        print("- Focusing extra effort on upcoming assignments")
        print("- Forming a study group with classmates")
    elif letter_grade == "D":
        print("⚠️ You're passing but at risk. Consider:")
        print("- Reviewing areas where you lost points")
        print("- Asking for help on challenging topics")
    elif letter_grade == "C":
        print("✓ You're passing! To improve:")
        print("- Review quiz mistakes for patterns")
        print("- Start assignments earlier")
    elif letter_grade == "B":
        print("✓ Good work! You're doing well.")
        print("- Keep up the consistent effort!")
    else:  # A grade
        print("🎉 Excellent work! Keep it up!")

if __name__ == "__main__":
    main()
```

---

# Activity 5: Testing and Reflection (15 minutes)

### Part A: Test Your Programs (10 minutes)
Test your academic advisor with these scenarios:

**Test Case 1**: Struggling Student
- Exit Tickets: 65, Quizzes: 70, Labs: 68, Final Project: 72
- Expected: Overall ≈ 69.5% (D), should suggest improvements

**Test Case 2**: Good Student  
- Exit Tickets: 85, Quizzes: 88, Labs: 92, Final Project: 90
- Expected: Overall ≈ 89.2% (B), positive feedback

**Test Case 3**: Excellent Student
- Exit Tickets: 95, Quizzes: 94, Labs: 96, Final Project: 98  
- Expected: Overall ≈ 96.5% (A), congratulations

### Part B: Reflection (5 minutes)
Answer these questions with your group:

1. **Decomposition**: How did breaking down the advisor problem into smaller parts help?

2. **Pattern Recognition**: What patterns did you notice between the grade calculator and the advisor program?

3. **Abstraction**: What real-world details did you choose to ignore in your student model?

4. **Algorithm Design**: How did writing pseudocode first help with your Python implementation?

5. **Decision Making**: Give an example of a decision your program makes and why it's useful.

---

# Submission Requirements

Submit all your Python files with proper documentation:


- [ ] `academic_advisor.py` - Your complete academic advisor program  
- [ ] `pseudocode.txt` - Your pseudocode for the advisor program
- [ ] `models.txt` - Your building, student, and route models from Activity 1

**Code Requirements**:
- [ ] All functions have docstrings explaining their purpose
- [ ] Code uses meaningful variable names
- [ ] Programs handle invalid input gracefully
- [ ] Programs produce correct output for test cases
- [ ] Code is properly indented and readable

**Documentation Requirements**:
- [ ] Include your name and group members at the top of each file
- [ ] Comment complex calculations and logic
- [ ] Explain your abstraction choices in the models file

---

# More Extension Challenges (Optional)

If you finish early, try these advanced challenges:

### Challenge 1: Multiple Students
Modify your advisor to handle multiple students in sequence using a while loop.

### Challenge 2: Grade History  
Track how grades change over time by storing previous calculations.

### Challenge 3: Course Comparison
Compare a student's performance across multiple courses.

### Challenge 4: Predictive Modeling
Create a simple prediction of final grade based on early assignment patterns.

---

# Key Takeaways

Today you practiced computational thinking by:

- **Breaking down complex problems** (campus navigation, academic advising) into manageable pieces
- **Recognizing patterns** in code structure and reusing solutions through functions  
- **Creating abstractions** by focusing only on essential information in your models
- **Designing step-by-step algorithms** using pseudocode before coding
- **Making programs intelligent** through decision-making structures

These skills are fundamental to programming and problem-solving in computer science. Every complex system starts with these basic thinking patterns!

**Remember**: Professional programmers spend more time thinking about problems than typing code. The thinking skills you practiced today are what separate good programmers from great ones.

**Next Week**: We'll explore loops and iteration - how to make programs repeat actions efficiently.
