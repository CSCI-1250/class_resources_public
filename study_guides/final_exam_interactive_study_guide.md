# CSCI 1250 C# Interactive Study Guide
## Test Your Knowledge with Hands-On Activities! 🎯

---

## 🔢 **Activity 1: Operator Detective**
Fill in the blanks with the correct operator symbols:

1. To check if two values are equal: `5 ___ 5` → `true`
2. To check if a number is NOT equal to zero: `x ___ 0`
3. Logical AND operator: `true ___ false` → `false`
4. Increment operator: `count___` (equivalent to `count = count + 1`)
5. Modulo operator: `10 ___ 3` → `1`

**Challenge**: What's the result of this expression?
```
!true && (false || true) && 5 >= 3
```
Step through it: `________________`

---

## 🎲 **Activity 2: Data Type Matching Game**
Match each scenario with the BEST data type:

**Scenarios:**
- A. Student's age
- B. Product price with tax calculations
- C. User's full name
- D. Whether a user is logged in
- E. A single grade letter
- F. Temperature reading

**Data Types:**
1. `bool`
2. `char` 
3. `decimal`
4. `double`
5. `int`
6. `string`

**Your Answers:**
A: ___ | B: ___ | C: ___ | D: ___ | E: ___ | F: ___

---

## 🧩 **Activity 3: Division Mystery Puzzle**
Solve this step-by-step! What will each expression evaluate to?

```csharp
int a = 15;
int b = 4;
double c = 15.0;
double d = 4.0;
```

1. `a / b` = ___
2. `c / b` = ___
3. `a / d` = ___
4. `(double)a / b` = ___
5. `c / d` = ___

**Bonus Puzzle**: Fix this code to get the correct average:
```csharp
// BROKEN: This gives wrong result!
double average = (85 + 90 + 78) / 3;
// Your fix: ________________________________
```

---

## 📝 **Activity 4: Variable Declaration Practice**
Complete these variable declarations using best practices:

1. Declare and initialize a variable to store a student's GPA:
   ```csharp
   _______ _______ = _______;
   ```

2. Declare a variable for counting items (start at 0):
   ```csharp
   _______ _______ = _______;
   ```

3. Declare a variable to store whether homework is submitted:
   ```csharp
   _______ _______ = _______;
   ```

---

## 🔤 **Activity 5: String Challenge**
Given: `string course = "  CSCI-1250  ";`

Fill in the code to achieve each result:

1. Get the length: `course.______` → Result: ___
2. Remove spaces: `course.______()` → Result: ___
3. Make lowercase: `course.______.______()` → Result: ___
4. Get characters 2-5: `course.______.______(2, 4)` → Result: ___
5. Check if contains "1250": `course.______(______)` → Result: ___

**String Indexing Puzzle**: If `word = "CODING"`, what character is at:
- `word[0]`: ___
- `word[word.Length - 1]`: ___
- `word[2]`: ___

---

## 🔄 **Activity 6: Loop Logic Puzzles**

### Puzzle A: Count the Output
How many times will "Hello" be printed?
```csharp
for (int i = 5; i < 15; i += 2)
{
    Console.WriteLine("Hello");
}
```
**Answer**: ___ times

### Puzzle B: While vs Do-While
What's the output difference?

**Code A:**
```csharp
int x = 10;
while (x < 5)
{
    Console.WriteLine(x);
    x++;
}
```
Output: _______________

**Code B:**
```csharp
int x = 10;
do
{
    Console.WriteLine(x);
    x++;
} while (x < 5);
```
Output: _______________

### Puzzle C: Control Variable Tracking
Trace through this loop and list all values of `i` that get printed:
```csharp
for (int i = 10; i >= 2; i -= 3)
{
    Console.WriteLine(i);
}
```
Values printed: _______________

---

## ✅ **Activity 7: Boolean Logic Brain Teaser**
Evaluate these step-by-step (show your work!):

**Problem 1:**
```csharp
int age = 17;
bool hasPermission = true;
bool isWeekend = false;

// Can access if: age >= 18 OR (has permission AND it's weekend)
bool canAccess = age >= 18 || (hasPermission && isWeekend);
```

Step 1: `age >= 18` = ___
Step 2: `hasPermission && isWeekend` = ___
Step 3: Final result = ___

**Problem 2:**
```csharp
!(true || false) && (false && true) || true
```

Step 1: `(true || false)` = ___
Step 2: `!(true || false)` = ___
Step 3: `(false && true)` = ___
Step 4: `___ && ___` = ___
Step 5: `___ || true` = ___

[Boolean truth table diagram](./assets/boolean_truth_table.svg)

---

## 🔧 **Activity 8: Modulo Applications**

### Fill in the Blanks:
```csharp
// Check if number is even
if (number ___ 2 ___ 0)
{
    Console.WriteLine("Even");
}

// Check if divisible by 5
if (number ___ ___ == ___)
{
    Console.WriteLine("Divisible by 5");
}

// Get last digit
int lastDigit = number ___ ___;
```

### Practical Problem:
You're creating a seating system where every 4th person gets a special meal. Write the condition:
```csharp
if (personNumber ___ ___ == ___)
{
    Console.WriteLine("Special meal!");
}
```

---

## ⚙️ **Activity 9: Method Mastery**

### Complete the Method:
```csharp
// Calculate letter grade from percentage
public static _____ GetLetterGrade(_____ percentage)
{
    if (percentage >= 90) return _____;
    else if (percentage >= 80) return _____;
    else if (percentage >= 70) return _____;
    else if (percentage >= 60) return _____;
    else return _____;
}
```

### Method Call Challenge:
Given this method:
```csharp
public static double CalculateTip(double billAmount, double tipPercent)
{
    return billAmount * (tipPercent / 100);
}
```

How would you call it to calculate a 15% tip on a $50 bill?
```csharp
double tip = _________________________;
```

### Void vs Return Puzzle:
Which of these methods should return a value vs use `void`?
- A. `PrintStudentInfo()` → ________
- B. `CalculateGPA()` → ________
- C. `DisplayMenu()` → ________
- D. `GetUserAge()` → ________

---

## 🏗 **Activity 10: Class Construction Challenge**

### Complete the Student Class:
```csharp
public class Student
{
    // Private fields
    private string _______;
    private int _______;
    private _______ gpa;
    
    // Default constructor
    public _______()
    {
        name = _______;
        studentId = _______;
        gpa = _______;
    }
    
    // Parameterized constructor
    public Student(_______ n, _______ id, _______ g)
    {
        _______ = n;
        _______ = id;
        _______ = g;
    }
    
    // Properties
    public string Name 
    { 
        _______ { return _______; } 
        _______ { _______ = _______; } 
    }
    
    // Override ToString
    public override _______ _______()
    {
        return $"_______________________";
    }
}
```

### Object Creation Practice:
Create two Student objects using the class above:
```csharp
// Using default constructor
Student student1 = _________________________;

// Using parameterized constructor
Student student2 = _________________________;
```

---

## 🔐 **Activity 11: Access Modifier Quiz**

Mark each as **Public**, **Private**, **Protected**, or **Internal**:

1. A method that calculates grades internally: _______
2. A property that other classes need to access: _______
3. A field storing sensitive account balance: _______
4. A class used only within this project: _______
5. A method that validates input before processing: _______

**Scenario**: In a BankAccount class, categorize these members:
```csharp
_____ class BankAccount
{
    _____ double balance;           // Should this be accessible?
    _____ string accountNumber;     // Should this be accessible?
    _____ void Deposit(double amt); // Should this be accessible?
    _____ bool ValidateAmount(double amt); // Should this be accessible?
}
```

[Access modifiers diagram](./assets/access_modifiers_diagram.svg)

---

## 💾 **Activity 12: Memory Detective**

### Stack or Heap?

Mark each as **Stack** or **Heap**:
```csharp
int count = 5;                    // _______
string name = "Alice";            // _______  (the string data)
Student s = new Student();        // _______  (the object)
bool isActive = true;             // _______
int[] scores = new int[10];       // _______  (the array data)
```

[Stack/heap memory diagram](./assets/stack_heap_diagram.svg)

### Reference Type Puzzle:
Predict the output:
```csharp
Student alice = new Student("Alice", 101, 3.5);
Student backup = alice;
backup.Name = "Alicia";
Console.WriteLine(alice.Name);
```
Output: _______

Why? _______________________________

---

## 📂 **Activity 13: File I/O Challenge**

### Complete the Code:
```csharp
// Read all student names from a file
string[] names = File._______(________);

// Process and create output
List<string> output = new List<string>();
foreach (string name in names)
{
    output._____($$"Student: {_____}");
}

// Write results to new file
File._______(_______, _______);
```

### File Processing Puzzle:
You have a file with test scores (one per line). Complete the code to:
1. Read all scores
2. Calculate average  
3. Save results

```csharp
string[] scoreLines = _________________________;
double total = 0;
foreach (string line in scoreLines)
{
    int score = _________________________;
    total += score;
}
double average = _________________________;

string[] results = {$"Total scores: {scoreLines._______}",
                   $"Average: {average:F2}"};
File._______________________;
```

---

## 📚 **Activity 14: Arrays vs Lists Showdown**

### Fill in the Correct Property/Method:
```csharp
// Arrays
int[] scores = new int[5];
Console.WriteLine(scores._______);  // Get size

// Lists  
List<int> grades = new List<int>();
Console.WriteLine(grades._______);  // Get size
grades._______(95);                 // Add element
grades._______(0);                  // Remove at index
bool hasA = grades._______(95);     // Check if contains
```

### Conversion Challenge:
Convert this array code to use a List instead:
```csharp
// Original Array Code:
string[] names = new string[3] {"Alice", "Bob", "Charlie"};
for (int i = 0; i < names.Length; i++)
{
    Console.WriteLine(names[i]);
}

// Your List Version:
List<string> names = _________________________;
foreach (_______ name in _______)
{
    Console.WriteLine(_______);
}
```

---

## 🎯 **Activity 15: Final Boss Challenge**

### The Great Integration Puzzle!
You're building a grade book system. Use everything you've learned to fill in this comprehensive example:

```csharp
public class GradeBook
{
    // Private field for storing grades
    _______ List<_______> grades;
    
    // Constructor
    public _______()
    {
        grades = _________________________;
    }
    
    // Method to add grade with validation
    public _______ AddGrade(_______ grade)
    {
        if (grade >= 0 _______ grade <= 100)
        {
            grades._______(grade);
            Console.WriteLine("Grade added successfully!");
        }
        else
        {
            Console.WriteLine("Invalid grade!");
        }
    }
    
    // Method to calculate average
    public _______ CalculateAverage()
    {
        if (grades._______ == 0) return 0;
        
        _______ total = 0;
        foreach (_______ grade in grades)
        {
            total _______ grade;
        }
        return _______ total / grades._______;
    }
    
    // Method to get letter grade
    public _______ GetLetterGrade()
    {
        double avg = _______();
        if (avg >= 90) return _______;
        // Complete the rest...
        else return _______;
    }
    
    // Override ToString for display
    public override _______ _______()
    {
        return $"Grades: {_______}, Average: {_______:F2}, Letter: {_______}";
    }
}

// Usage:
GradeBook book = _________________________;
book._______(95);
book._______(87);
book._______(92);
Console.WriteLine(_______);
```

---

## 🎉 **Answer Key & Self-Check**

Once you complete all activities, use this section to check your answers and identify areas that need more review!

### Quick Reference Reminders:
- **Division**: `int/int = int`, but `double/int = double`
- **String**: `.Length` (property, no parentheses)
- **Arrays**: `.Length` property  
- **Lists**: `.Count` property, `.Add()`, `.Remove()` methods
- **Boolean Order**: `()` → `!` → `&&` → `||`
- **Modulo**: `%` gives remainder (useful for even/odd, cycling)
- **Access**: `public` = accessible everywhere, `private` = only in same class
- **Memory**: Value types → Stack, Reference types → Heap
- **Constructors**: Special methods for object initialization

---

### 🏆 Study Strategy Tips:
1. **Code Tracing**: Work through each line with specific values
2. **Memory Diagrams**: Draw boxes for stack vs heap allocation  
3. **Boolean Tables**: Create truth tables for complex conditions
4. **Method Practice**: Write small methods for common tasks
5. **Object Modeling**: Design classes for real-world scenarios

### 📋 Pre-Exam Checklist:
- [ ] Can evaluate complex boolean expressions
- [ ] Know difference between `=` and `==`  
- [ ] Understand when division gives int vs double
- [ ] Remember `.Length` vs `.Count`
- [ ] Can write basic constructors and properties
- [ ] Understand public vs private access
- [ ] Know when to use different loop types
- [ ] Can trace through method calls with parameters
- [ ] Understand stack vs heap memory concepts
- [ ] Can write file I/O operations

**You've got this! 🎓 Good luck on your final exam!**