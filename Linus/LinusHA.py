import flet as ft


@ft.component
def DayNightScene() -> ft.Container:
    is_night, set_is_night = ft.use_state(False)

    sky_color = "#101B3B" if is_night else "#87CEEB"
    meadow_color = "#24502D" if is_night else "#4CAF50"
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
                    content=ft.Stack(
                        expand=True,
                        controls=[
                            ft.Container(
                                align=ft.Alignment(
                                    -0.45, 3.0 if is_night else -0.35
                                ),
                                animate_align=ft.Animation(
                                    2000, ft.AnimationCurve.EASE_IN_OUT
                                ),
                                content=ft.Icon(
                                    ft.Icons.WB_SUNNY_ROUNDED,
                                    size=120,
                                    color="#FFD54F",
                                ),
                            ),
                            ft.Container(
                                align=ft.Alignment(
                                    0.45, -0.35 if is_night else 3.0
                                ),
                                animate_align=ft.Animation(
                                    2000, ft.AnimationCurve.EASE_IN_OUT
                                ),
                                content=ft.Icon(
                                    ft.Icons.NIGHTLIGHT_ROUNDED,
                                    size=100,
                                    color="#F5F3CE",
                                ),
                            ),
                            *[
                                ft.Container(
                                    align=ft.Alignment(x, y),
                                    visible=is_night,
                                    content=ft.Icon(
                                        ft.Icons.STAR_ROUNDED,
                                        size=size,
                                        color="#FFF4B8",
                                    ),
                                )
                                for x, y, size in [
                                    (-0.82, -0.75, 18),
                                    (-0.52, -0.38, 13),
                                    (-0.24, -0.82, 16),
                                    (0.08, -0.52, 12),
                                    (0.38, -0.78, 20),
                                    (0.68, -0.42, 14),
                                    (0.84, 0.08, 12),
                                    (-0.72, 0.22, 14),
                                    (0.18, 0.18, 11),
                                ]
                            ],
                        ],
                    ),
                ),
                ft.Container(
                    expand=2,
                    bgcolor=meadow_color,
                    content=ft.Stack(
                        expand=True,
                        controls=[
                            *[
                                ft.Container(
                                    align=ft.Alignment(x, y),
                                    content=ft.Icon(
                                        ft.Icons.GRASS_ROUNDED,
                                        size=size,
                                        color=color,
                                    ),
                                )
                                for x, y, size, color in [
                                    (-0.88, -0.62, 34, "#81C784"),
                                    (-0.67, 0.18, 26, "#A5D6A7"),
                                    (-0.46, -0.28, 38, "#66BB6A"),
                                    (-0.22, 0.62, 30, "#81C784"),
                                    (0.02, -0.72, 28, "#A5D6A7"),
                                    (0.24, 0.12, 40, "#66BB6A"),
                                    (0.48, -0.42, 32, "#81C784"),
                                    (0.72, 0.58, 36, "#A5D6A7"),
                                    (0.91, -0.12, 27, "#66BB6A"),
                                ]
                            ],
                            ft.Container(
                                align=ft.Alignment.CENTER,
                                content=ft.Icon(
                                    ft.Icons.GRASS_ROUNDED,
                                    size=56,
                                    color="#C5E1A5",
                                ),
                            ),
                        ],
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
