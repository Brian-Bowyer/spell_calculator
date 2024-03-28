from nicegui import ui


@ui.page("/")
def main():
    with ui.row().classes("w-full h-full border flex-wrap"):
        columns = [ui.column().classes("flex-auto border") for _ in range(3)]
        with columns[0]:
            cards = [ui.card().classes("w-full items-center") for _ in range(3)]
            with cards[0]:
                ui.label("Lorem ipsum")

            with cards[1]:
                ui.label("Lorem ipsum")

            with cards[2]:
                ui.label("Lorem ipsum")
        with columns[1]:
            cards = [ui.card().classes("w-full items-center") for _ in range(3)]
            with cards[0]:
                ui.label("Lorem ipsum")

            with cards[1]:
                ui.label("Lorem ipsum")

            with cards[2]:
                ui.label("Lorem ipsum")
        with columns[2]:
            cards = [ui.card().classes("w-full items-center") for _ in range(3)]
            with cards[0]:
                ui.label("Lorem ipsum")

            with cards[1]:
                ui.label("Lorem ipsum")

            with cards[2]:
                ui.label("Lorem ipsum")


ui.run()
