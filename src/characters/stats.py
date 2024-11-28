from dataclasses import dataclass

@dataclass
class Stats:
    force: int
    agilite: int
    intelligence: int
    pv: int
    energie: int
    bitcoins: int = 1000
    reputation: int = 0 