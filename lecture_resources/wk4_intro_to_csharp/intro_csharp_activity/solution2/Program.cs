// ------------------------------------------------------------
// To create this project from scratch using the .NET CLI:
// ------------------------------------------------------------
// 1. Open a terminal or command prompt
// 2. Run the following command to create a new console app:
//      dotnet new console -n CircleAreaCalculator
//
// 3. Navigate to the new project folder:
//      cd CircleAreaCalculator
//
// 4. Replace the contents of Program.cs with this file.
//
// 5. To build the project:
//      dotnet build
//
// 6. To run the project:
//      dotnet run
//
// ------------------------------------------------------------

using System;


/** CHALLENGE: Try writing your own calcCircleArea function above
 the Main function (inside the braces of the Program class).

--------------------------------------------------------------- 
The template to write a function is like this:

static [return_type] FunctionName([parameters])
{
    // Function logic here
    return value; // if return_type is not void
}

Notice that the return type is required. In Python, you didn't do
this. But in C#, if you return a decimal (like the calculation of
the overall score), you have to write your function signature like:

static double nameOfTheFunction(param1, param2, ... etc.) { ...

"double" means "this function will return a double"!

---------------------------------------------------------------
Example Square function (notice we say static *int* because we
return an int):

static int Square(int number)
{
    return number * number;
}

Example usage:

int result = Square(5); // result is 25
---------------------------------------------------------------

Square function example implemented inside Program class:

class Program 
{
    static int Square(int number)
    {
        return number * number;
    }

    static void Main(string[] args) // Starting point (run automatically)
    {
        int result = Square(5); // result is 25

        Console.WriteLine($"5^2 is: {result}");

        // Python equivalent of the following line is print(f"Type of result: {type(result)}")
        Console.WriteLine($"Type of result: {result.GetType()}");
    }
}

*/

namespace CircleAreaCalculator
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter radius: ");
            double radius = double.Parse(Console.ReadLine());

            const double pi = 3.14159;
            double area = pi * radius * radius;

            Console.WriteLine($"Area is: {area}");

            // Try Console.WriteLine($"Area is: {area:F3}");
            // Would work just like Python's: print(f"Area is: {area:.3f}")
        }
    }
}
