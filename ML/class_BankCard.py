"""
У студента есть кредитная карта банка, на
который лежат деньги в долларах. Требуется реализовать класс
BankCard
"""

class BankCard:
    def __init__(self, total_sum):
        self.total_sum = total_sum

    def __repr__(self):
        return "To learn the balance you should put the money on the card, spent some money or get the bank data. The last procedure is not free and costs 1 dollar."

    def __call__(self, sum_spent):
        try:
            if self.total_sum >= sum_spent:
                self.total_sum -= sum_spent
                return("You spent", sum_spent, "dollars.", self.total_sum, "dollars are left.")
        except ValueError:
            print("Not enough money to spent", sum_spent(), "dollars.")

    @property
    def balance(self):
        try:
            if self.total_sum > 0:
                self.total_sum -= 1
                return self.total_sum
        except ValueError:
            print("Not enough money to learn the balance.")

    def put(self, sum_put):
        self.total_sum += sum_put
        return("You put", sum_put, "dollars.", self.total_sum, "dollars are left.")


