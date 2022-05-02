"""
Perform basic statistics on a collection of small positive integers
allowed values 0 < x < 1000
"""
from __future__ import annotations

from typing import Dict

from app.validators.inputvalidator import valid_input

MIN_VAL = 1
MAX_VAL = 999


class DataCapture():
    """DataCapture holds a # of repetitions of small positive integers (0<x<1000)
    from which statistics can be perform."""

    def __init__(self) -> None:
        self.numbers_dict: Dict[int, int] = {}

    @valid_input()
    def add(self, num: int) -> None:
        """Add a number to the collection of numbers."""

        if num not in self.numbers_dict.keys():
            self.numbers_dict[num] = 1
        else:
            self.numbers_dict[num] += 1

    def build_stats(self) -> StatsEngine:
        """Return StatsEngine instance."""
        return StatsEngine(self)


class StatsEngine:
    """StatsEngine can perform basic statistics on a DataCapture Object."""

    def __init__(self, datacapture: DataCapture) -> None:
        self.datacapture = datacapture
        self.cumulative_counter: Dict[int, int] = {}
        accumulator = 0
        for x in range(MIN_VAL, MAX_VAL + 1):
            if x in self.datacapture.numbers_dict.keys():
                accumulator += self.datacapture.numbers_dict[x]
            self.cumulative_counter[x] = accumulator

    @valid_input()
    def less(self, num: int) -> int:
        """Return the amount of numbers less than 'num'."""
        if num == MIN_VAL:
            return 0
        return self.between(MIN_VAL, num - 1)

    @valid_input()
    def greater(self, num: int) -> int:
        """Return the amount of numbers greater than 'num'."""
        if num == MAX_VAL:
            return 0
        return self.between(num + 1, MAX_VAL)

    @valid_input()
    def between(self, num_a: int, num_b: int) -> int:
        """Return the amount of numbers between [num_a, num_b]."""
        upper = max(num_a, num_b)
        lower = min(num_a, num_b)

        if lower == MIN_VAL:
            return self.cumulative_counter[upper]

        return (self.cumulative_counter[upper] -
                self.cumulative_counter[lower - 1])
