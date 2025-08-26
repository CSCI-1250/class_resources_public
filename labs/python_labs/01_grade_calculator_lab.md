# CSCI 1250 Lab 1: Grade Calculator (Complete Version)

## Learning Objectives
By the end of this lab, you will be able to:
- **Declare** and **initialize** variables with meaningful names
- Use the `input()` function to gather user data
- **Parse** string input into appropriate numeric data types
- Apply mathematical operators to perform calculations
- Use f-strings to format and display results
- Apply proper Python syntax conventions
- **Define** and **call** functions with parameters and return values
- Implement control flow using while loops

---

# Phase 1: Basic Grade Calculator

## Learning Objectives
By the end of this phase, you will be able to:
- **Declare** and **initialize** variables with meaningful names
- Use the `input()` function to gather user data
- **Parse** string input into appropriate numeric data types
- Apply mathematical operators to perform calculations
- Use f-strings to format and display results
- Apply proper Python syntax conventions

## Scenario
You're a student in CSCI 1100, and you want to calculate your current grade in the class. Your final grade is calculated using the following weights:
- Exit Tickets Average: 1/6 (≈16.67%)
- Quiz Average: 1/6 (≈16.67%)
- Lab Average: 1/6 (≈16.67%)
- Final Project: 3/6 (50%)

Your task is to create a Python program that asks for your scores in each category and calculates your overall class grade.

## Part 1: Variable Declaration and Getting User Input

### Understanding Variables
Before we start coding, let's understand what we're doing when we work with variables:

- **Variable Declaration**: This is when we create a new variable name in our program
- **Variable Initialization**: This is when we assign a value to that variable for the first time

In Python, declaration and initialization happen together. When we write:
```python
name = "Alice"
```
We are both **declaring** a variable called `name` AND **initializing** it with the value `"Alice"`.

### Your Task: Gather Input and Store in Variables

Create a new Python file called `grade_calculator.py` and follow these steps:

1. **Declare and initialize** a variable to store the exit tickets average:
   ```python
   exit_tickets = input("Enter your exit tickets average: ")
   ```

2. **Declare and initialize** variables for the other grade components using meaningful variable names:
   - Quiz average
   - Lab average  
   - Final project score

**Syntax Reminder**: 
- Variable names should be descriptive (`quiz_average` not `q`)
- Use lowercase letters and underscores for multi-word variables (`final_project` not `finalProject`)
- No spaces in variable names (`exit tickets` ❌, `exit_tickets` ✅)

## Part 2: Parsing Data Types

### Understanding Data Types and Parsing
Right now, all your variables contain **strings** (text), but we need **numbers** to do math! 

- **Parsing**: Converting data from one type to another (in this case, string to float)
- The `input()` function **always** returns a string, even if the user types numbers
- We must **parse** these strings into floats before we can perform mathematical operations

### Your Task: Parse Strings to Floats

Convert each string input to a float by **reassigning** the variable. You can do this in two ways:

**Method 1: Reassign the same variable**
```python
exit_tickets = float(exit_tickets)
```

**Method 2: Declare new variables**
```python
exit_tickets_float = float(exit_tickets)
```

Choose Method 1 for this lab. Parse all four grade components from strings to floats.

**Syntax Reminders**:
- Parentheses are required: `float(variable_name)`
- Don't forget the assignment operator `=`
- Variable names are case-sensitive (`Exit_Tickets` ≠ `exit_tickets`)

## Part 3: Mathematical Operations and Variable Assignment

### Understanding the Calculation
Now we'll perform the weighted average calculation. Remember, each component has a different weight:
- Exit Tickets: 1/6 of total grade
- Quizzes: 1/6 of total grade  
- Labs: 1/6 of total grade
- Final Project: 3/6 of total grade (half the grade!)

### Your Task: Calculate and Store the Result

Here's an example of how to calculate the weighted value for one component:

```python
exit_ticket_grade = exit_tickets * (1/6)
```

Now you need to:
1. Calculate the weighted value for each of the other three components (quizzes, labs, final project)
2. **Declare and initialize** a variable called `overall_grade` that adds all four weighted components together

**Syntax Reminders**:
- Use parentheses to control order of operations
- Multiplication operator is `*` 
- Addition operator is `+`
- Division operator is `/`
- Python follows standard mathematical order of operations (PEMDAS)

## Part 4: Output Formatting with F-Strings

### Understanding F-String Formatting
An **f-string** (formatted string literal) allows us to embed variables directly inside strings for clean output.

### Your Task: Display the Results

Use an f-string to display the final grade. The syntax is:
```python
print(f"Your overall grade in CSCI 1100 is: {overall_grade:.2f}%")
```

**F-String Syntax Breakdown**:
- `f"..."` - The `f` before the quotes makes it a formatted string
- `{variable_name}` - Curly braces contain the variable to display  
- `{variable_name:.2f}` - The `:.2f` formats the number to 2 decimal places
- Everything else prints exactly as written

**Important Syntax Notes**:
- Don't forget the `f` before the opening quote!
- Curly braces `{}` are required around variable names
- The print statement needs parentheses: `print(...)`

## Sample Run

Here's what your program should look like when it runs:

```
Enter your exit tickets average: 85.0
Enter your quiz average: 92.0
Enter your lab average: 88.0
Enter your final project score: 90.0
Your overall grade in CSCI 1100 is: 89.17%
```

## Key Programming Terminology Review

As you work through this lab, you're applying these important concepts:

- **Variable Declaration**: Creating new variable names in your program
- **Variable Initialization**: Assigning values to variables for the first time  
- **Parsing**: Converting data from one type (string) to another (float)
- **Assignment Operator**: The `=` symbol that stores values in variables
- **F-String**: A formatted string that embeds variables using `f"..."` syntax

**Common Syntax Errors to Avoid**:
- Forgetting parentheses in function calls: `float exit_tickets` ❌ vs `float(exit_tickets)` ✅
- Missing the `f` in f-strings: `"Grade: {grade}"` ❌ vs `f"Grade: {grade}"` ✅  
- Using spaces in variable names: `exit tickets` ❌ vs `exit_tickets` ✅
- Wrong quotation marks: `"Hello'` ❌ vs `"Hello"` ✅

## Submission Requirements

Submit your completed `grade_calculator.py` file. Make sure your code:
- [ ] Uses `input()` to gather all four grade components
- [ ] Converts all inputs to floats
- [ ] Stores values in appropriately named variables
- [ ] Correctly applies the weighting scheme (1/6, 1/6, 1/6, 3/6)
- [ ] Uses an f-string to display the final result
- [ ] Includes appropriate prompts so the user knows what to enter

## Testing Your Code

Test your program with these sample inputs to verify it's working correctly:

**Test Case 1:**
- Exit Tickets: 80, Quizzes: 85, Labs: 90, Final Project: 95
- Expected Result: 90.0%

**Test Case 2:**
- Exit Tickets: 100, Quizzes: 100, Labs: 100, Final Project: 100
- Expected Result: 100.0%

**Test Case 3:**
- Exit Tickets: 70, Quizzes: 75, Labs: 80, Final Project: 85
- Expected Result: 80.0%

Good luck, and remember: this is your first step into the world of programming!

---

# Phase 2: Introducing Functions

## Learning Objectives
By the end of this phase, you will be able to:
- Understand what functions are and why they're useful
- **Define** functions with proper syntax
- Understand **method signatures**, **parameters**, and **arguments**
- Use **return statements** to send values back from functions
- **Call** functions and use their returned values

## Understanding Functions

### What is a Function?
A **function** is a reusable block of code that performs a specific task. Functions help us:
- **Avoid repetition**: Write code once, use it many times
- **Organize code**: Break complex problems into smaller, manageable pieces
- **Make code readable**: Give meaningful names to chunks of logic
- **Enable testing**: Test individual pieces of functionality

### Function Anatomy
Every function has several parts:

```python
def function_name(parameter1, parameter2):  # ← Method Signature
    # Function body (the code that runs)
    result = parameter1 + parameter2
    return result  # ← Return Statement
```

**Key Vocabulary**:
- **Method Signature**: The first line that defines the function name and its parameters
- **Parameter**: A variable name in the function definition that will receive a value
- **Argument**: The actual value you pass to the function when you call it
- **Return Statement**: Sends a value back to whoever called the function

### Example: Parameters vs Arguments
```python
def greet(name):        # 'name' is a PARAMETER
    return f"Hello, {name}!"

message = greet("Alice")  # "Alice" is an ARGUMENT
print(message)  # Output: Hello, Alice!
```

## Your Task: Refactor Using Functions

Now let's take your working Phase 1 code and improve it using functions.

### Function 1: input_float()

Create a function that handles the repetitive task of getting input and parsing it to float:

```python
def input_float(prompt):
    # Your code here: 
    # 1. Get user input using the prompt parameter
    # 2. Parse the input to float
    # 3. Return the float value
```

**Method Signature Breakdown**:
- `def` - keyword that starts a function definition
- `input_float` - the function name (descriptive!)
- `(prompt)` - parameter list (this function takes one parameter)
- `:` - colon ends the method signature

### Function 2: calculate_overall_grade()

Create a function that performs the grade calculation:

```python
def calculate_overall_grade(exit_tickets, quiz_avg, lab_avg, final_project):
    # Your code here:
    # 1. Calculate weighted values for each component
    # 2. Add them together
    # 3. Return the overall grade
```

### Using Your Functions

Once you've defined both functions, rewrite your main program to use them:

```python
# Get all the grades using your input_float function
exit_tickets = input_float("Enter your exit tickets average: ")
# ... get the other three grades

# Calculate the overall grade using your calculation function
overall_grade = calculate_overall_grade(exit_tickets, quiz_avg, lab_avg, final_project)

# Display the result
print(f"Your overall grade in CSCI 1100 is: {overall_grade:.2f}%")
```

**Key Points**:
- When you **call** `input_float("Enter...")`, the string `"Enter..."` becomes the **argument**
- Inside the function, this argument is received as the **parameter** called `prompt`
- The **return statement** sends the parsed float back to your main program

## Testing Phase 2

Test your refactored code with the same test cases from Phase 1 to make sure it still works correctly!

---

# Phase 3: Adding Loops for Multiple Calculations

## Learning Objectives
By the end of this phase, you will be able to:
- Understand what loops are and when to use them
- Implement **while loops** with proper syntax
- Use **conditional statements** to control loop execution
- Handle user input for program control flow

## Understanding While Loops

### What is a While Loop?
A **while loop** repeatedly executes a block of code as long as a condition remains true. It's perfect for situations where you don't know exactly how many times you need to repeat something.

### Basic While Loop Syntax
```python
while condition:
    # Code that repeats
    # Make sure to eventually change the condition!
```

### Examples of While Loops

**Example 1: Simple Counter**
```python
count = 1
while count <= 3:
    print(f"Count is: {count}")
    count = count + 1  # This changes the condition!
print("Done counting!")
```

**Example 2: User-Controlled Loop**
```python
user_input = ""
while user_input != "quit":
    user_input = input("Enter 'quit' to stop: ")
    if user_input != "quit":
        print(f"You entered: {user_input}")
print("Goodbye!")
```

**Important**: Always make sure your loop condition will eventually become false, or you'll create an **infinite loop**!

## Your Task: Multiple Grade Calculations

Now modify your Phase 2 code to allow calculating grades for multiple students.

### Program Flow
Your program should:
1. Ask for a student's four grade components
2. Calculate and display their overall grade
3. Ask if the user wants to calculate another student's grades
4. Repeat until the user chooses to quit

### Implementation Strategy

Create a **while loop** that continues until the user enters a quit command:

```python
# Your input_float and calculate_overall_grade functions go here (from Phase 2)

user_choice = ""
while user_choice.lower() != "quit":
    print("\n--- Grade Calculator ---")
    
    # Get grades using your functions from Phase 2
    # Calculate overall grade using your function
    # Display the result
    
    user_choice = input("\nEnter 'quit' to exit, or press Enter to calculate another grade: ")

print("Thanks for using the grade calculator!")
```

### Key While Loop Concepts
- **Loop Condition**: `user_choice.lower() != "quit"` - continues as long as user doesn't type "quit"
- **Loop Variable**: `user_choice` - this variable controls whether the loop continues
- **Loop Body**: All the indented code that repeats each iteration
- **Condition Update**: Getting new input for `user_choice` at the end of each loop

**Syntax Reminders**:
- Don't forget the colon `:` after the while condition
- All code inside the loop must be indented
- Use `.lower()` to handle "QUIT", "Quit", "quit", etc. the same way

## Testing Phase 3

Test your complete program by:
1. Calculating grades for at least 2 different students
2. Testing both "quit" and "QUIT" (case insensitivity)  
3. Verifying that calculations are still correct
4. Making sure the program exits cleanly when you quit

## Final Submission Requirements

Submit your completed `grade_calculator.py` file that includes all three phases (you can comment out the first two phases with a multi-line comment).
Your final program should:
- [ ] Use the `input_float()` function for all grade input
- [ ] Use the `calculate_overall_grade()` function for calculations
- [ ] Allow multiple grade calculations using a while loop
- [ ] Handle the quit command (case-insensitive)
- [ ] Display results with proper f-string formatting
- [ ] Include appropriate prompts and user-friendly output