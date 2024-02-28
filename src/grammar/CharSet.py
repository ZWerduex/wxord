import random

class CharSet:

    def __init__(self, chars: list[str], weights : list[int] = None) -> None: # type: ignore
        if weights and len(chars) != len(weights):
            raise ValueError('Length of chars and weights must be the same')
        if len(chars) != len(set(chars)):
            raise ValueError(f'Found duplicate chars in {chars}')
        self.chars = chars
        self.weights = weights if weights else [1] * len(chars)

    def pick(self) -> str:
        return random.choices(self.chars, weights=self.weights)[0]