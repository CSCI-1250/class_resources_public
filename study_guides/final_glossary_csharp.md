# CSCI 1250 C# Programming Glossary
**Comprehensive Reference for Final Exam**

---

## **A**

**Access Modifier**  
Keywords that determine the visibility and accessibility of classes, methods, and variables. Examples: `public`, `private`, `protected`, `internal`.

**Accessor (getter)**  
The `get` portion of a property that allows reading the property's value.

**AND Operator (&&)**  
Logical operator that returns `true` only when both operands are `true`. Example: `true && false` returns `false`.

**Argument**  
The actual value passed to a method when it's called. Distinguished from parameter (the variable in the method signature).

**Array**  
A collection of elements of the same type stored in contiguous memory locations. Has fixed size and uses `.Length` property.

**Assignment Operator (=)**  
Operator used to assign a value to a variable. Example: `int x = 5;`

**Auto-Implemented Property**  
A property where C# automatically creates the backing field. Example: `public string Name { get; set; }`

---

## **B**

**Backing Field**  
A private field that stores the actual data for a property when not using auto-implemented properties.

**bool (Boolean)**  
Data type that can only hold two values: `true` or `false`. Used for conditions and flags.

**Boolean Expression**  
An expression that evaluates to either `true` or `false`. Often used in conditional statements.

---

## **C**

**camelCase**  
Naming convention where the first word is lowercase and subsequent words are capitalized. Used for local variables and parameters. Example: `studentCount`

**Casting**  
Explicitly converting one data type to another. Example: `(double)5` converts integer 5 to double 5.0.

**char (Character)**  
Data type that stores a single Unicode character. Example: `char grade = 'A';`

**Class**  
A blueprint or template for creating objects. Defines the structure and behavior of objects.

**Class Members**  
Elements that belong to a class, including fields, properties, methods, and constructors.

**Compound Assignment Operators**  
Operators that combine arithmetic operations with assignment. Examples: `+=`, `-=`, `*=`, `/=`

**Constructor**  
Special method called when creating an object. Initializes the object's state. Has the same name as the class.

**Control Variable**  
A variable that determines how many times a loop executes. It's initialized, tested, and modified during loop execution.

---

## **D**

**Data Type**  
Specifies what kind of data a variable can hold. Examples: `int`, `double`, `string`, `bool`, `char`

**decimal**  
Data type for high-precision decimal numbers, typically used for financial calculations.

**Declaration**  
Creating a variable by specifying its data type and name. Example: `int age;`

**Decrement Operator (--)**  
Operator that decreases a variable's value by 1. Example: `count--`

**Default Constructor**  
A constructor with no parameters that provides default values for object initialization.

**do-while Loop**  
A post-test loop that executes at least once before checking the condition.

**double**  
Data type for double-precision floating-point numbers. Used for decimal values.

**Dynamic Allocation**  
Memory allocation that occurs at runtime, typically for objects stored on the heap.

---

## **E**

**Encapsulation**  
Object-oriented principle of bundling data and methods together and hiding internal implementation details.

**Equality Operator (==)**  
Comparison operator that checks if two values are equal. Returns a boolean result.

**Explicit Casting**  
Manually converting one data type to another using cast syntax. Example: `(int)3.14`

---

## **F**

**Field**  
A variable declared within a class. Typically private to maintain encapsulation.

**File I/O (Input/Output)**  
Operations for reading from and writing to files. Common methods: `File.ReadAllLines()`, `File.WriteAllLines()`

**foreach Loop**  
A loop designed to iterate through collections without managing index variables. Example: `foreach (int num in numbers)`

**for Loop**  
A loop with initialization, condition, and update expressions all in the header.

---

## **G**

**Garbage Collection**  
Automatic memory management system that reclaims memory from objects no longer in use.

**Greater Than (>)**  
Comparison operator that checks if the left operand is greater than the right operand.

**Greater Than or Equal (>=)**  
Comparison operator that checks if the left operand is greater than or equal to the right operand.

---

## **H**

**Heap Memory**  
Memory area where reference types (objects, arrays, strings) are stored. Managed by garbage collection.

---

## **I**

**Implicit Conversion**  
Automatic type conversion that occurs when no data loss will happen. Example: `int` to `double`

**Increment Operator (++)**  
Operator that increases a variable's value by 1. Example: `count++`

**Index**  
The position of an element in an array or string, starting from 0.

**Index Out of Range**  
Error that occurs when trying to access an array or string position that doesn't exist.

**Initialization**  
Giving a variable its first value. Example: `int count = 0;`

**Instance**  
A specific object created from a class. Also called an object.

**Instance Members**  
Fields, properties, and methods that belong to a specific object instance.

**int (Integer)**  
Data type for whole numbers without decimal places.

**Integer Division**  
Division between two integers that truncates the decimal portion. Example: `5 / 2` = `2`

**internal**  
Access modifier that allows access within the same assembly/project but not from external assemblies.

---

## **L**

**Length Property**  
Property of arrays and strings that returns the number of elements/characters. No parentheses needed.

**Less Than (<)**  
Comparison operator that checks if the left operand is less than the right operand.

**Less Than or Equal (<=)**  
Comparison operator that checks if the left operand is less than or equal to the right operand.

**LIFO (Last In, First Out)**  
Principle describing how the stack memory works - last allocated memory is first deallocated.

**List**  
Dynamic collection that can grow and shrink during runtime. Uses `.Count` property and methods like `.Add()`, `.Remove()`

**Local Variable**  
A variable declared within a method that's only accessible within that method's scope.

**Logical Operators**  
Operators that work with boolean values: AND (`&&`), OR (`||`), NOT (`!`)

---

## **M**

**Method**  
A block of code that performs a specific task. Can accept parameters and return values.

**Method Signature**  
The declaration of a method including its name, parameters, and return type.

**Modifier (setter)**  
The `set` portion of a property that allows changing the property's value.

**Modulo Operator (%)**  
Arithmetic operator that returns the remainder after division. Example: `10 % 3` = `1`

---

## **N**

**Naming Conventions**  
Standardized ways of naming code elements. C# uses PascalCase for classes/methods, camelCase for variables.

**NOT Operator (!)**  
Logical operator that reverses a boolean value. Example: `!true` = `false`

**Not Equal (!=)**  
Comparison operator that checks if two values are different.

---

## **O**

**Object**  
An instance of a class containing data and methods. Created using the `new` keyword.

**Object-Oriented Programming (OOP)**  
Programming paradigm based on objects that contain data and methods.

**OR Operator (||)**  
Logical operator that returns `true` when at least one operand is `true`. Example: `false || true` = `true`

**Order of Operations**  
The precedence rules for evaluating expressions. For booleans: `()` → `!` → `&&` → `||`

**out Parameter**  
Parameter that passes a value back from a method. Used with `TryParse` methods.

**Override**  
Providing a new implementation for a method inherited from a base class. Example: overriding `ToString()`

---

## **P**

**Parameter**  
A variable in a method signature that receives values when the method is called.

**Parameterized Constructor**  
A constructor that accepts parameters to initialize object fields with specific values.

**Parsing**  
Converting a string representation to another data type. Example: `int.Parse("42")`

**PascalCase**  
Naming convention where each word starts with a capital letter. Used for classes, methods, and properties.

**Post-test Loop**  
A loop that checks its condition after executing the loop body (do-while loop).

**Pre-test Loop**  
A loop that checks its condition before executing the loop body (while and for loops).

**private**  
Access modifier that restricts access to within the same class only.

**Property**  
A class member that provides controlled access to private fields through get and set accessors.

**protected**  
Access modifier that allows access within the same class and derived classes.

**public**  
Access modifier that allows access from anywhere in the program.

---

## **R**

**Reference Type**  
Data types that store references (addresses) to memory locations on the heap. Examples: objects, arrays, strings.

**Relational Operators**  
Operators that compare values and return boolean results. Examples: `==`, `!=`, `>`, `<`, `>=`, `<=`

**return Statement**  
Statement that exits a method and optionally returns a value to the caller.

**Return Type**  
The data type that a method returns. Use `void` if the method doesn't return anything.

---

## **S**

**Scope**  
The region of code where a variable or method can be accessed.

**Stack Memory**  
Memory area where value types and references to objects are stored. Fast access with automatic cleanup.

**static**  
Keyword indicating that a member belongs to the class itself rather than to instances.

**string**  
Reference type for storing text. Immutable and stored on the heap.

**String Indexing**  
Accessing individual characters in a string using bracket notation. Example: `word[0]`

**String Methods**  
Methods for manipulating strings. Examples: `ToUpper()`, `ToLower()`, `Trim()`, `Contains()`, `Substring()`

**Substring**  
A portion of a string extracted using the `Substring()` method.

---

## **T**

**ToString() Method**  
Method that returns a string representation of an object. Can be overridden for custom formatting.

**TryParse**  
Safe parsing method that returns `true` if conversion succeeds, `false` otherwise. Prevents exceptions.

**Truncation**  
Cutting off the decimal portion of a number, which happens in integer division.

**Type Conversion**  
Changing data from one type to another, either implicitly or explicitly.

---

## **U**

**Unary Operators**  
Operators that work on a single operand. Examples: `++`, `--`, `!`, `-`

---

## **V**

**Value Type**  
Data types that store actual values on the stack. Examples: `int`, `double`, `bool`, `char`

**Variable**  
A named storage location that can hold data of a specific type.

**void**  
Keyword indicating that a method doesn't return a value.

---

## **W**

**while Loop**  
A pre-test loop that continues executing as long as its condition is `true`.

---

## **Quick Reference Patterns**

### **Common Method Patterns:**
```csharp
// Method with return value
public static returnType MethodName(parameterType param)
{
    return value;
}

// Void method (no return)
public static void MethodName(parameterType param)
{
    // statements
}
```

### **Property Patterns:**
```csharp
// Auto-implemented
public DataType PropertyName { get; set; }

// With backing field
private dataType fieldName;
public DataType PropertyName
{
    get { return fieldName; }
    set { fieldName = value; }
}
```

### **Constructor Pattern:**
```csharp
public ClassName(parameters)
{
    // initialization
}
```

### **Common Mistakes to Avoid:**
- Using `.Length()` instead of `.Length` (Length is a property!)
- Using `.Count` on arrays or `.Length` on Lists
- Integer division when you need decimal results
- Forgetting access modifiers (defaults to private for fields)
- Using `=` instead of `==` in conditions

---

*This glossary covers all terminology from CSCI 1250. Use it as a quick reference during studying and programming!*