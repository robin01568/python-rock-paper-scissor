class Solution:
    def __init__(self) -> object:
        pass

    def add(self, a: int, b: int, *c: int, d: dict) -> float:
        try:
            addition: float = round(float(a + b + sum(c) + sum(d["a"])), 2)
            return addition
        except Exception as e:
            return e

    def multiply(self, a: int, b: int, *c: int, d: dict) -> float:
        try:
            multiplication: float = round(float(a * b * sum(c) * sum(d["a"])), 2)
            return multiplication
        except Exception as e:
            return e


# Input Values
a: int = 11
b: int = 23
c: list = [1, 2, 3, 4]
d: dict = {"a": [1, 2, 3]}

# Create an instance of Solution
solution = Solution()

# Call the methods
addition = solution.add(a, b, *c, d=d)
print(f"{addition = }")

multipication = solution.multiply(a, b, *c, d=d)
print(f"{multipication = }")
