from typing import Callable
from abc import ABC, abstractmethod


def bisection_root(func: Callable[[int | float], int | float],
                   a: int | float, b: int | float,
                   tolerance=1e-6,
                   max_iterations: int = 100) \
        -> int | float:
    """
    Finds a root of the given function within the interval [a, b]
     using the bisection method.

    Parameters:
        func (Callable[[int | float], int | float]): The function for
         which the root is to be found.
        a (int | float): The left endpoint of the interval.
        b (int | float): The right endpoint of the interval.
        tolerance (float, optional): The acceptable level of error in
         the root approximation. Defaults to 1e-6.
        max_iterations (int, optional): The maximum number of iterations. Defaults to 100.

    Returns:
        int | float: An approximation of the root within the specified tolerance.

    Raises:
        ValueError: If the function has the same sign at both endpoints (func(a) * func(b) > 0).
    """

    if func(a) * func(b) > 0:
        raise ValueError('The multiplication result must be a negative number')
    iteration = 0
    if a > b:
        a, b = b, a
    while (b - a) / 2 > tolerance and iteration < max_iterations:
        c = (a + b) / 2
        if func(c) == 0:
            return c
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c
        iteration += 1
    return round((a + b) / 2, 3)


class Integration(ABC):
    @abstractmethod
    def calculate(self, func: Callable[[int | float], int | float],
                  a: int | float, b: int | float,
                  n: int):
        """
        Parameters:
        func (Callable[[int | float], int | float]): Function to be integrated.
        a (int | float): The lower limit of integration.
        b (int | float): The upper limit of integration.
        n (int): The number of trapezoids used to divide the area under
         the curve.

    Returns:
        float: The estimated value of the definite integral.
        """
        pass


class TrapezoidalIntegration(Integration):

    def calculate(self,
                  func: Callable[[int | float], int | float],
                  a: int | float, b: int | float,
                  n: int):
        """
        Approximates the definite integral of a function using the trapezoidal
        rule. Evaluates area under the curve by dividing the total area into
        smaller trapzoids.
        """
        h = (b - a) / n
        integral_approximation = 0.5 * (func(a) + func(b))

        for i in range(1, n):
            x = a + i * h
            integral_approximation += func(x)
        return integral_approximation * h


class RectangularIntegration(Integration):

    def calculate(self,
                  func: Callable[[int | float], int | float],
                  a: int | float, b: int | float,
                  n: int):
        """
        Approximates the definite integral of a function using the rectangle rule.
        In other words - evaluates area under the curve by dividing the total area
        into smaller rectangles.
        """

        h = (b - a) / n
        integral_approximation = 0

        for i in range(n):
            x = a + (i + 0.5) * h
            rectangle_area = func(x) * h
            integral_approximation += rectangle_area
        return integral_approximation
