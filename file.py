class File:

    def __init__(self, filename: str):
        self._filename = filename
        self._contents = open(self._filename).read()

    @property
    def contents(self) -> str:
        return self._contents
