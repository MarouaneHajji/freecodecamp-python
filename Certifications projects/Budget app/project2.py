import math


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []  # list of {'amount': ..., 'description': ...} dicts

    # Append a positive transaction to the ledger
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    # Append a negative transaction; returns False if insufficient funds
    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        self.ledger.append({'amount': -amount, 'description': description})  # store as negative
        return True

    # Sum all amounts in the ledger to get the current balance
    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    # Withdraw from self and deposit into destination category
    def transfer(self, amount, destination):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f'Transfer to {destination.name}')
        destination.deposit(amount, f'Transfer from {self.name}')
        return True

    # Returns True if amount does not exceed current balance
    def check_funds(self, amount):
        return amount <= self.get_balance()

    # Format the category as a 30-char wide ledger printout
    def __str__(self):
        title = self.name.center(30, '*')  # center name between * characters
        lines = [title]
        for item in self.ledger:
            desc = item['description'][:23].ljust(23)       # max 23 chars, left-aligned
            amount = f"{item['amount']:.2f}".rjust(7)       # 2 decimal places, right-aligned in 7 chars
            lines.append(f"{desc}{amount}")
        lines.append(f"Total: {self.get_balance():.2f}")
        return '\n'.join(lines)


def create_spend_chart(categories):
    # Sum withdrawals (negative amounts) per category
    withdrawals = []
    for cat in categories:
        total = sum(-item['amount'] for item in cat.ledger if item['amount'] < 0)
        withdrawals.append(total)

    total_spent = sum(withdrawals)

    # Convert each category's spend to a percentage, rounded DOWN to nearest 10
    percentages = [math.floor(w / total_spent * 100 / 10) * 10 for w in withdrawals]

    # Build y-axis rows from 100 down to 0, placing 'o' where the bar reaches that level
    lines = ['Percentage spent by category']
    for level in range(100, -1, -10):
        row = f"{level:3}| "
        for pct in percentages:
            row += 'o  ' if pct >= level else '   '  # 'o' if category reaches this level
        lines.append(row)

    # Horizontal separator line under the bars
    lines.append('    ' + '-' * (len(categories) * 3 + 1))

    # Print category names vertically, one character per row
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        row = '     '
        for cat in categories:
            row += (cat.name[i] if i < len(cat.name) else ' ') + '  '  # pad shorter names with space
        lines.append(row)

    return '\n'.join(lines)