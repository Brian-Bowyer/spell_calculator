from dataclasses import dataclass
from typing import Callable

from nicegui import ui
from utils.constants import ARCANA, STORAGE_SECRET


def card_title(label: str):
    with ui.card_section().classes("border w-full bg-teal-800 text-white"):
        ui.label(label)


def field_card():
    return ui.card_section().classes("w-full border")


def field(label: str, field_generator: Callable):
    with field_card():
        ui.markdown(f"###### {label}")
        field_generator()


@dataclass
class Caster:
    def __init__(self):
        self.gnosis = 1
        self.arcanum_name = ARCANA[0]
        self.arcanum_value = 1
        self.is_highest_arcanum = True
        self.is_ruling_arcanum = True
        self.active_spells = 0


@ui.page("/")
def main():
    caster = Caster()
    with ui.header():
        ui.label("Header goes here")

    with ui.stepper().props("alternative-labels contractable").classes(
        "flex w-full"
    ) as stepper:
        with ui.step(name="first", title="Spell Overview"):
            ui.markdown("##### Spell Overview")

            with ui.row().classes("flex w-full"):
                with ui.card().tight().classes("border w-4/12"):
                    card_title("CASTER")

                    with field_card():
                        ui.markdown(f"###### Gnosis")
                        ui.slider(min=1, max=10, step=1).props(
                            "label-always snap"
                        ).bind_value(caster, "gnosis")

                    with field_card():
                        ui.markdown(f"###### Highest Arcanum Used")
                        ui.select(options=ARCANA).bind_value(
                            caster,
                            "arcanum_name",
                        )
                    with field_card():
                        ui.markdown().bind_content_from(
                            caster,
                            "arcanum_name",
                            lambda arcanum: f"###### Mage's {arcanum} Arcanum",
                        )
                        ui.slider(min=1, max=5, step=1).props(
                            "label-always snap"
                        ).bind_value(caster, "arcanum_value")

                    with field_card():
                        ui.markdown().bind_content_from(
                            caster,
                            "arcanum_name",
                            lambda arcanum: f"###### Is {arcanum} the Mage's Highest Arcanum?",
                        )
                        ui.switch(value=True).bind_value(caster, "is_highest_arcanum")

                    with field_card():
                        ui.markdown().bind_content_from(
                            caster,
                            "arcanum_name",
                            lambda arcanum: f"###### Is {arcanum} the Mage's Ruling Arcanum?",
                        )
                        ui.switch(value=True).bind_value(caster, "is_ruling_arcanum")

                    with field_card():
                        ui.markdown(f"###### Active Spells")
                        ui.number(value=0, min=0).bind_value(caster, "active_spells")

                with ui.card().tight().classes("border w-4/12"):
                    card_title("SPELL")
                    field("Spell's Required X Arcanum", lambda: None)
                    field("Primary Factor", lambda: None)
                    field("Is Rote?", lambda: None)
                    field("Is Praxis?", lambda: None)
                    field("Additional Spellcasting Dice", lambda: None)
                    field("Willpower Spent", lambda: None)

                with ui.card().tight().classes("border w-3/12"):
                    card_title("SUBJECT")
                    field("Is Resisted?", lambda: None)
                    # hidden: Withstand
                    # hidden: Number of Withstand Ratings

        with ui.step(name="second", title="Factors"):
            ui.label("pass")

        with ui.step(name="third", title="Yantras"):
            ui.label("pass")

        with ui.step(name="fourth", title="Paradox"):
            ui.label("pass")

        with ui.step(name="fifth", title="Summary"):
            ui.label("pass")

    with ui.footer():
        ui.label("Footer goes here")


ui.run(storage_secret=STORAGE_SECRET)
