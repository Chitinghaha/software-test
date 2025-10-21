class Calculator:
    def add(self, a, b):
        """加法運算"""
        return a + b

    def subtract(self, a, b):
        """減法運算"""
        return a - b

    def multiply(self, a, b):
        """乘法運算"""
        return a * b

    def divide(self, a, b):
        """
        除法運算，回傳浮點數。
        若 b = 0，丟出 ValueError。
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return float(a) / float(b)
