"""
Make a dictionary with keys as subject name (physics, chemistry, etc.)
and values as their marks. Print the name of the subject with highest marks scored.
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
highest_subject = ""
for subject, mark in subject_marks.items():
    if mark > highest:
        highest = mark
        highest_subject = subject

print(f"Highest marks scored is {highest} in {highest_subject} subject")
