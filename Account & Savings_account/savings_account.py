from Account import Account

class Savings(Account):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)
        self.interest_rate = 0.02
        # Part 1: Add the withdraw limit attribute
        self.withdraw_limit = 100

    # Part 2: Override the withdrawal behavior
    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            print(f"Withdrawal failed! Amount exceeds the ${self.withdraw_limit} limit.")
        else:
            # This tells Python to use the original withdrawal rules from the Account file
            super().withdraw(amount)

# This part tests the code to make sure it works
if __name__ == "__main__":
    test_account = Savings("Akindunbi", 500)
    print("--- Testing Limit (Trying to take $150) ---")
    test_account.withdraw(150)
    print("--- Testing Normal (Taking $50) ---")
    test_account.withdraw(50)