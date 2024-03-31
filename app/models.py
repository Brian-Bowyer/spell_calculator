from dataclasses import dataclass

from utils.constants import ARCANA, PRIMARY_FACTOR


@dataclass
class Caster:
    def __init__(self):
        self.gnosis = 1
        self.arcanum_value = 1
        self.is_highest_arcanum = True
        self.is_ruling_arcanum = True
        self.active_spells = 0


@dataclass
class Spell:
    def __init__(self):
        self.arcanum_name = ARCANA[0]
        self.arcanum_value = 1
        self.primary_factor = PRIMARY_FACTOR[0]
        self.is_rote = False
        self.is_praxis = False
        self.additional_dice = 0
        self.is_willpower_spent = False


@dataclass
class Casting:
    def __init__(self):
        self.is_resisted = False
        self.max_withstand = None
        self.num_withstands = None
