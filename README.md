# Fiberprinter Electronics

Dieses Repository enthält die Elektronikentwicklung für den faserverlegenden 3D-Drucker, der im Rahmen einer Diplomarbeit an der HTBLA Kaindorf entwickelt wird. Die Elektronik umfasst sowohl die Steuerung der Druckkopffunktionen als auch die Anbindung an das Hauptsystem mittels eines Raspberry Pi mit **Klipper-Firmware**.

## 📌 Projektübersicht

Das Ziel dieses Projekts ist die Entwicklung einer modularen und effizienten Steuerung für den Druckkopf, die über eine eigenentwickelte Platine mit einem **ATmega328** realisiert wird. Diese übernimmt spezifische Aufgaben, die über das Hauptsystem des Druckers nicht direkt gesteuert werden.

## ⚙️ Hauptkomponenten

### 1️⃣ **Steuerungshardware**
- **Raspberry Pi** mit Klipper-Firmware zur übergeordneten Steuerung
- **Eigenes Mainboard mit ATmega328** zur Ansteuerung folgender Komponenten:
  - Lüfter
  - BL Touch (Autoleveling-Sensor)
  - Servo
  - Schrittmotor
  - Temperatursensoren
- **Breakout-Board für den ATmega2560**, das Test- und Messpunkte sowie einen Bootloader enthält
- **FT232RL** als USB-to-Serial-Adapter für die Kommunikation mit dem ATmega2560
- **Reset-Button** zur einfachen Rücksetzung des Systems

### 2️⃣ **Firmware & Kommunikation**
- Der **ATmega328** wird von der Klipper-Firmware auf dem Raspberry Pi über USB angesprochen
- Kommunikation erfolgt über **serielles Protokoll**
- Entwicklung einer **angepassten Firmware für den ATmega328**, um die spezifischen Druckkopf-Funktionen auszuführen

### 3️⃣ **Software**
- Python-Skript zur **Integration der Steuerung in Klipper**
- Implementierung eines Protokolls zur **Steuerung der Hardware aus Klipper heraus**
- Zusammenarbeit mit der **Slicing-Software**, um die gezielte Faserverlegung zu ermöglichen


## 🛠️ Entwicklungsteam

- **Jan Traußnigg** – Elektronikdesign & Firmware
- **Nico Hütter** – Konstruktion, Aufbau & Testung
- **Elias Gottsbacher** – Slicing-Software & Software-Integration

## 📜 Lizenz

Dieses Projekt steht unter der **MIT-Lizenz**. Weitere Details sind in der Datei `LICENSE` zu finden.
