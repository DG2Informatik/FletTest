# 🚀 So startest du das Programm (Flet im GitHub-Codespace)

## 1. Codespace öffnen

**Teil A: Im Codespace (Cloud)**

**Fall A – Du hast schon einen Codespace (normaler Fall):**
1. Repo öffnen → **Code** → Tab **Codespaces**
2. Deinen bestehenden Codespace (z. B. „ideal fishstick") **anklicken**
3. Du landest genau dort weiter, wo du aufgehört hast – nichts neu installieren!

**Fall B – Noch nie einen Codespace erstellt (einmalig):**
1. Repo öffnen → **Code** → Tab **Codespaces** → **„+"** → *Create codespace*
2. Erster Start dauert ein paar Minuten – Container wird eingerichtet (uv, Pakete, alles)

> ⚠️ Regel: **Nur einen Codespace pro Repo und Person.** Nicht jedes Mal einen neuen erstellen – alte Codespaces kosten Speicherplatz und werden nach 30 Tagen Inaktivität gelöscht.

## 2. Programm starten

Im Terminal des Codespaces:

```bash
uv run flet run --web --port 8550 main_imperativ.py
```

- Die App öffnet sich automatisch im Browser
- **Speichern = App aktualisiert sich sofort** (Hot Reload)

## 3. Arbeiten und sichern

```bash
git add .
git commit -m "Kurz beschreiben, was du geändert hast"
git push
```

## 4. Feierabend

- Nur den Browser-Tab schließen? Der Codespace läuft noch und stoppt später automatisch von selbst.
- Oder im Browser-Tab den Code-Space sauber herunterfahren (Ctrl/Cmd+Shift+P → „Codespaces: Stop Current Codespace").

---

## 🧠 Merksatz

**Codespace anklicken → `uv run flet run --web --port 8550` → coden → committen → push.**

## ❓ Kleine Störungsshilfe

| Problem | Lösung |
|---|---|
| App zeigt nichts Neues | Im Terminal schauen, ob ein Fehler beim Speichern kam; Seite neu laden |
| „File ... not found" | Prüfen, ob du im richtigen Ordner bist (`cd /workspaces/FletTest`) |
| Codespace „kaputt" | Ctrl/Cmd+Shift+P → **Rebuild Container** (vorher committen!) |
| Wirklich alles kaputt | Alten Codespace auf github.com/codespaces löschen, mit **„+"** neu erstellen |

---

# 💻 Alternative: Lokal mit VS Code (ohne Codespace)

Du hast VS Code fest installiert? Dann brauchst du **keinen** Codespace.

## 1. Setup einmalig pro Rechner

```bash
# 1. Repo klonen
git clone https://github.com/DG2Informatik/FletTest.git
cd FletTest

# 2. uv installieren (falls nicht vorhanden)
#    Windows (PowerShell):
winget install astral-sh.uv
#    macOS/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh

# 3. Umgebung aus dem Repo bauen
uv sync
```

> Python muss nicht vorinstalliert sein – uv holt sich bei Bedarf selbst eine passende Version.

## 2. Programm starten (natives Fenster, ohne Browser)

```bash
uv run flet run main_imperativ.py
```

- Die App öffnet sich als **eigenes Fenster** auf deinem Rechner
- **Speichern = App aktualisiert sich sofort** (Hot Reload)

## 3. Arbeiten

- Projektordner in VS Code öffnen und normal coden
- Als Python-Interpreter die `.venv` aus dem Projektordner wählen (unten rechts in der Statusleiste)
- Am Ende committen und pushen wie in Teil A, Punkt 3

## 4. Feierabend

Terminal zu, fertig. Deine Umgebung (`.venv` im Projektordner) ist beim nächsten Mal sofort wieder da.

## 🧠 Merksatz (lokal)

**`git pull` → `uv run flet run` → coden → committen → push.**

## ❓ Störungshilfe (lokal)

| Problem | Lösung |
|---|---|
| „File ... not found" | Ins Projektordner-Terminal wechseln (`cd FletTest`) |
| Umgebung kaputt | `.venv`-Ordner löschen, dann `uv sync` |
| App startet nicht | Terminal-Ausgabe lesen; Notausgang: Repo neu klonen + `uv sync` |

---

## 🆚 Der einzige echte Unterschied zwischen beiden Wegen

| | Codespace | Lokal mit VS Code |
|---|---|---|
| Setup | „+" klicken, fertig | `git clone` + `uv sync` |
| Startbefehl | `uv run flet run --web --port 8550 ...` | `uv run flet run ...` |
| App läuft als | Browser-Vorschau | natives Fenster |
| Git, uv, Code | identisch | identisch |

> Beide Gruppen arbeiten am **selben Repo** mit demselben Code – ihr könnt jederzeit mischen und zwischen den Wegen wechseln.