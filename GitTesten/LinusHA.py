import flet as ft


@ft.component
def DayNightScene() -> ft.Container:
    is_night, set_is_night = ft.use_state(False)

    sky_color = "#101B3B" if is_night else "#87CEEB"
    meadow_color = "#24502D" if is_night else "#4CAF50"
    sky_icon = ft.Icons.NIGHTLIGHT_ROUNDED if is_night else ft.Icons.WB_SUNNY_ROUNDED
    sky_icon_color = "#F5F3CE" if is_night else "#FFD54F"
    button_text = "Tag einschalten" if is_night else "Nacht einschalten"
    button_icon = ft.Icons.WB_SUNNY_ROUNDED if is_night else ft.Icons.NIGHTLIGHT_ROUNDED

    def toggle_day_night(e: ft.ControlEvent) -> None:
        set_is_night(not is_night)

    return ft.Container(
        expand=True,
        content=ft.Column(
            spacing=0,
            expand=True,
            controls=[
                ft.Container(
                    expand=3,
                    bgcolor=sky_color,
                    alignment=ft.Alignment.CENTER,
                    content=ft.Icon(
                        sky_icon,
                        size=120,
                        color=sky_icon_color,
                    ),
                ),
                ft.Container(
                    expand=2,
                    bgcolor=meadow_color,
                    alignment=ft.Alignment.CENTER,
                    content=ft.Icon(
                        ft.Icons.GRASS_ROUNDED,
                        size=56,
                        color="#C5E1A5",
                    ),
                ),
                ft.Container(
                    height=100,
                    alignment=ft.Alignment.CENTER,
                    content=ft.Button(
                        button_text,
                        icon=button_icon,
                        on_click=toggle_day_night,
                    ),
                ),
            ],
        ),
    )


def main(page: ft.Page) -> None:
    page.title = "Tag und Nacht"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.render(DayNightScene)


if __name__ == "__main__":
    ft.run(main)
