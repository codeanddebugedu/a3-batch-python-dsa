"""
Make a dictionary with keys as subject name (physics, chemistry, etc.) 
and values as their marks. Print the highest marks scored
"""

from typing import Dict

subject_marks: Dict[str, int] = {
    "physics": 67,
    "chemistry": 12,
    "english": 95,
    "computer": 99,
    "hindi": 54,
}

highest = 0

for mark in subject_marks.values():
    if mark > highest:
        highest = mark

print(highest)
