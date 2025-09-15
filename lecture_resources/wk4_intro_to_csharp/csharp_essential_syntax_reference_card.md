```cs
// Basic program structure
using System;

public class Program 
{
    public static void Main(string[] args)
    {
        // Variable declaration
        int age = 25;
        string name = "Alice";
        double gpa = 3.75;
        
        // Input/Output
        Console.Write("Enter name: ");
        string input = Console.ReadLine();
        Console.WriteLine("Hello " + input);
        
        // Type conversion
        int number = int.Parse(input);
        
        // Math operations
        int sum = 10 + 5;
        int remainder = 17 % 3;
    }
}
```