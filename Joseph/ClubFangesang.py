from typing import Any

import flet as ft


@ft.component
def ClubFangesang() -> ft.Container:
    page_index: int
    set_page_index: Any
    page_index, set_page_index = ft.use_state(0)

    def show_next(e: ft.ControlEvent) -> None:
        set_page_index((page_index + 1) % 3)

    texts = (
        "Auswärts nur dabei",
        "Im Schutz der Polizei",
        "Scheiße Kleeblatt Fürth",
    )
    backgrounds = (ft.Colors.RED_900, ft.Colors.WHITE, ft.Colors.BLACK)
    text_colors = (ft.Colors.WHITE, ft.Colors.BLACK, ft.Colors.WHITE)
    button_color = ft.Colors.RED_900 if page_index == 2 else ft.Colors.BLACK

    content = ft.Stack(
        controls=[
            ft.Container(
                content=ft.Text(
                    texts[page_index],
                    size=56,
                    weight=ft.FontWeight.BOLD,
                    color=text_colors[page_index],
                    text_align=ft.TextAlign.CENTER,
                ),
                alignment=ft.Alignment.CENTER,
                expand=True,
            ),
            ft.Container(
                content=ft.Button(
                    "Club",
                    bgcolor=button_color,
                    color=ft.Colors.WHITE,
                    on_click=show_next,
                ),
                alignment=ft.Alignment.BOTTOM_CENTER,
                padding=20,
                expand=True,
            ),
        ],
        expand=True,
    )

    return ft.Container(
        content=content,
        bgcolor=backgrounds[page_index],
        expand=True,
        padding=20,
        alignment=ft.Alignment.CENTER,
    )


def main(page: ft.Page) -> None:
    page.title = "1. FC Nürnberg"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.render(ClubFangesang)


if __name__ == "__main__":
    ft.run(main)
