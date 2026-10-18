import flet as ft

print("version 2 - Repariert für Flet 1.0.1+")

def main(page: ft.Page) -> None:
    # 1. Seiteneinstellungen vornehmen
    page.title = "Flet 1.0.1+ Imperativer Stil"
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT

    # 2. Anfangszustand (State) definieren
    state: dict[str, bool] = {"is_blue": False}

    # 3. Button erstellen
    # HINWEIS: Flet verpackt den übergebenen String intern automatisch in ein
    # ft.Text-Control und legt es im Attribut `btn.content` ab.
    btn: ft.Button = ft.Button(
        "Wechsel zu Blau",
        bgcolor=ft.Colors.BLUE,
        color=ft.Colors.WHITE,
    )

    # 4. Die Logikfunktion für den Klick
    def toggle_color(e: ft.ControlEvent) -> None:
        state["is_blue"] = not state["is_blue"]

        if state["is_blue"]:
            page.bgcolor = ft.Colors.BLUE_50
            
            # API 1.0.1+ KORREKTUR: .text existiert nicht mehr!
            # Wir müssen das 'value'-Attribut des inneren 'content' (Text-Controls) ändern.
            btn.content = "Wechsel zu Grün"
            btn.bgcolor = ft.Colors.GREEN
            print(1)
        else:
            print(2)
            page.bgcolor = ft.Colors.GREEN_50
            
            # API 1.0.1+ KORREKTUR: Auch hier den Text über .content.value ändern.
            btn.content = "Wechsel zu Blau"
            btn.bgcolor = ft.Colors.BLUE
        
        # HINWEIS: In Flet 1.0+ ist ein manuelles 'btn.update()' oder 'page.update()'
        # am Ende eines Event-Handlers nicht mehr notwendig. Flet aktualisiert die UI automatisch!

    # 5. Event-Handler zuweisen & Layout ausrichten
    btn.on_click = toggle_color  # type: ignore[assignment]
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.Colors.GREEN_50

    # 6. Button zur Seite hinzufügen
    page.add(btn)


if __name__ == "__main__":
    # App-Start über die moderne ft.run Pipeline mittels Lambda
    ft.run(lambda page: main(page))
