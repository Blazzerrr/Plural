class Plural:
    def __init__(self, firstValue, secondValue, thirdValue):
        self.firstValue = firstValue
        self.secondValue = secondValue
        self.thirdValue = thirdValue

    def plural_result(self, n):
        values = [self.firstValue, self.secondValue, self.thirdValue]

        n = float(n)
        if n % 1 == 0:
            n = int(n)

        if n % 10 == 1 and n % 100 != 11:
            p = 0
        elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
            p = 1
        else:
            p = 2

        return str(n) + ' ' + values[p] 