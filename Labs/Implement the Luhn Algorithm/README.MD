# Luhn Algorithm Credit Card Validator

## 📌 Overview

This project implements the **Luhn Algorithm** (also known as the mod 10 algorithm), a simple checksum formula used to validate identification numbers such as credit card numbers.

The program checks whether a given card number is valid or invalid.

---

## ⚙️ How It Works

The validation process follows these steps:

1. **Clean the Input**
   - Remove spaces and dashes from the input string.

2. **Reverse Traversal**
   - Start from the rightmost digit (check digit).

3. **Double Every Second Digit**
   - Moving from right to left, double every second digit (excluding the check digit).

4. **Adjust Large Numbers**
   - If doubling results in a number greater than 9:
     - Subtract 9 from it
     - OR sum its digits (equivalent operation)

5. **Sum All Digits**
   - Add all processed digits together.

6. **Validation Rule**
   - If the total is divisible by 10 → ✅ VALID  
   - Otherwise → ❌ INVALID

---

## 🧠 Example

Input:


453914881


Steps:


Original: 4 5 3 9 1 4 8 8 1
Processed: 4 1 3 9 1 8 8 7 1
Sum = 42 → INVALID


---

## 🧪 Example Usage

```python
verify_card_number('453914889')
# Output: VALID!
verify_card_number('4111-1111-1111-1111')
# Output: VALID!
verify_card_number('1234 5678 9012 3456')
# Output: INVALID!
🚫 Constraints
Do not use external libraries
Handle input with:
Spaces
Dashes
Must return:
"VALID!" or "INVALID!"
🧠 Key Concepts
String processing
Iteration and indexing
Conditional logic
Checksum validation
📂 Project Structure
luhn-validator/
│
├── validator.py   # Main implementation
└── README.md      # Documentation
🚀 Conclusion

This project demonstrates how real-world systems validate card numbers using a lightweight algorithm. It strengthens understanding of loops, conditions, and data validation techniques.