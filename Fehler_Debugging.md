# 🚀 Flet 1.0.1+ API-Migration & Lerneffekte

Diese Übersicht fasst den Wandel von der alten imperativen Flet-Architektur (0.x) hin zur modernen, deklarativen und zustandsbasierten Entwicklung in Flet 1.0+ zusammen.

---

## 🧩 1. Imperativ vs. Deklarativ (Der Paradigmenwechsel)

### Früher (Imperativer Stil)
Du musstest UI-Elemente manuell im Code referenzieren, ihre Werte Schritt für Schritt überschreiben und die Oberfläche manuell aktualisieren.
* Code fühlte sich an wie eine Kette von Befehlen: *„Ändere Text, ändere Farbe, aktualisiere Seite.“*
* Hohes Risiko, dass die UI asynchron zum eigentlichen Datenzustand wird.

### Heute (Deklarativer Stil)
Die Benutzeroberfläche spiegelt zu jedem Zeitpunkt den aktuellen Zustand (**State**) der App wider.
* Du definierst Variablen, die den Zustand beschreiben (z. B. `is_blue`).
* Die UI-Elemente lesen diesen Zustand dynamisch ab.
* **Auto-Update:** Ändert sich der Zustand, berechnet Flet die UI-Differenz automatisch im Hintergrund und zeichnet den Bildschirm neu. Ein manuelles `page.update()` ist in Event-Handlern nicht mehr nötig.

---

## 🛠️ 2. Die wichtigsten API-Änderungen im Überblick

| Feature / Element | Altes Flet (0.x) | Modernes Flet (1.0.1+) | Grund der Änderung |
| :--- | :--- | :--- | :--- |
| **App-Start** | `ft.app(target=main)` | `ft.run(lambda p: main(p))` | Vereinheitlichung des Lebenszyklus |
| **UI-Montage** | `page.add(Komponente())` | `page.render(Komponente)` | Aktiviert die neue Hook- & Rendering-Pipeline |
| **Farben** | `ft.colors.BLUE` | `ft.Colors.BLUE` | Umstellung auf großgeschriebene Klassenstrukturen |
| **Ausrichtung** | `ft.alignment.center` | `ft.Alignment.CENTER` | Vereinheitlichung von Enums & Konstanten |
| **Schaltflächen** | `ft.ElevatedButton(...)` | `ft.Button(...)` | Konsolidierung überflüssiger Button-Klassen |

---

## ⚠️ 3. Typische Fehlermeldungen und ihre Behebung

### ❌ `AttributeError: module 'flet' has no attribute 'app'`
* **Ursache:** Du versuchst, den alten Startbefehl zu nutzen.
* **Lösung:** Ersetze `ft.app(target=main)` durch `ft.run(main)` (bzw. die stabilere Lambda-Schreibweise).

### ❌ `AttributeError: module 'flet' has no attribute 'colors'` (oder `alignment`)
* **Ursache:** Zugriff auf die alten, kleingeschriebenen Module.
* **Lösung:** Nutze die neuen Klassen mit großem Anfangsbuchstaben (`ft.Colors` / `ft.Alignment`) und schreibe die Konstanten komplett in Großbuchstaben (z. B. `ft.Alignment.CENTER`).

### ❌ `The application encountered an error: No current renderer is set.`
* **Ursache:** Du nutzt moderne Hooks wie `ft.use_state()`, fügst die Komponente aber über das alte `page.add()` hinzu. Flet fehlt dadurch der logische Kontext für den Zustand.
* **Lösung:** Übergreife die Komponente als reinen Funktionsverweis (ohne Klammern) an die neue Methode: `page.render(MeineKomponente)`.

---

## 💡 4. Best Practices für sauberen Flet 1.0-Code

1. **Typisierung nutzen:** Nutze Pythons `typing`-Modul (z. B. `page: ft.Page`, `e: ft.ControlEvent`), um Autovervollständigung in deiner IDE zu aktivieren und Fehler frühzeitig abzufangen.
2. **Abgeleiteter Zustand (Derived State):** Berechne Farben, Texte oder Sichtbarkeiten direkt unterhalb deiner Hooks basierend auf dem aktuellen State. Vermeide es, Zustände doppelt abzuspeichern.
3. **Komponenten isolieren:** Halte deine `@ft.component`-Funktionen klein und fokussiert. Jede Komponente sollte nur für ihren eigenen Bereich zuständig sein.
