"""Flet-Startseite inspiriert von Hübner Bräu in Steinfeld."""

import flet as ft

BACKGROUND = "#F3F0EA"
PAPER = "#FFFCF6"
GREEN = "#28483B"
GREEN_LIGHT = "#3D6652"
BROWN = "#453E38"
MUTED = "#756C62"
GOLD = "#C49A55"
LINE = "#E2DBCF"
IMAGE_BASE = "https://huebner-braeu.de/wp-content/uploads/"
SHOP_URL = "https://huebner-braeu.de/online-shop/shop/"


def main(page: ft.Page) -> None:
    page.title = "Hübner Bräu | Steinfeld"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = BACKGROUND
    page.padding = 0

    async def scroll_to(section: str) -> None:
        await page.scroll_to(scroll_key=section, duration=350)

    def scroll_handler(section: str):
        async def on_click(_: ft.ControlEvent) -> None:
            await scroll_to(section)

        return on_click

    def nav_button(label: str, section: str) -> ft.TextButton:
        return ft.TextButton(
            label,
            style=ft.ButtonStyle(color=BROWN, padding=10),
            on_click=scroll_handler(section),
        )

    brand = ft.Row(
        controls=[
            ft.Container(
                content=ft.Text(
                    "H",
                    size=25,
                    weight=ft.FontWeight.BOLD,
                    color=GREEN,
                    text_align=ft.TextAlign.CENTER,
                ),
                width=46,
                height=46,
                alignment=ft.Alignment.CENTER,
                border=ft.Border.all(1, GOLD),
                border_radius=23,
            ),
            ft.Column(
                controls=[
                    ft.Text(
                        "HÜBNER BRÄU",
                        size=19,
                        weight=ft.FontWeight.BOLD,
                        color=GREEN,
                        font_family="Georgia",
                    ),
                    ft.Text(
                        "BRAUEREI · GASTSTÄTTE · BRENNEREI",
                        size=9,
                        color=MUTED,
                        weight=ft.FontWeight.BOLD,
                    ),
                ],
                spacing=2,
                tight=True,
            ),
        ],
        spacing=12,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    navigation = ft.ResponsiveRow(
        controls=[
            ft.Container(content=brand, col={"xs": 12, "md": 5}),
            ft.Container(
                content=ft.Row(
                    controls=[
                        nav_button("Brauerei", "brauerei"),
                        nav_button("Wirtshaus", "wirtshaus"),
                        nav_button("Steinfeld", "besuch"),
                        ft.Button(
                            "Online-Shop",
                            url=SHOP_URL,
                            bgcolor=GREEN,
                            color=ft.Colors.WHITE,
                            elevation=0,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=6),
                                padding=ft.Padding(18, 12, 18, 12),
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    wrap=True,
                    spacing=4,
                ),
                col={"xs": 12, "md": 7},
            ),
        ],
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        run_spacing=8,
    )

    hero_copy = ft.Column(
        controls=[
            ft.Text(
                "STEINFELD · FRÄNKISCHE SCHWEIZ",
                size=12,
                weight=ft.FontWeight.BOLD,
                color="#E4C88E",
            ),
            ft.Text(
                "Ein guter Platz\nfür fränkischen Genuss.",
                size=42,
                weight=ft.FontWeight.BOLD,
                color=PAPER,
                font_family="Georgia",
            ),
            ft.Text(
                "Brauerei, Wirtshaus und Biergarten in Steinfeld – "
                "die kleine Privatbrauerei ist auch als Ottobier bekannt.",
                size=16,
                color="#E6E0D6",
            ),
            ft.Row(
                controls=[
                    ft.Button(
                        "Unser Wirtshaus",
                        on_click=scroll_handler("wirtshaus"),
                        bgcolor=GOLD,
                        color=GREEN,
                        elevation=0,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=6),
                            padding=ft.Padding(20, 14, 20, 14),
                        ),
                    ),
                    ft.Button(
                        "Anfahrt",
                        url=(
                            "https://www.google.com/maps/search/"
                            "?api=1&query=H%C3%BCbner+Br%C3%A4u+Steinfeld"
                        ),
                        bgcolor=GREEN_LIGHT,
                        color=PAPER,
                        elevation=0,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=6),
                            padding=ft.Padding(20, 14, 20, 14),
                        ),
                    ),
                ],
                wrap=True,
                spacing=12,
            ),
        ],
        spacing=18,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    hero_art = ft.Container(
        content=ft.Image(
            src=f"{IMAGE_BASE}steinfelder_slider00.jpg",
            width=330,
            height=300,
            fit=ft.BoxFit.COVER,
            border_radius=12,
            semantics_label="Steinfelder Vollbier von Hübner Bräu",
        ),
        border_radius=16,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
    )

    hero = ft.Container(
        content=ft.ResponsiveRow(
            controls=[
                ft.Container(content=hero_copy, col={"xs": 12, "md": 7}),
                ft.Container(content=hero_art, col={"xs": 12, "md": 5}),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=28,
            run_spacing=28,
        ),
        bgcolor=GREEN,
        border_radius=18,
        padding=ft.Padding(36, 36, 36, 36),
    )

    def info_card(
        image: str, image_alt: str, eyebrow: str, title: str, description: str
    ) -> ft.Container:
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Image(
                        src=f"{IMAGE_BASE}{image}",
                        width=300,
                        height=155,
                        fit=ft.BoxFit.COVER,
                        border_radius=8,
                        semantics_label=image_alt,
                    ),
                    ft.Text(
                        eyebrow.upper(),
                        size=10,
                        weight=ft.FontWeight.BOLD,
                        color=MUTED,
                    ),
                    ft.Text(
                        title,
                        size=21,
                        weight=ft.FontWeight.BOLD,
                        color=GREEN,
                        font_family="Georgia",
                    ),
                    ft.Text(description, size=14, color=BROWN),
                ],
                spacing=12,
            ),
            bgcolor=PAPER,
            border=ft.Border.all(1, LINE),
            border_radius=12,
            padding=22,
        )

    intro = ft.Row(
        controls=[
            ft.Column(
                controls=[
                    ft.Text(
                        "GUT ZU WISSEN",
                        size=11,
                        weight=ft.FontWeight.BOLD,
                        color=GOLD,
                    ),
                    ft.Text(
                        "Drei gute Gründe\nfür eine Einkehr",
                        size=31,
                        weight=ft.FontWeight.BOLD,
                        color=GREEN,
                        font_family="Georgia",
                    ),
                ],
                spacing=8,
            ),
            ft.Container(
                content=ft.Text(
                    "Ein Stück fränkische Gastlichkeit am Tor zur Fränkischen Schweiz.",
                    size=15,
                    color=MUTED,
                ),
                width=330,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.END,
        wrap=True,
        spacing=20,
    )

    features = ft.ResponsiveRow(
        controls=[
            ft.Container(
                content=info_card(
                    "hb_bierflaschen_vollbier.jpg",
                    "Flaschen Steinfelder Vollbier",
                    "Aus der eigenen Brauerei",
                    "Steinfelder Bier",
                    "Im Sortiment finden sich unter anderem Steinfelder "
                    "Vollbier und Steinfelder Hell.",
                ),
                col={"xs": 12, "md": 4},
            ),
            ft.Container(
                content=info_card(
                    "FF0A9BF9-767E-4E69-8B2C-6CA46F086E81.jpg",
                    "Essen aus der Brauereigaststätte",
                    "Fränkisch & hausgemacht",
                    "Wirtshausküche",
                    "Hausgemachte Brotzeiten und Kuchen sowie warme "
                    "fränkische Gerichte.",
                ),
                col={"xs": 12, "md": 4},
            ),
            ft.Container(
                content=info_card(
                    "huebner_gasthaus_01_small.jpg",
                    "Hübner Bräu Gaststätte und Biergarten",
                    "Drinnen oder draußen",
                    "Biergarten",
                    "Im Sommer im Biergarten, bei kühlerem Wetter in der "
                    "warmen Gaststube.",
                ),
                col={"xs": 12, "md": 4},
            ),
        ],
        spacing=16,
        run_spacing=16,
    )

    food_section = ft.Container(
        key="essen",
        content=ft.ResponsiveRow(
            controls=[
                ft.Container(
                    content=ft.Image(
                        src=f"{IMAGE_BASE}IMG_3488-scaled.jpg",
                        width=320,
                        height=230,
                        fit=ft.BoxFit.COVER,
                        border_radius=10,
                        semantics_label="Hausgemachtes aus der Hübner-Bräu Küche",
                    ),
                    col={"xs": 12, "md": 5},
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "AUS DER WIRTSHAUSKÜCHE",
                                size=11,
                                weight=ft.FontWeight.BOLD,
                                color=GOLD,
                            ),
                            ft.Text(
                                "Eine Brotzeit geht immer.",
                                size=28,
                                weight=ft.FontWeight.BOLD,
                                color=GREEN,
                                font_family="Georgia",
                            ),
                            ft.Text(
                                "Freu dich auf hausgemachte Brotzeiten, "
                                "warme Gerichte und Kuchen. Freitags gibt es "
                                "hausgemachte Pizza (April bis Dezember).",
                                size=15,
                                color=BROWN,
                            ),
                        ],
                        spacing=12,
                    ),
                    col={"xs": 12, "md": 7},
                ),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=24,
            run_spacing=18,
        ),
        bgcolor=PAPER,
        border=ft.Border.all(1, LINE),
        border_radius=14,
        padding=24,
    )

    def product_card(
        image: str,
        image_alt: str,
        title: str,
        price: str,
        product_url: str,
    ) -> ft.Container:
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Image(
                        src=f"{IMAGE_BASE}{image}",
                        width=230,
                        height=170,
                        fit=ft.BoxFit.COVER,
                        border_radius=8,
                        semantics_label=image_alt,
                    ),
                    ft.Text(
                        title,
                        size=19,
                        weight=ft.FontWeight.BOLD,
                        color=GREEN,
                        font_family="Georgia",
                    ),
                    ft.Text(price, size=14, color=MUTED),
                    ft.Button(
                        "Zum Produkt",
                        url=product_url,
                        bgcolor=GREEN,
                        color=PAPER,
                        elevation=0,
                    ),
                ],
                spacing=10,
            ),
            bgcolor=PAPER,
            border=ft.Border.all(1, LINE),
            border_radius=12,
            padding=18,
        )

    shop_section = ft.Container(
        key="sortiment",
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text(
                                    "BRAUEREI & BRENNEREI",
                                    size=11,
                                    weight=ft.FontWeight.BOLD,
                                    color=GOLD,
                                ),
                                ft.Text(
                                    "Aus dem Steinfelder Sortiment",
                                    size=29,
                                    weight=ft.FontWeight.BOLD,
                                    color=GREEN,
                                    font_family="Georgia",
                                ),
                            ],
                            spacing=8,
                        ),
                        ft.Button(
                            "Zum Online-Shop",
                            url=SHOP_URL,
                            bgcolor=GREEN,
                            color=PAPER,
                            elevation=0,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.END,
                    wrap=True,
                    spacing=16,
                ),
                ft.ResponsiveRow(
                    controls=[
                        ft.Container(
                            content=product_card(
                                "hb_bierflaschen_hell.jpg",
                                "Flaschen Steinfelder Hell",
                                "Steinfelder Hell",
                                "2,00 € · 4,00 €/l",
                                "https://huebner-braeu.de/produkt/steinfelder-hell/",
                            ),
                            col={"xs": 12, "md": 4},
                        ),
                        ft.Container(
                            content=product_card(
                                "hb_bierflaschen_vollbier.jpg",
                                "Flaschen Steinfelder Vollbier",
                                "Steinfelder Vollbier",
                                "2,00 € · 4,00 €/l",
                                "https://huebner-braeu.de/produkt/steinfelder-vollbier/",
                            ),
                            col={"xs": 12, "md": 4},
                        ),
                        ft.Container(
                            content=product_card(
                                "hb_braende_bier.jpg",
                                "Bierschnaps aus der Hübner-Bräu Brennerei",
                                "Bierschnaps",
                                "12,50–18,50 €",
                                "https://huebner-braeu.de/produkt/bierschnaps/",
                            ),
                            col={"xs": 12, "md": 4},
                        ),
                    ],
                    spacing=16,
                    run_spacing=16,
                ),
                ft.Text(
                    "Preise und Verfügbarkeit laut Online-Shop; sie können sich ändern.",
                    size=12,
                    color=MUTED,
                ),
            ],
            spacing=18,
        ),
    )

    visit_section = ft.Container(
        key="besuch",
        content=ft.ResponsiveRow(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "RAUS INS GRÜNE",
                                size=11,
                                weight=ft.FontWeight.BOLD,
                                color="#E4C88E",
                            ),
                            ft.Text(
                                "Steinfeld entdecken",
                                size=29,
                                weight=ft.FontWeight.BOLD,
                                color=PAPER,
                                font_family="Georgia",
                            ),
                            ft.Text(
                                "Wander- und Radtouren, Kletterfelsen und "
                                "das nahe Paradiestal machen Steinfeld zu "
                                "einem schönen Ausgangs- oder Rastpunkt. "
                                "Die Gaststätte liegt an der B22 Richtung Hollfeld.",
                                size=15,
                                color="#E6E0D6",
                            ),
                        ],
                        spacing=12,
                    ),
                    col={"xs": 12, "md": 8},
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Icon(
                                ft.Icons.PEDAL_BIKE,
                                size=34,
                                color=GOLD,
                            ),
                            ft.Text(
                                "Pause gefällig?",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=PAPER,
                                font_family="Georgia",
                            ),
                            ft.Button(
                                "Route planen",
                                url=(
                                    "https://www.google.com/maps/search/"
                                    "?api=1&query=H%C3%BCbner+Br%C3%A4u+Steinfeld"
                                ),
                                bgcolor=GOLD,
                                color=GREEN,
                                elevation=0,
                            ),
                        ],
                        spacing=12,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
                    col={"xs": 12, "md": 4},
                ),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=24,
            run_spacing=20,
        ),
        bgcolor="#354F42",
        border_radius=14,
        padding=28,
    )

    wirtshaus_section = ft.Container(
        key="wirtshaus",
        content=ft.ResponsiveRow(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "WIRTSHAUS & BIERGARTEN",
                                size=11,
                                weight=ft.FontWeight.BOLD,
                                color=GOLD,
                            ),
                            ft.Text(
                                "Schau vorbei.",
                                size=30,
                                weight=ft.FontWeight.BOLD,
                                color=GREEN,
                                font_family="Georgia",
                            ),
                            ft.Text(
                                "Die Brauerei-Gaststätte verbindet fränkische "
                                "Küche mit einer gemütlichen Gaststube und "
                                "einem Biergarten. Im Sommer sitzt man draußen, "
                                "in der kühleren Jahreszeit drinnen.",
                                size=15,
                                color=BROWN,
                            ),
                        ],
                        spacing=12,
                    ),
                    col={"xs": 12, "md": 8},
                ),
                ft.Container(
                    content=ft.Button(
                        "Küche entdecken",
                        on_click=scroll_handler("essen"),
                        bgcolor=GREEN,
                        color=PAPER,
                        elevation=0,
                    ),
                    alignment=ft.Alignment.CENTER_RIGHT,
                    col={"xs": 12, "md": 4},
                ),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=24,
            run_spacing=16,
        ),
        bgcolor="#E9E0D1",
        border_radius=14,
        padding=28,
    )

    owner_section = ft.Container(
        content=ft.ResponsiveRow(
            controls=[
                ft.Container(
                    content=ft.Image(
                        src=f"{IMAGE_BASE}thomas_huebner_01.jpg",
                        width=220,
                        height=220,
                        fit=ft.BoxFit.COVER,
                        border_radius=110,
                        semantics_label="Thomas Will, Inhaber und Brauer",
                    ),
                    alignment=ft.Alignment.CENTER,
                    col={"xs": 12, "md": 4},
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "INHABER & BRAUER",
                                size=11,
                                weight=ft.FontWeight.BOLD,
                                color=GOLD,
                            ),
                            ft.Text(
                                "Thomas Will",
                                size=30,
                                weight=ft.FontWeight.BOLD,
                                color=GREEN,
                                font_family="Georgia",
                            ),
                            ft.Text(
                                "Hübner Bräu ist eine kleine Privatbrauerei "
                                "in Steinfeld – mit eigener Gaststätte und "
                                "Brennerei.",
                                size=15,
                                color=BROWN,
                            ),
                        ],
                        spacing=12,
                    ),
                    col={"xs": 12, "md": 8},
                ),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            run_spacing=18,
        ),
        bgcolor="#E9E0D1",
        border_radius=14,
        padding=24,
    )

    footer = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text(
                    "HÜBNER BRÄU",
                    size=15,
                    weight=ft.FontWeight.BOLD,
                    color=PAPER,
                    font_family="Georgia",
                ),
                ft.Text(
                    "Brauerei · Gaststätte · Brennerei in Steinfeld",
                    size=12,
                    color="#E6E0D6",
                ),
                ft.Text(
                    "Fotos und Sortiment: huebner-braeu.de",
                    size=11,
                    color="#E4C88E",
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            wrap=True,
            spacing=12,
        ),
        bgcolor=GREEN,
        padding=ft.Padding(28, 20, 28, 20),
    )

    page.add(
        ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text(
                        "STEINFELD AN DER WIESENT  ·  FRÄNKISCHE SCHWEIZ",
                        size=10,
                        weight=ft.FontWeight.BOLD,
                        color=PAPER,
                    ),
                    bgcolor="#1E382D",
                    padding=ft.Padding(24, 8, 24, 8),
                    alignment=ft.Alignment.CENTER,
                ),
                ft.Container(
                    content=navigation,
                    bgcolor=BACKGROUND,
                    padding=ft.Padding(28, 18, 28, 18),
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(key="brauerei", content=hero),
                            intro,
                            features,
                            food_section,
                            shop_section,
                            visit_section,
                            wirtshaus_section,
                            owner_section,
                        ],
                        spacing=34,
                    ),
                    padding=ft.Padding(28, 28, 28, 44),
                    expand=True,
                ),
                footer,
            ],
            spacing=0,
            expand=True,
            scroll=ft.ScrollMode.AUTO,
        )
    )


if __name__ == "__main__":
    ft.run(main)
