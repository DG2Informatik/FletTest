"""Ein einfacher, vom Apple-Taschenrechner inspirierter Rechner mit Flet."""

import math
from typing import ClassVar

import flet as ft


class Calculator:
    """Verwaltet die Eingabe und die Grundrechenarten des Rechners."""

    OPERATORS: ClassVar[set[str]] = {"+", "−", "×", "÷"}
    ERROR = "Fehler"

    def __init__(self) -> None:
        self.display = "0"
        self.operator: str | None = None
        self.first_operand: float | None = None
        self.waiting_for_operand = False
        self.last_operator: str | None = None
        self.last_operand: float | None = None

    def press(self, key: str) -> None:
        if key == "AC":
            self.__init__()
            return

        if self.display == self.ERROR:
            self.__init__()

        if key.isdigit() or key == ".":
            self._enter_digit(key)
        elif key == "+/−":
            self.display = self._format_number(-float(self.display))
        elif key == "%":
            if self.waiting_for_operand:
                return
            value = float(self.display)
            if self.operator in {"+", "−"} and self.first_operand is not None:
                value = self.first_operand * value / 100
            else:
                value /= 100
            self.display = self._format_number(value)
        elif key in self.OPERATORS:
            self._choose_operator(key)
        elif key == "=":
            self._calculate_result()

    def _enter_digit(self, key: str) -> None:
        if self.waiting_for_operand:
            self.display = "0" if key == "." else key
            if key == ".":
                self.display = "0."
            self.waiting_for_operand = False
            return

        if key == ".":
            if "." not in self.display:
                self.display += "."
        elif self.display == "0":
            self.display = key
        elif len(self.display) < 12:
            self.display += key

    def _choose_operator(self, operator: str) -> None:
        current = float(self.display)
        if self.operator is not None and self.first_operand is not None:
            if not self.waiting_for_operand:
                result = self._calculate(self.first_operand, current, self.operator)
                if result is None:
                    self._show_error()
                    return
                self.display = self._format_number(result)
            self.first_operand = float(self.display)
        else:
            self.first_operand = current

        self.operator = operator
        self.waiting_for_operand = True
        self.last_operator = None
        self.last_operand = None

    def _calculate_result(self) -> None:
        if self.operator is not None and self.first_operand is not None:
            operand = (
                self.first_operand if self.waiting_for_operand else float(self.display)
            )
            result = self._calculate(self.first_operand, operand, self.operator)
            if result is None:
                self._show_error()
                return

            self.display = self._format_number(result)
            self.last_operator = self.operator
            self.last_operand = operand
            self.operator = None
            self.first_operand = None
            self.waiting_for_operand = True
        elif self.last_operator is not None and self.last_operand is not None:
            result = self._calculate(
                float(self.display), self.last_operand, self.last_operator
            )
            if result is None:
                self._show_error()
                return
            self.display = self._format_number(result)
            self.waiting_for_operand = True

    @staticmethod
    def _calculate(left: float, right: float, operator: str) -> float | None:
        if operator == "+":
            result = left + right
        elif operator == "−":
            result = left - right
        elif operator == "×":
            result = left * right
        else:
            if right == 0:
                return None
            result = left / right
        return result if math.isfinite(result) else None

    def _show_error(self) -> None:
        self.display = self.ERROR
        self.operator = None
        self.first_operand = None
        self.last_operator = None
        self.last_operand = None
        self.waiting_for_operand = True

    @staticmethod
    def _format_number(value: float) -> str:
        if value == 0:
            return "0"
        return f"{value:.10g}"


def main(page: ft.Page) -> None:
    page.title = "Taschenrechner"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#000000"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    calculator = Calculator()
    display = ft.Text(
        calculator.display,
        size=64,
        color=ft.Colors.WHITE,
        text_align=ft.TextAlign.RIGHT,
        no_wrap=True,
        overflow=ft.TextOverflow.CLIP,
        width=334,
    )

    def make_button(label: str, *, wide: bool = False) -> ft.Button:
        if label in {"AC", "+/−", "%"}:
            background, foreground = "#A5A5A5", "#000000"
        elif label in Calculator.OPERATORS or label == "=":
            background, foreground = "#FF9F0A", "#FFFFFF"
        else:
            background, foreground = "#333333", "#FFFFFF"

        def on_click(_: ft.ControlEvent) -> None:
            calculator.press(label)
            display.value = calculator.display

        return ft.Button(
            label,
            width=162 if wide else 76,
            height=76,
            bgcolor=background,
            color=foreground,
            elevation=0,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=100),
                padding=0,
            ),
            on_click=on_click,
        )

    rows = [
        ["AC", "+/−", "%", "÷"],
        ["7", "8", "9", "×"],
        ["4", "5", "6", "−"],
        ["1", "2", "3", "+"],
    ]
    buttons = [
        ft.Row(
            controls=[make_button(label) for label in row],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,
        )
        for row in rows
    ]
    buttons.append(
        ft.Row(
            controls=[
                make_button("0", wide=True),
                make_button("."),
                make_button("="),
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    page.add(
        ft.Column(
            controls=[
                ft.Container(
                    content=display,
                    width=334,
                    height=112,
                    alignment=ft.Alignment(1, 1),
                    padding=ft.Padding(0, 0, 4, 8),
                ),
                *buttons,
            ],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


if __name__ == "__main__":
    ft.run(main)
7u