import subprocess
import tkinter as tk
from tkinter import simpledialog, messagebox

def create_release():
    # GUI für die Eingabe der Version
    root = tk.Tk()
    root.withdraw()  # Verstecke das Hauptfenster

    version = simpledialog.askstring("Release Version", "Welche Version möchtest du erstellen? (z.B. v1.0.0)")
    if not version:
        messagebox.showinfo("Abbruch", "Keine Version eingegeben. Abbruch.")
        return

    if not version.startswith("v") or not version[1:].replace(".", "").isdigit():
        messagebox.showerror("Fehler", "Ungültiges Format. Bitte im Format 'vX.X.X' eingeben.")
        return

    # Tag erstellen und pushen
    try:
        subprocess.run(["git", "tag", "-a", version, "-m", f"Release {version}"], check=True)
        subprocess.run(["git", "push", "origin", version], check=True)
        messagebox.showinfo("Erfolg", f"Tag {version} wurde erfolgreich erstellt und gepusht.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Fehler", f"Fehler beim Erstellen oder Pushen des Tags:\n{e}")

if __name__ == "__main__":
    create_release()
