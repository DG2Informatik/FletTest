from typing import Any

import flet as ft


# =============================================================================
# 1. DIE DEKLARATIVE FUNKTIONS-KOMPONENTE
# =============================================================================
@ft.component
def ColorSwitcher() -> ft.Container:
    """Eine deklarative Flet-Komponente, die ihren Zustand (State) mittels Hooks verwaltet.

    Gibt ein stabiles ft.Container-Steuerelement für die Rendering-Pipeline
    zurück.
    """
    # HOOK-SYSTEM (NEU IN FLET 1.0):
    # 'ft.use_state' registriert einen reaktiven Zustand im internen Renderer-Baum.
    # Er gibt zwei Werte zurück:
    # 1. Den aktuellen Wert (is_blue: bool)
    # 2. Eine Funktion, um diesen Wert sicher zu verändern (set_is_blue)
    is_blue: bool
    set_is_blue: Any  # Funktionstyp für den Hook-Setter
    is_blue, set_is_blue = ft.use_state(False)

    # ABGELEITETER ZUSTAND (DERIVATIVE STATE):
    # Wir berechnen die UI-Eigenschaften dynamisch direkt aus dem Zustand.
    # WUNSCH-LOGIK: Wenn der Hintergrund Grün ist (nicht blau), soll die
    # Beschriftung "Wechsel zu Blau" signalisieren.
    btn_text: str = "Wechsel zu Grün" if is_blue else "Wechsel zu Blau"
    btn_color: str = ft.Colors.GREEN if is_blue else ft.Colors.BLUE
    bg_color: str = ft.Colors.BLUE_50 if is_blue else ft.Colors.GREEN_50

    # EVENT-HANDLER:
    # Diese Funktion wird beim Klicken aufgerufen.
    def toggle_color(e: ft.ControlEvent) -> None:
        # FEHLER-BEHEBUNG: In Flet 1.0+ entfällt 'page.update()' in Event-Handlern komplett!
        # Durch den Aufruf des Setters erfährt Flet, dass sich der Zustand geändert hat,
        # berechnet die UI-Differenz ("Diffing") und zeichnet den Bildschirm vollautomatisch neu.
        set_is_blue(not is_blue)

    # REAKTIVES UI-LAYOUT (DEKLARATIVER STIL):
    # Wir bauen das Layout und binden unsere Variablen direkt an die Attribute.
    return ft.Container(
        content=ft.Column(
            controls=[
                # FEHLER-BEHEBUNG: ft.ElevatedButton wurde entfernt. Es gibt nur noch ft.Button.
                # Zudem nimmt ft.Button den Text direkt als ersten Positionsparameter an.
                ft.Button(
                    btn_text,
                    bgcolor=btn_color,
                    color=ft.Colors.WHITE,
                    on_click=toggle_color,  # type: ignore[assignment, arg-type]
                )
            ]
        ),
        bgcolor=bg_color,
        padding=20,
        # FEHLER-BEHEBUNG: Kleingeschriebene Enums wie 'ft.alignment.center' wurden durch
        # die großgeschriebene Klasse 'ft.Alignment.CENTER' ersetzt.
        alignment=ft.Alignment.CENTER,
        expand=True,  # Lässt den Container das gesamte App-Fenster ausfüllen
    )


# =============================================================================
# 2. HAUPTFUNKTION (EINSTIEGSPUNKT DER APP)
# =============================================================================
def main(page: ft.Page) -> None:
    """Konfiguriert das Hauptfenster der Anwendung und stößt die

    deklarative Rendering-Pipeline an.
    """
    # Seiteneinstellungen vornehmen
    page.title = "Flet 1.0.1 Modern & Typisiert"
    page.theme_mode = ft.ThemeMode.LIGHT

    # FEHLER-BEHEBUNG: 'page.add()' darf für reaktive Hook-Komponenten nicht genutzt werden.
    # Die Komponente wird als Funktionsverweis (ohne Klammern) an 'page.render()' übergeben.
    # Nur so wird der zwingend erforderliche "Renderer-Kontext" für ft.use_state() geöffnet.
    page.render(ColorSwitcher)


# =============================================================================
# 3. APP-START (BOOTSTRAPPING)
# =============================================================================
if __name__ == "__main__":
    # FEHLER-BEHEBUNG: 'ft.app(target=main)' existiert in Flet 1.0+ nicht mehr.
    # Es wurde durch 'ft.run()' ersetzt. Um einen stabilen Lebenszyklus zu garantieren,
    # wird die Hauptfunktion sauber über einen Lambda-Ausdruck gestartet.
    ft.run(lambda page: main(page))
