from models import Spell
from nicegui import ui
from templates import card_title, field_card, labeled_snap_slider
from utils.constants import ARCANA, PRIMARY_FACTOR


def spell_overview_page(spell: Spell):
    with ui.step(name="first", title="Spell Overview"):
        ui.markdown("##### Spell Overview")

        with ui.row().classes("flex w-full"):
            with ui.card().tight().classes("border w-4/12"):
                card_title("CASTER")

                with field_card():
                    ui.markdown(f"###### Gnosis")
                    labeled_snap_slider(min=1, max=10, step=1).props(
                        "label-always snap"
                    ).bind_value(spell, "gnosis")

                with field_card():
                    ui.markdown().bind_content_from(
                        spell,
                        "arcanum_name",
                        lambda arcanum: f"###### Mage's {arcanum} Arcanum",
                    )
                    labeled_snap_slider(min=1, max=5, step=1).bind_value(
                        spell, "caster_arcanum_value"
                    )

                with field_card():
                    ui.markdown().bind_content_from(
                        spell,
                        "arcanum_name",
                        lambda arcanum: f"###### Is {arcanum} the Mage's Highest Arcanum?",
                    )
                    ui.switch(value=True).bind_value(spell, "is_highest_arcanum")

                with field_card():
                    ui.markdown().bind_content_from(
                        spell,
                        "arcanum_name",
                        lambda arcanum: f"###### Is {arcanum} the Mage's Ruling Arcanum?",
                    )
                    ui.switch(value=True).bind_value(spell, "is_ruling_arcanum")

                with field_card():
                    ui.markdown(f"###### Active Spells")
                    ui.number(value=0, min=0).bind_value(spell, "active_spells")

            with ui.card().tight().classes("border w-4/12"):
                card_title("SPELL")
                with field_card():
                    ui.markdown(f"###### Highest Arcanum Used")
                    ui.select(options=ARCANA).bind_value(
                        spell,
                        "arcanum_name",
                    )
                with field_card():
                    ui.markdown().bind_content_from(
                        spell,
                        "arcanum_name",
                        lambda arcanum: f"###### Spell's Required {arcanum} Arcanum",
                    )

                    def validate_spell_arcanum_value(event):
                        if spell.caster_arcanum_value < event.value:
                            spell.caster_arcanum_value = event.value
                            ui.notify(
                                "Spell Arcanum Value cannot be higher than Caster Arcanum Value",
                                type="warning",
                            )

                    labeled_snap_slider(
                        value=1, min=1, max=5, on_change=validate_spell_arcanum_value
                    ).bind_value(
                        spell,
                        "spell_arcanum_value",
                    )
                with field_card():
                    ui.markdown(f"###### Spell's Primary Factor")
                    ui.select(options=PRIMARY_FACTOR).bind_value(
                        spell,
                        "primary_factor",
                    )
                with field_card():
                    ui.markdown(f"###### Is Rote?")
                    ui.switch(value=False).bind_value(spell, "is_rote")

                with field_card():
                    ui.markdown(f"###### Is Praxis?")
                    ui.switch(value=False).bind_value(spell, "is_praxis")

                with field_card():
                    ui.markdown(f"###### Additional Spellcasting Dice")
                    ui.number(value=0, min=0).bind_value(spell, "additional_dice")

                with field_card():
                    ui.markdown(f"###### Willpower Spent")
                    ui.switch(value=False).bind_value(spell, "is_willpower_spent")

            with ui.card().tight().classes("border w-3/12"):
                card_title("CASTING")
                with field_card():
                    ui.markdown(f"###### Is Resisted?")
                    ui.switch(value=False).bind_value(spell, "is_resisted")
                # hidden: Withstand
                # hidden: Number of Withstand Ratings
