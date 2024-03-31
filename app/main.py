from models import Spell
from nicegui import ui
from pages.spell_overview import spell_overview_page
from utils.constants import STORAGE_SECRET


@ui.page("/")
def main():
    spell = Spell()
    with ui.header():
        ui.label("Header goes here")

    with ui.stepper().props("alternative-labels contractable").classes(
        "flex w-full"
    ) as stepper:
        spell_overview_page(spell)

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
