import flet as ft


def main(page: ft.Page):
    """Minimal-App: Zähler mit Floating-Action-Button.

    `counter.data` ist der unsichtbare Zählerspeicher,
    `counter.value` die sichtbare Anzeige.
    Flet 1.0 aktualisiert die Oberfläche automatisch:
    kein page.update() nötig.
    """
    counter = ft.Text("0", size=50, data=0)

    def increment(e):
        counter.data += 1
        counter.value = str(counter.data)

    page.add(
        ft.Container(
            content=counter,
            alignment=ft.Alignment.CENTER,   # 1.0: Klasse, nicht ft.alignment.center
            expand=True,
        ),
        ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=increment),
    )


ft.run(main)