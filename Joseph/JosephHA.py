from typing import Any

import flet as ft


@ft.component
def ColorSwitcher() -> ft.Container:
    is_white: bool
    set_is_white: Any
    is_white, set_is_white = ft.use_state(False)

    btn_text: str = "Wechsel zu Weiß" if not is_white else "Wechsel zu Rot"
    bg_color: str = ft.Colors.RED_900 if not is_white else ft.Colors.WHITE
    title_color: str = ft.Colors.WHITE if not is_white else ft.Colors.BLACK

    def toggle_color(e: ft.ControlEvent) -> None:
        set_is_white(not is_white)

    return ft.Container(
        content=ft.Stack(
            controls=[
                ft.Text(
                    "FC Bayern München",
                    size=48,
                    weight=ft.FontWeight.BOLD,
                    color=title_color,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(
                    content=ft.Button(
                        btn_text,
                        bgcolor=ft.Colors.RED,
                        color=ft.Colors.WHITE,
                        on_click=toggle_color,
                    ),
                    alignment=ft.Alignment.BOTTOM_CENTER,
                    padding=20,
                    expand=True,
                ),
            ],
            alignment=ft.Alignment.CENTER,
            expand=True,
        ),
        bgcolor=bg_color,
        padding=20,
        alignment=ft.Alignment.CENTER,
        expand=True,  
    )

def main(page: ft.Page) -> None:
    page.title = "Flet 1.0.1 Modern & Typisiert"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.render(ColorSwitcher)

if __name__ == "__main__":
    ft.run(lambda page: main(page))
