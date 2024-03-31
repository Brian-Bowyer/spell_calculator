from dataclasses import dataclass

from utils.constants import ARCANA


@dataclass
class Caster:
    def __init__(self):
        self.gnosis = 1
        self.arcanum_name = ARCANA[0]
        self.arcanum_value = 1
        self.is_highest_arcanum = True
        self.is_ruling_arcanum = True
        self.active_spells = 0
