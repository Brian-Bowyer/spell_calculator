from models import Caster
from nicegui import ui
from templates import card_title, field, field_card
from utils.constants import ARCANA


def spell_overview_page():
    caster = Caster()
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
                    ui.slider(min=1, max=5, step=1).props("label-always snap").bind_value(
                        caster, "arcanum_value"
                    )

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
