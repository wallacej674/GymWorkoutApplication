import sqlite3
import threading
from  dataclasses import dataclass 

@dataclass
class Exercise:
    id: str
    name: str
    primary_muscle: str
    secondary_muscle: List[str]
    equipment: str
    instructions: str