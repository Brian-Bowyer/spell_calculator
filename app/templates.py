from typing import Callable

from nicegui import ui


def card_title(label: str):
    with ui.card_section().classes("border w-full bg-teal-800 text-white"):
        ui.label(label)


def field_card():
    return ui.card_section().classes("w-full border")


def field(label: str, field_generator: Callable):
    with field_card():
        ui.markdown(f"###### {label}")
        field_generator()
