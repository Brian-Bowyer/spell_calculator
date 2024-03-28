from nicegui import ui


@ui.page("/")
def main():
    with ui.row().classes("full-width full-height border flex-wrap"):
        with ui.column().classes("flex-auto border"):
            with ui.card():
                ui.label("1")

            with ui.card():
                ui.label("2")

            with ui.card():
                ui.label("3")
        with ui.column().classes("flex-auto border"):
            ui.label("4")
            ui.label("5")
            ui.label("6")
        with ui.column().classes("flex-auto border"):
            ui.label("7")
            ui.label("8")
            ui.label("9")


ui.run()
