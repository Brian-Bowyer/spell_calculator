import os

ARCANA = [
    "Death",
    "Fate",
    "Forces",
    "Life",
    "Matter",
    "Mind",
    "Prime",
    "Space",
    "Spirit",
    "Time",
]
PRIMARY_FACTOR = [
    "Potency",
    "Duration",
    "Potency (swapped from Duration)",
    "Duration (swapped from Potency)",
]
STORAGE_SECRET = os.getenv("STORAGE_SECRET", "local_storage_secret")
