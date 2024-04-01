from typing import Callable

from nicegui import ui


def card_title(label: str):
    with ui.card_section().classes("border w-full bg-teal-800 text-white"):
        ui.label(label)


def field_card():
    return ui.card_section().classes("w-full border")


@ui.refreshable
def labeled_snap_slider(*args, **kwargs):
    return ui.slider(*args, **kwargs).props("label-always snap")


def chip():
    return ui.badge().props("color=cyan rounded").classes("text-base font-bold")
