from typing import Callable

from nicegui import ui


def card_title(label: str):
    with ui.card_section().classes("border w-full bg-teal-800 text-white"):
        ui.label(label)


def field(label: str, field_generator: Callable):
    with ui.card_section().classes("w-full border"):
        ui.markdown(f"###### {label}")
        field_generator()


@ui.page("/")
def main():
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

                    field(
                        "Gnosis",
                        lambda: ui.slider(min=1, max=5, step=1)
                        .props("label-always")
                        .classes("w-full"),
                    )

                    field("Highest Arcanum Used", lambda: None)

                    field("Mage's X Arcanum", lambda: None)

                    field("Is X the Mage's Highest Arcanum?", lambda: None)

                    field("Is X the Mage's Ruling Arcanum?", lambda: None)

                    field("Active Spells", lambda: None)

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


ui.run()
