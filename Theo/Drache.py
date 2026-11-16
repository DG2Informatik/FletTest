import asyncio

import flet as ft

print("version 2 - Repariert für Flet 1.0.1+")

def main(page: ft.Page) -> None:
    # 1. Seiteneinstellungen vornehmen
    page.title = "Flet 1.0.1+ Imperativer Stil"
    page.padding = 20
    page.theme_mode = ft.ThemeMode.DARK

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
    explosion = ft.Text(
        "💥",
        size=64,
        visible=False,
        scale=ft.Scale(0.2),
        opacity=0,
        animate_scale=ft.Animation(250, ft.AnimationCurve.EASE_OUT),
        animate_opacity=ft.Animation(250, ft.AnimationCurve.EASE_OUT),
    )


    # 4. Die Logikfunktion für den Klick
    async def toggle_color(e: ft.ControlEvent) -> None:
        state["is_blue"] = not state["is_blue"]

        if state["is_blue"]:
            btn.bgcolor = ft.Colors.BLUE_50
            
            # API 1.0.1+ KORREKTUR: .text existiert nicht mehr!
            # Wir müssen das 'value'-Attribut des inneren 'content' (Text-Controls) ändern.
            btn.content = "Wechsel zu Grün"
            btn.bgcolor = ft.Colors.GREEN
            print(1)
        else:
            print(2)
            btn.bgcolor = ft.Colors.GREEN_50
            
            # API 1.0.1+ KORREKTUR: Auch hier den Text über .content.value ändern.
            btn.content = "Wechsel zu Blau"
            btn.bgcolor = ft.Colors.BLUE

        explosion.visible = True
        explosion.scale = ft.Scale(1)
        explosion.opacity = 1
        page.update()
        await asyncio.sleep(0.25)
        explosion.scale = ft.Scale(1.6)
        explosion.opacity = 0
        page.update()
        await asyncio.sleep(0.25)
        explosion.visible = False
        explosion.scale = ft.Scale(0.9)
        page.update()

        # HINWEIS: In Flet 1.0+ ist ein manuelles 'btn.update()' oder 'page.update()'
        # am Ende eines Event-Handlers nicht mehr notwendig. Flet aktualisiert die UI automatisch!

    background_is_black = False
    background_btn = ft.Button("Schwarz", bgcolor=ft.Colors.BLACK, color=ft.Colors.WHITE)

    def toggle_background(e: ft.ControlEvent) -> None:
        nonlocal background_is_black
        background_is_black = not background_is_black
        page.bgcolor = ft.Colors.BLACK if background_is_black else ft.Colors.WHITE
        background_btn.content = "Weiß" if background_is_black else "Schwarz"

    # 5. Event-Handler zuweisen & Layout ausrichten
    btn.on_click = toggle_color  # type: ignore[assignment]
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.Colors.WHITE

    # 6. Button zur Seite hinzufügen
    page.add(
        ft.Column(
            controls=[
                ft.Container(
                    content=ft.Stack(
                        controls=[
                            btn,
                            explosion,
                        ],
                        alignment=ft.Alignment.CENTER,
                        expand=True,
                    ),
                    alignment=ft.Alignment.CENTER,
                    expand=True,
                ),
                ft.Row(controls=[background_btn], alignment=ft.MainAxisAlignment.START),
            ],
            expand=True,
        )
    )
    background_btn.on_click = toggle_background  # type: ignore[assignment]


if __name__ == "__main__":
    # App-Start über die moderne ft.run Pipeline mittels Lambda
    ft.run(lambda page: main(page))
