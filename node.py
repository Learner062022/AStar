import sys


class Node:

    def __init__(self, state: ..., parent: ..., action: ...):
        self._state = state
        self._parent = parent
        self._action = action

    @property
    def state(self) -> ...:
        return self._state

    @property
    def parent(self) -> ...:
        return self._parent

    @property
    def action(self) -> ...:
        return self._action
