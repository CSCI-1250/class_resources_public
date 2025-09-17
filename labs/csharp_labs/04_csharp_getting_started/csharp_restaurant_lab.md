# C# Restaurant Order System Lab

## Objective
Create a console application that simulates a simple restaurant ordering system. This lab will help you practice C# syntax, data types, string interpolation, user input handling, and mathematical operations while building on programming concepts you already know.

## Setup Instructions

### Creating Your C# Project
1. Open your terminal/command prompt
2. Navigate to where you want to create your project
3. Run these commands:
   ```bash
   dotnet new console -n RestaurantOrder
   cd RestaurantOrder
   ```
4. Open the `Program.cs` file in your text editor
5. Replace the default code with your solution

### Building and Running
- To build: `dotnet build`
- To run: `dotnet run`
- To do both: `dotnet run` (builds automatically if needed)

## Requirements

Create a program that:

1. **Welcomes the customer** and displays a simple menu with at least 4 items and their prices
2. **Takes orders** by asking the customer to enter:
   - Item name or number
   - Quantity for each item
3. **Calculates totals** including:
   - Subtotal
   - Tax (use 8.5%)
   - Final total
4. **Displays a receipt** using string interpolation showing:
   - Each item ordered with quantity and line total
   - Subtotal, tax amount, and final total
   - Formatted to 2 decimal places

## Technical Requirements

- Use appropriate data types (`int`, `double`, `decimal`, `string`)
- Use string interpolation for formatted output
- Handle user input properly (consider `int.Parse()` or `int.TryParse()`)
- Use meaningful variable names following C# conventions
- Include proper semicolons and curly braces
- Everything must be inside your `Program` class and `Main` method

## Sample Menu Ideas
```
1. Burger - $8.99
2. Fries - $3.49
3. Soda - $2.29
4. Salad - $6.75
```

## Example Output
```
Welcome to Ryan's Diner!
Menu:
1. Burger - $8.99
2. Fries - $3.49
...

Enter item number: 1
Enter quantity: 2
Add another item? (y/n): y
Enter item number: 2
Enter quantity: 1
Add another item? (y/n): n

--- Receipt ---
2x Burger: $17.98
1x Fries: $3.49
Subtotal: $21.47
Tax (8.5%): $1.82
Total: $23.29
```

## Helpful Hints

- Remember that in C#, you need to declare variable types explicitly
- Use `decimal` for money calculations to avoid floating-point precision issues
- String interpolation syntax: `$"Total: {variable:F2}"` (F2 formats to 2 decimal places)
- Console input always comes in as strings - you'll need to convert to numbers
- Consider creating arrays or variables to store your menu items and prices

## Reflection Questions
When you finish, add these questions and your answers as a multiline comment at the top of your file:

```csharp
/*
Reflection Questions:
1. What data types did you choose for prices and quantities? Why?
2. How did you handle the tax calculation? Did you use int, double, or decimal?
3. What challenges did you face with string interpolation vs concatenation?
4. How is input handling different in C# compared to Python?
5. What would happen if a user entered invalid input (non-numbers)? How could you improve this?
*/
```

## Submission
Submit your completed `Program.cs` file with the reflection questions answered in the multiline comment at the top.

## Extension Challenges (Optional)
- Research the [TryParse](https://letmegooglethat.com/?q=use+tryparse+method+validate+input+C%23) method and add input validation using `TryParse()`
- Allow customers to remove items from their order
- Add a discount for orders over a certain amount
- Create a more sophisticated menu with categories