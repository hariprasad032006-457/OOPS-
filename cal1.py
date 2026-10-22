from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Calculator:
    """A simple calculator for two numeric values."""

    a: float
    b: float

    def add(self) -> float:
        """Return the sum of a and b."""
        return self.a + self.b

    def subtract(self) -> float:
        """Return the difference between a and b."""
        return self.a - self.b

    def multiply(self) -> float:
        """Return the product of a and b."""
        return self.a * self.b

    def divide(self) -> float:
        """Return a divided by b.

        Raises:
            ZeroDivisionError: If b is zero.
        """
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        return self.a / self.b

    def multiplication_table(self, limit: int = 10) -> list[str]:
        """Return the multiplication table for a.

        Args:
            limit: Number of rows in the table.

        Raises:
            ValueError: If limit is less than 1.
        """
        if limit < 1:
            raise ValueError("Table limit must be at least 1.")

        return [
            f"{self.a:g} × {i} = {self.a * i:g}"
            for i in range(1, limit + 1)
        ]


def main() -> None:
    """Run the calculator example."""
    calculator = Calculator(a=10, b=5)

    print(f"Addition:       {calculator.add():g}")
    print(f"Subtraction:    {calculator.subtract():g}")
    print(f"Multiplication: {calculator.multiply():g}")
    print(f"Division:       {calculator.divide():g}")

    print("\nMultiplication Table:")
    for row in calculator.multiplication_table():
        print(row)


if __name__ == "__main__":
    main()