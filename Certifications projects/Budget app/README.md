# Budget App

A Python module for tracking spending across categories and visualizing relative spend as a bar chart.

## Classes

### `Category(name)`

Represents a budget category (e.g. Food, Clothing). Each instance holds a `ledger` list of transactions.

| Method | Description |
|---|---|
| `deposit(amount, description='')` | Adds a positive transaction to the ledger |
| `withdraw(amount, description='')` | Adds a negative transaction; returns `False` if insufficient funds |
| `get_balance()` | Returns the current balance (sum of all ledger amounts) |
| `transfer(amount, destination)` | Withdraws from self and deposits into another category; returns `False` if insufficient funds |
| `check_funds(amount)` | Returns `False` if amount exceeds balance — used internally by `withdraw` and `transfer` |

#### Printing a Category

```python
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
print(food)
```

```
*************Food*************
initial deposit        1000.00
groceries               -10.15
Total: 989.85
```

- Title: 30 characters wide, name centered with `*`
- Each row: description truncated to 23 chars (left-aligned) + amount to 2 decimal places (right-aligned, max 7 chars)
- Last line: running total

---

## Functions

### `create_spend_chart(categories)`

Returns a bar chart string showing the percentage of total withdrawals per category, rounded **down** to the nearest 10.

```python
food = Category('Food')
clothing = Category('Clothing')
food.deposit(1000)
food.withdraw(600)
clothing.deposit(1000)
clothing.withdraw(400)
print(create_spend_chart([food, clothing]))
```

```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o  o     
 30| o  o     
 20| o  o     
 10| o  o     
  0| o  o     
    -------
     F  C  
     o  l  
     o  o  
     d  t  
        h  
        i  
        n  
        g  
```

- Only withdrawals count toward percentages (not deposits)
- Bars use `o` characters
- Category names are printed vertically below the chart

---

## File Structure

```
budget.py    # Category class + create_spend_chart function
README.md    # This file
```