from __future__ import annotations

from dataclasses import dataclass, field

import flet as ft

BG = "#F7F8FC"
CARD = "#FFFFFF"
INK = "#18202F"
MUTED = "#7D8492"
PURPLE = "#6C63FF"
PURPLE_LIGHT = "#EEEDFF"
GREEN = "#25B887"
RED = "#E85D75"


@dataclass
class Subject:
    name: str
    weight: float = 1.0
    grades: list[float] = field(default_factory=list)

    @property
    def average(self) -> float | None:
        return sum(self.grades) / len(self.grades) if self.grades else None


def main(page: ft.Page) -> None:
    page.title = "Notan – Schulnoten"
    page.bgcolor = BG
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO

    subjects: list[Subject] = [
        Subject("Mathematik", 1.5, [2.0, 1.0]),
        Subject("Deutsch", 1.0, [1.7]),
        Subject("Englisch", 1.0, [2.3, 1.7]),
    ]

    average_text = ft.Text("–", size=42, weight=ft.FontWeight.W_700, color=INK)
    summary_text = ft.Text("", size=13, color=MUTED)
    subject_list = ft.Column(spacing=12)

    def format_grade(value: float) -> str:
        return f"{value:.1f}".replace(".", ",")

    def weighted_average() -> float | None:
        values = [(subject.average, subject.weight) for subject in subjects]
        values = [(average, weight) for average, weight in values if average is not None]
        if not values:
            return None
        return sum(average * weight for average, weight in values) / sum(
            weight for _, weight in values
        )

    def refresh() -> None:
        result = weighted_average()
        average_text.value = format_grade(result) if result is not None else "–"
        summary_text.value = (
            f"{len(subjects)} Fächer · {sum(len(s.grades) for s in subjects)} Noten"
            if subjects
            else "Noch keine Fächer angelegt"
        )
        subject_list.controls = [subject_card(subject) for subject in subjects]
        page.update()

    def show_message(message: str, color: str = RED) -> None:
        page.snack_bar = ft.SnackBar(ft.Text(message), bgcolor=color)
        page.snack_bar.open = True
        page.update()

    def add_grade(subject: Subject, field: ft.TextField, _: ft.ControlEvent) -> None:
        raw = (field.value or "").strip().replace(",", ".")
        try:
            grade = float(raw)
        except ValueError:
            show_message("Bitte eine gültige Note zwischen 1,0 und 6,0 eingeben.")
            return
        if not 1 <= grade <= 6:
            show_message("Noten müssen zwischen 1,0 und 6,0 liegen.")
            return
        subject.grades.append(grade)
        field.value = ""
        refresh()

    def remove_grade(subject: Subject, index: int, _: ft.ControlEvent) -> None:
        subject.grades.pop(index)
        refresh()

    def update_weight(subject: Subject, field: ft.TextField, _: ft.ControlEvent) -> None:
        raw = (field.value or "").strip().replace(",", ".")
        try:
            weight = float(raw)
        except ValueError:
            show_message("Die Gewichtung muss eine positive Zahl sein.")
            return
        if weight <= 0:
            show_message("Die Gewichtung muss größer als 0 sein.")
            return
        subject.weight = weight
        refresh()

    def delete_subject(subject: Subject, _: ft.ControlEvent) -> None:
        subjects.remove(subject)
        refresh()

    def subject_card(subject: Subject) -> ft.Control:
        grade_field = ft.TextField(
            hint_text="Note",
            width=112,
            height=44,
            text_size=14,
            border_radius=12,
            border_color="#E2E5EC",
            focused_border_color=PURPLE,
            keyboard_type=ft.KeyboardType.NUMBER,
            on_submit=lambda event: add_grade(subject, grade_field, event),
        )
        weight_field = ft.TextField(
            value=format_grade(subject.weight),
            width=84,
            height=40,
            text_size=13,
            text_align=ft.TextAlign.CENTER,
            border_radius=10,
            border_color="#E2E5EC",
            on_submit=lambda event: update_weight(subject, weight_field, event),
        )
        grade_chips = ft.Row(
            controls=[
                ft.Container(
                    content=ft.Row(
                        [
                            ft.Text(format_grade(grade), size=13, color=INK),
                            ft.IconButton(
                                icon=ft.Icons.CLOSE,
                                icon_size=13,
                                icon_color=MUTED,
                                tooltip="Note löschen",
                                on_click=lambda event, index=index: remove_grade(
                                    subject, index, event
                                ),
                            ),
                        ],
                        spacing=1,
                    ),
                    bgcolor="#F2F3F7",
                    border_radius=10,
                    padding=ft.Padding.symmetric(horizontal=8, vertical=2),
                )
                for index, grade in enumerate(subject.grades)
            ],
            spacing=6,
            wrap=True,
        )
        average = subject.average
        return ft.Container(
            bgcolor=CARD,
            border_radius=20,
            padding=20,
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=18,
                color="#1018280D",
                offset=ft.Offset(0, 5),
            ),
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Text(subject.name, size=18, weight=ft.FontWeight.W_600, color=INK),
                                    ft.Text(
                                        f"{len(subject.grades)} "
                                        f"{'Note' if len(subject.grades) == 1 else 'Noten'}",
                                        size=12,
                                        color=MUTED,
                                    ),
                                ],
                                spacing=3,
                                expand=True,
                            ),
                            ft.Column(
                                [
                                    ft.Text(
                                        format_grade(average) if average is not None else "–",
                                        size=24,
                                        weight=ft.FontWeight.W_700,
                                        color=PURPLE if average is not None else MUTED,
                                    ),
                                    ft.Text("Schnitt", size=11, color=MUTED),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.END,
                                spacing=0,
                            ),
                            ft.IconButton(
                                icon=ft.Icons.DELETE_OUTLINE,
                                icon_color=MUTED,
                                tooltip="Fach löschen",
                                on_click=lambda event: delete_subject(subject, event),
                            ),
                        ],
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Divider(height=18, color="#EEF0F4"),
                    ft.Row(
                        [
                            grade_field,
                            ft.Button(
                                "Note hinzufügen",
                                icon=ft.Icons.ADD,
                                bgcolor=PURPLE_LIGHT,
                                color=PURPLE,
                                height=42,
                                on_click=lambda event: add_grade(subject, grade_field, event),
                            ),
                            ft.Container(expand=True),
                            ft.Text("Gewichtung", size=12, color=MUTED),
                            weight_field,
                            ft.Text("×", size=14, color=MUTED),
                        ],
                        spacing=8,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        wrap=True,
                    ),
                    ft.Container(height=8),
                    grade_chips if subject.grades else ft.Text("Noch keine Noten eingetragen", size=12, color=MUTED),
                ],
                spacing=0,
            ),
        )

    def open_subject_dialog(_: ft.ControlEvent) -> None:
        name_field = ft.TextField(
            label="Fachname",
            hint_text="z. B. Biologie",
            autofocus=True,
            border_radius=12,
            border_color="#E2E5EC",
            focused_border_color=PURPLE,
        )

        def create_subject(_: ft.ControlEvent) -> None:
            name = (name_field.value or "").strip()
            if not name:
                show_message("Bitte gib einen Fachnamen ein.")
                return
            if any(subject.name.casefold() == name.casefold() for subject in subjects):
                show_message("Dieses Fach gibt es bereits.")
                return
            subjects.append(Subject(name))
            dialog.open = False
            refresh()

        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Neues Fach", weight=ft.FontWeight.W_600, color=INK),
            content=ft.Column(
                [ft.Text("Lege ein Fach an und passe die Gewichtung später jederzeit an.", size=13, color=MUTED), name_field],
                tight=True,
                spacing=14,
            ),
            actions=[
                ft.Button("Abbrechen", on_click=lambda event: close_dialog(event)),
                ft.Button("Fach erstellen", bgcolor=PURPLE, color=ft.Colors.WHITE, on_click=create_subject),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        def close_dialog(_: ft.ControlEvent) -> None:
            dialog.open = False
            page.update()

        page.dialog = dialog
        dialog.open = True
        page.update()

    header = ft.Container(
        padding=ft.Padding.only(left=28, right=28, top=24, bottom=18),
        content=ft.Row(
            [
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Icon(ft.Icons.AUTO_GRAPH_ROUNDED, color=ft.Colors.WHITE, size=22),
                            width=42,
                            height=42,
                            bgcolor=PURPLE,
                            border_radius=13,
                            alignment=ft.Alignment.CENTER,
                        ),
                        ft.Column(
                            [
                                ft.Text("Notan", size=23, weight=ft.FontWeight.W_700, color=INK),
                                ft.Text("Dein Notenplaner", size=12, color=MUTED),
                            ],
                            spacing=0,
                        ),
                    ],
                    spacing=12,
                ),
                ft.Container(expand=True),
                ft.Button(
                    "Fach hinzufügen",
                    icon=ft.Icons.ADD,
                    bgcolor=INK,
                    color=ft.Colors.WHITE,
                    on_click=open_subject_dialog,
                ),
            ],
        ),
    )

    hero = ft.Container(
        margin=ft.Margin.only(left=20, right=20, bottom=24),
        padding=ft.Padding.symmetric(horizontal=24, vertical=22),
        bgcolor=PURPLE_LIGHT,
        border_radius=24,
        content=ft.Row(
            [
                ft.Column(
                    [
                        ft.Text("Dein aktueller Schnitt", size=14, color="#5F5AAB"),
                        average_text,
                        summary_text,
                    ],
                    spacing=1,
                    expand=True,
                ),
                ft.Container(
                    content=ft.Icon(ft.Icons.SCHOOL_ROUNDED, color=PURPLE, size=42),
                    width=78,
                    height=78,
                    bgcolor="#FFFFFF99",
                    border_radius=22,
                    alignment=ft.Alignment.CENTER,
                ),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    page.add(
        ft.Column(
            [header, hero, ft.Container(subject_list, padding=ft.Padding.only(left=20, right=20, bottom=28))],
            spacing=0,
        )
    )
    refresh()


if __name__ == "__main__":
    ft.run(lambda page: main(page))