from dataclasses import dataclass
from math import ceil

from utils.constants import ARCANA, PRIMARY_FACTOR


@dataclass
class Spell:
    # Caster properties
    gnosis: int = 1
    arcanum_name: str = ARCANA[0]
    caster_arcanum_value: int = 1
    is_highest_arcanum: bool = True
    is_ruling_arcanum: bool = True
    active_spells: int = 0

    # Spell properties
    spell_arcanum_value: int = 1
    primary_factor: str = PRIMARY_FACTOR[0]  # TODO enum?
    is_rote: bool = False
    is_praxis: bool = False
    additional_dice: int = 0
    is_willpower_spent: bool = False

    # Casting properties
    is_resisted: bool = False
    max_withstand: int | None = None
    num_withstands: int | None = None

    @property
    def dice(self) -> int:
        # TODO add yantras
        return int(
            self.gnosis
            + self.caster_arcanum_value
            + (self.additional_dice if self.additional_dice else 0)
            + (3 if self.is_willpower_spent else 0)
        )

    @property
    def free_reach(self) -> int:
        return self.caster_arcanum_value - self.spell_arcanum_value + 1

    @property
    def used_reach(self) -> int:
        # TODO calculate used reach
        return 0

    @property
    def reach(self) -> str:
        return f"{self.used_reach}/{self.free_reach}"

    @property
    def paradox(self) -> int:
        # TODO add witness paradox
        overreach = self.free_reach - self.used_reach
        overreach_modifier = ceil(self.gnosis / 2)
        return overreach * overreach_modifier
