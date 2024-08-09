from typing import Dict, List, Tuple
from file import File


class Symbols:
    def __init__(self):
        self._start: str = "A"
        self._goal: str = "B"
        self._other: str = " "
        self._coordinates: Dict[str, List[Tuple[int, int]]] = {}
        self._single_start_and_goal: bool

    def symbol_count(self, symbol: str, file: File) -> int:
        return file.contents.count(symbol)

    @property
    def single_start_and_goal(self) -> bool:
        return self._single_start_and_goal

    @single_start_and_goal.setter
    def single_start_and_goal(self, file: File):
        start_count = self.symbol_count(self._start, file)
        goal_count = self.symbol_count(self._goal, file)
        self._single_start_and_goal = (start_count == 1 and goal_count == 1)

    @property
    def coordinates(self) -> Dict[str, List[Tuple[int, int]]]:
        return self._coordinates

    @coordinates.setter
    def coordinates(self, symbol: str, coordinates: Tuple[int, int]):
        self._coordinates[symbol] = coordinates
