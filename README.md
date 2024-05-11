# colinkmd
convert linklists markdown files into yaml

## Projekt: colinkmd
Das Projekt "colinkmd" konvertiert eine in Markdown gepflegte Linkliste in eine strukturierte YAML Datei. 
Die YAML-Dateien können dann von "gethomepage" verwendet werden, um die Link-Sammlungen zu generieren oder zu aktualisieren. 

# Usage:
Linkliste in Markdown wird konvertiert zu einer yaml die von gethomepage gelesen werden kann

### Ziel
Vereinfachung der Verwaltung von Linklisten durch die Bereitstellung eines Tools, das Markdown in eine YAML-Struktur umwandelt.
Dies erleichtert die Integration in webbasierte Plattformen und verbessert die Übersichtlichkeit und Wartbarkeit der Link-Daten.

### Features
- **Markdown Parsing**: Analyse und Interpretation von Markdown-Dateien, um Links und zugehörige Informationen zu extrahieren.
- **YAML-Konversion**: Umwandlung der extrahierten Daten in eine strukturierte YAML-Datei, die leicht von anderen Anwendungen gelesen werden kann.
- **Konfigurierbare Templates**: Möglichkeit zur Definition benutzerdefinierter YAML-Strukturen basierend auf den Bedürfnissen der Zielanwendung.
- **Kommandozeilen-Interface (CLI)**: Einfache Bedienung über die Kommandozeile für schnelle Konvertierungen.
- **Fehlerbehandlung und Validierung**: Sicherstellung, dass die erzeugten YAML-Dateien den Spezifikationen entsprechen und fehlerfrei sind.

#### Kommandozeilen-Verwendung
```
colinkmd convert -i input.md -o output.yaml
```

#### Beispiel

##### Eingabe: `links.md`

```markdown
# Meine Links

## Gruppe
- [Titel](https://any.link.to)

## Blankpages
- [Titel Blank Page](about:blank) - Blank Page

## Entertainment
- [Twitch](https://www.twitch.tv) - Twitch Live Streaming Platform **TW**
- [Netflix](https://www.netflix.com/de) - Streaming Platform **NF**
```

## Entertainment
- [Twitch](https://www.twitch.tv) - Twitch Live Streaming Platform **TW**
- [Netflix](https://www.netflix.com/de) - Streaming Platform **NF**

##### Ausgabe: `bookmarks.yaml`

```yaml
- Gruppe:
    - Titel:
        - abbr: AK
          icon: https://www.google.com/favicon.ico
          href: http://about:blank
          description: Blank

    - Twitch:
        - abbr: TW
          icon: si-twitch-#9146FF
          href: https://www.twitch.tv
          description: Twitch
```


### Weiterentwicklung
- **UI Integration**: Entwicklung einer grafischen Benutzeroberfläche für einfacheres Handling und Visualisierung der Konvertierungsprozesse.
- **Plugin-System**: Erweiterung der Funktionalität durch Plugins, die spezifische Anpassungen oder Erweiterungen der Kernfunktionalität erlauben.

Dieses Konzept bietet eine klare Struktur und einfache Bedienbarkeit, die es Endnutzern ermöglicht, ihre Linklisten effizient zu verwalten und in verschiedenen Anwendungskontexten zu nutzen.




```code
Gruppe          # Gruppe wird manuell festgelegt. 
titel           # Der Titel wird aus der URL und oder dem Titel der Webseite extrahiert
abbr            # Die Abkürzung kann aus den Anfangsbuchstaben des Namens oder der URL bestehen
description     # Wenn in der Datei keine Daten verfügbar könnte ChatGPT die Beschreibung erzeugen
icon            # Das Icon kommt entweder von simpleicons.org oder es könnte von ChatGPT erzeugt werden
href            # Das ist die URL die zum Ziel führt
```