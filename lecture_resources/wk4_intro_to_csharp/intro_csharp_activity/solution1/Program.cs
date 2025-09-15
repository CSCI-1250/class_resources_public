// ------------------------------------------------------------
// To create this project from scratch using the .NET CLI:
// ------------------------------------------------------------
// 1. Open a terminal or command prompt
// 2. Run the following command to create a new console app:
//      dotnet new console -n GradeCalculatorApp
//
// 3. Navigate to the new project folder:
//      cd GradeCalculatorApp
//
// 4. Replace the contents of Program.cs with this file (copy/paste)
//
// 5. To build the project:
//      dotnet build
//
// 6. To run the project:
//      dotnet run
//
// Notice we see the same warnings from class... These are WARNINGS, not errors
// There's a way we can make this code safer, but this is a good equivalent
// translation of what the Python code said.
// ------------------------------------------------------------

using System;

namespace GradeCalculatorApp // This is our surrounding folder
{
    // This class handles input and calculation logic
    class GradeCalculator
    {

        // In Python, we called the main function, i.e. main()
        // In C# the Main function as defined below is getting
        // called by default. Just imagine an imaginary call at
        // the bottom that says:
        //
        // Main(...);
        static void Main(string[] args)
        {
            Console.Write("Enter student name: ");
            string studentName = Console.ReadLine();

            Console.Write("Midterm score: ");
            
            // Can do this as two separate lines
            string midtermString = Console.ReadLine();
            int midterm = int.Parse(midtermString);

            Console.Write("Final score: ");
            
            // Can also do it all in one line
            // Python equivalent final = int(input())
            int final = int.Parse(Console.ReadLine());

            double average = (midterm + final) / 2.0;

            // Good old-fashioned string concatenation (but no converting the numbers to strings! C# does that for you)
            //Console.WriteLine("Student " + studentName + " has average: " + average);
            // F-string equivalent (called string interpolation)
            Console.WriteLine($"Student {studentName} has average: {average}");
        }
    }
}
