from typing import List

def return_evens(numbers: List[int]) -> List[int]:
    return [n for n in numbers if n % 2 == 0]

def make_exclamation(sentences: List[str]) -> List[str]:
    return [sentence + "!" for sentence in sentences]
