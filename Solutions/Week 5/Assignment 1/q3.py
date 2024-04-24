"""
Make a dictionary with keys as subject name (physics, chemistry, etc.) 
and values as their marks. 
Print the name of the subject which has marks more than passing marks (above 33).
"""

from typing import Dict

subject_marks: Dict[str, int] = {
    "physics": 67,
    "chemistry": 12,
    "english": 22,
    "computer": 19,
    "hindi": 54,
}

for subject, mark in subject_marks.items():
    if mark >= 33:
        print(subject)
