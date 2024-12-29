#!/bin/bash

# Funktion, um eine Eingabe zu erhalten
read_version() {
  echo "Welche Version möchtest du erstellen? (z.B. v1.0.0)"
  read -r version
  # Überprüfen, ob die Eingabe im Tag-Format ist
  if [[ ! "$version" =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo "Ungültiges Format. Bitte gib die Version im Format 'vX.X.X' ein."
    read_version
  fi
}

# Nach der Version fragen
read_version

# Bestätigen, bevor fortgefahren wird
echo "Erstelle und pushe Tag: $version. Bist du sicher? (y/n)"
read -r confirmation

if [[ "$confirmation" != "y" ]]; then
  echo "Abgebrochen."
  exit 0
fi

# Tag erstellen
echo "Erstelle Tag: $version"
git tag -a "$version" -m "Release $version"

# Tag pushen
echo "Pushe Tag: $version"
git push origin "$version"

# Erfolgsmeldung
echo "Tag $version wurde erstellt und gepusht. Die Release-Pipeline sollte jetzt starten!"
