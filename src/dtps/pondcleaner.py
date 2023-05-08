import random
from dataclasses import dataclass

__all__ = ["CleaningResults", "DTPS"]


@dataclass
class CleaningResults:
    garbage: float


class DTPS:
    def clean(self) -> CleaningResults:
        garbage = random.uniform(0, 3)
        return CleaningResults(garbage)
