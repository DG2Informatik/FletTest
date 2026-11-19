import asyncio
from unittest.mock import MagicMock

import flet as ft

from Linus.LinusHB import SHOP_URL, main


def test_header_buttons_scroll_to_sections_and_open_online_shop() -> None:
    page = MagicMock(spec=ft.Page)

    main(page)

    root = page.add.call_args.args[0]
    header = root.controls[1].content
    nav_buttons = header.controls[1].content.controls

    for button, section in zip(
        nav_buttons[:3],
        ("brauerei", "wirtshaus", "besuch"),
        strict=True,
    ):
        asyncio.run(button.on_click(None))
        assert page.scroll_to.await_args.kwargs == {
            "scroll_key": section,
            "duration": 350,
        }

    shop_button = nav_buttons[3]
    assert shop_button.content == "Online-Shop"
    assert shop_button.url == SHOP_URL
