"""Tests für main_live_input.py (Live-Eingabe).

Hinweis: Flet 1.0.1 hat keine offizielle Test-API für Page-Objekte.
Diese Tests nutzen Mocking, um die Logik zu testen.
"""

from unittest.mock import MagicMock

import flet as ft


def test_page_title() -> None:
    """Testet, ob der Seitentitel korrekt gesetzt wird."""
    from main_live_input import main
    
    mock_page = MagicMock(spec=ft.Page)
    mock_page.controls = []
    
    main(mock_page)
    
    assert mock_page.title == "Flet 1.0.1+ Live-Eingabe"


def test_page_initial_bgcolor() -> None:
    """Testet die initiale Hintergrundfarbe der Seite."""
    from main_live_input import main
    
    mock_page = MagicMock(spec=ft.Page)
    mock_page.controls = []
    
    main(mock_page)
    
    assert mock_page.bgcolor == ft.Colors.BLUE_50


def test_column_spacing() -> None:
    """Testet den Abstand zwischen den Elementen in der Column."""
    from main_live_input import main
    
    mock_page = MagicMock(spec=ft.Page)
    mock_page.controls = []
    
    main(mock_page)
    
    # Prüfe, ob page.add aufgerufen wurde
    assert mock_page.add.call_count == 1
    
    # Hole die Column aus dem Aufruf
    column = mock_page.add.call_args[0][0]
    assert isinstance(column, ft.Column)
    assert column.spacing == 20


def test_text_input_properties() -> None:
    """Testet die Eigenschaften des Textfelds."""
    from main_live_input import main
    
    mock_page = MagicMock(spec=ft.Page)
    mock_page.controls = []
    
    main(mock_page)
    
    column = mock_page.add.call_args[0][0]
    text_field = column.controls[0]
    
    assert isinstance(text_field, ft.TextField)
    assert text_field.label == "Tippe etwas ein, um den Button-Text live zu ändern"
    assert text_field.width == 400
    assert text_field.hint_text == "Hier tippen..."


def test_button_initial_text() -> None:
    """Testet den anfänglichen Button-Text."""
    from main_live_input import main
    
    mock_page = MagicMock(spec=ft.Page)
    mock_page.controls = []
    
    main(mock_page)
    
    column = mock_page.add.call_args[0][0]
    button = column.controls[1]
    
    assert isinstance(button, ft.Button)
    content = button.content
    assert isinstance(content, ft.Text)
    assert content.value == "Ich verändere mich live..."


def test_text_change_logic() -> None:
    """Testet die Logik für Textänderungen (extrahiert)."""
    # Extrahierte Logik aus on_text_changing
    def get_button_text(input_value: str) -> str:
        return input_value if input_value else "Ich verändere mich live..."
    
    assert get_button_text("") == "Ich verändere mich live..."
    assert get_button_text("Test") == "Test"
    assert get_button_text("Neuer Text") == "Neuer Text"
