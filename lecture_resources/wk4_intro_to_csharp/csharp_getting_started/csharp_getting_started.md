# C# Getting Started Guide - From Python to C#
## CSCI 1250 - Transitioning from Python to C#

## Learning Objectives
By the end of this guide, you will be able to:
- **Set up** a C# development environment using .NET CLI and VS Code
- **Create and run** C# console applications
- **Understand** key differences between Python and C# syntax
- **Use** C# loops (for, while, foreach, do-while) effectively
- **Apply** computational thinking concepts in C# programs
- **Translate** Python algorithms to C# implementations

---

## Part 1: Environment Setup (15 minutes)

### Prerequisites Check
Make sure you have these installed on your system:

1. **Visual Studio Code** - You should already have this
2. **.NET SDK** - We'll install this now
3. **C# Extension for VS Code** - We'll add this

### Installing .NET SDK

#### Windows / MacOS:
1. Go to https://dotnet.microsoft.com/download
2. Download the latest .NET SDK (v9 at time of writing)
3. Run the installer and follow prompts
4. Restart VS Code

#### Linux (Ubuntu/Debian):
```bash
# Add Microsoft package repository
wget https://packages.microsoft.com/config/debian/$(lsb_release -rs)/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
rm packages-microsoft-prod.deb

# Install .NET SDK
sudo apt update
sudo apt install -y dotnet-sdk-9.0 # Or the desired version, e.g., dotnet-sdk-8.0
```

### Verify Installation
Open a terminal/command prompt and run:
```bash
dotnet --version
```
You should see something like `9.0.xxx`

### VS Code Extensions
1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Install: **C# Dev Kit** (this includes the C# extension)
4. Restart VS Code

---

## Part 2: Your First C# Program (20 minutes)

### Video reference

If you're having trouble following along with the written steps below, [check out this video](https://youtu.be/HFLALzkcjLM?si=z15HqizfXV4CG9oq&t=12).
At 0:45 the speaker is using PowerShell inside Windows Terminal. You can follow along in Termainal on Mac or which ever terminal you use on Linux as well. Note that when he types a command like `cd helloworld`, when he presses the tab key, the backslashes
are automatically added.

**Video command-line differences:**
- Linux and Mac terminals will not use backslashes (the basic commands are the same; just type `cd hel` and then hit the tab key to autocomplete!).
- Use `ls` instead of `dir` (platform agnostic way to print what's in the current directory)
- `dotnet` commands are the same

### Creating a New Project

Open terminal in VS Code and run:
```bash
# Create a new directory for your C# work
mkdir CSharPractice
cd CSharpPractice

# Create your first console application
dotnet new console -n HelloWorld
cd HelloWorld

# Open in VS Code
code .
```

### Understanding the Project Structure

Your project will have:
```
HelloWorld/
├── HelloWorld.csproj    # Project configuration (like package.json)
├── Program.cs           # Your main code file
└── obj/                 # Build artifacts (like __pycache__)
```

### Your First Program

Open `Program.cs` - you'll see:
```csharp
// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
```

**Compare to Python:**
```python
# Python
print("Hello, World!")
```

```csharp
// C#
Console.WriteLine("Hello, World!");
```

### Running Your Program

In the terminal:
```bash
dotnet run
```

You should see: `Hello, World!`

### Key Differences from Python

| Concept | Python | C# |
|---------|---------|-----|
| **Print** | `print("text")` | `Console.WriteLine("text");` |
| **Comments** | `# comment` | `// comment` |
| **Semicolons** | Not required | **Required** after statements |
| **Braces** | Indentation | `{ }` for code blocks |
| **Case Sensitivity** | snake_case | PascalCase for methods |


### "Variable Type Detective" Class Activity

Ready to see the full C# translations of our Python examples and run them?
Apply the same process as above to set up, build, and run these examples:

[Solution 1: Grade Calculator](https://github.com/CSCI-1250/class_resources_public/blob/main/lecture_resources/wk4_intro_to_csharp/intro_csharp_activity/solution1/Program.cs)


[Solution 2: Circle Area Calculator](https://github.com/CSCI-1250/class_resources_public/blob/main/lecture_resources/wk4_intro_to_csharp/intro_csharp_activity/solution2/Program.cs)

---

## Part 3: C# Syntax Essentials (25 minutes)

### Variables and Data Types

**Python vs C# Variables:**

```python
# Python - Dynamic typing
name = "Ryan"
age = 35
gpa = 3.8
is_professor = True
```

```csharp
// C# - Static typing (declare types)
string name = "Ryan";
int age = 35;
double gpa = 3.8;
bool isProfessor = true;
```

### Input and Output

**Python:**
```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

**C#:**
```csharp
Console.Write("Enter your name: ");
string name = Console.ReadLine();
Console.WriteLine($"Hello, {name}!");

// For numbers, you need to convert:
Console.Write("Enter your age: ");
string ageInput = Console.ReadLine();
int age = int.Parse(ageInput);

// Safer conversion:
int age = Convert.ToInt32(Console.ReadLine());
```

### String Interpolation

**Python:**
```python
name = "Alice"
score = 95
print(f"{name} scored {score}%")
```

**C#:**
```csharp
string name = "Alice";
int score = 95;
Console.WriteLine($"{name} scored {score}%");
```

### Practice Exercise 3A: Grade Calculator Conversion

Create a new file called `GradeCalculator.cs` and convert this Python code:

```python
# Python version
print("=== Grade Calculator ===")
name = input("Enter student name: ")
exam = float(input("Enter exam score: "))
homework = float(input("Enter homework average: "))
participation = float(input("Enter participation score: "))

# Calculate weighted grade
final_grade = (exam * 0.6) + (homework * 0.3) + (participation * 0.1)

print(f"{name}'s final grade: {final_grade:.2f}%")

if final_grade >= 90:
    letter = "A"
elif final_grade >= 80:
    letter = "B"
elif final_grade >= 70:
    letter = "C"
elif final_grade >= 60:
    letter = "D"
else:
    letter = "F"

print(f"Letter grade: {letter}")
```

**Your Task:** Convert this to C# in `GradeCalculator.cs`

<details>
<summary>Click to see the C# solution</summary>

```csharp
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("=== Grade Calculator ===");
        
        Console.Write("Enter student name: ");
        string name = Console.ReadLine();
        
        Console.Write("Enter exam score: ");
        double exam = Convert.ToDouble(Console.ReadLine());
        
        Console.Write("Enter homework average: ");
        double homework = Convert.ToDouble(Console.ReadLine());
        
        Console.Write("Enter participation score: ");
        double participation = Convert.ToDouble(Console.ReadLine());
        
        // Calculate weighted grade
        double finalGrade = (exam * 0.6) + (homework * 0.3) + (participation * 0.1);
        
        Console.WriteLine($"{name}'s final grade: {finalGrade:F2}%");
        
        string letter;
        if (finalGrade >= 90)
        {
            letter = "A";
        }
        else if (finalGrade >= 80)
        {
            letter = "B";
        }
        else if (finalGrade >= 70)
        {
            letter = "C";
        }
        else if (finalGrade >= 60)
        {
            letter = "D";
        }
        else
        {
            letter = "F";
        }
        
        Console.WriteLine($"Letter grade: {letter}");
    }
}
```
</details>

---

## Part 4: C# Loops - The Complete Guide (40 minutes)

Loops in C# are more explicit than Python but offer more control. Let's explore all the loop types.

### 4.1 For Loops

**Python:**
```python
# Basic for loop with range
for i in range(5):
    print(f"Count: {i}")

# For loop with list
courses = ["CS1250", "CS1100", "CS2400"]
for course in courses:
    print(course)
```

**C# - For Loop:**
```csharp
// Basic for loop
for (int i = 0; i < 5; i++)
{
    Console.WriteLine($"Count: {i}");
}

// For loop anatomy:
// for (initialization; condition; increment/decrement)
// {
//     // code to repeat
// }
```

### 4.2 While Loops

**Python:**
```python
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
```

**C#:**
```csharp
int count = 0;
while (count < 5)
{
    Console.WriteLine($"Count: {count}");
    count++;  // Note: ++ is increment operator
}
```

### 4.3 Do-While Loops (New in C#!)

C# has a loop that Python doesn't - the do-while loop. It **always runs at least once**.

```csharp
int number;
do
{
    Console.Write("Enter a number between 1-10: ");
    number = Convert.ToInt32(Console.ReadLine());
    
    if (number < 1 || number > 10)
    {
        Console.WriteLine("Invalid! Try again.");
    }
} 
while (number < 1 || number > 10);

Console.WriteLine($"Thank you! You entered: {number}");
```

**Use do-while when:** You need to run the loop body at least once (like input validation).

### 4.4 Foreach Loops

**Python:**
```python
courses = ["CS1250", "CS1100", "CS2400"]
for course in courses:
    print(course)
```

**C#:**
```csharp
string[] courses = {"CS1250", "CS1100", "CS2400"};
foreach (string course in courses)
{
    Console.WriteLine(course);
}

// Can also use var
foreach (var course in courses)
{
    Console.WriteLine(course);
}
```

### 4.5 Loop Control Statements

| Python | C# | Purpose |
|--------|-----|---------|
| `break` | `break;` | Exit loop completely |
| `continue` | `continue;` | Skip to next iteration |


## Summary: Key C# Loop Concepts

You've now learned all four main loop types in C#:

### Loop Type Quick Reference

| Loop Type | When to Use | Example |
|-----------|-------------|---------|
| **for** | Known number of iterations | `for (int i = 0; i < 10; i++)` |
| **while** | Unknown iterations, check condition first | `while (grade < 0)` |
| **do-while** | At least one iteration needed | `do { ... } while (choice != "Q");` |
| **foreach** | Iterate through collections | `foreach (string item in list)` |

### Key Differences from Python

1. **Explicit types**: `int i = 0` instead of `i = 0`
2. **Semicolons required**: Every statement ends with `;`
3. **Braces for blocks**: Use `{ }` instead of indentation
4. **Increment operator**: `i++` is common for `i += 1`
5. **String comparison**: Use `.Equals()` or `==` for strings
6. **Case sensitivity**: C# is case-sensitive (`Console` not `console`)

### Next Steps

Now that you understand C# loops and basic syntax, you're ready to:
- Learn about methods/functions in C# (see the "CHALLENGE" comment in [Solution 2](https://github.com/CSCI-1250/class_resources_public/blob/main/lecture_resources/wk4_intro_to_csharp/intro_csharp_activity/solution2/Program.cs))
- start building larger programs that chain functions together.
- The `dotnet` channel on YouTube has a fantastic [C# for Beginners playlist](https://youtu.be/HFLALzkcjLM?si=CeVqQ74-qlBUNrfz) to serve as a crash course to C#. Videos 2-11 cover much of what we've already learned in Python.

The computational thinking skills you learned in Python transfer directly to C# - you're just using a different syntax to express the same logical concepts!
            
