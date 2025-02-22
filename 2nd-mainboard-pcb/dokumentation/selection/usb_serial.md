! wichtige Anmerkung ! 
Weil es kein fertiges EDA-Modell vom FT232RNL gibt, wird der FT 232RL verwendet


https://www.digikey.at/de/products/detail/ftdi-future-technology-devices-international-ltd/FT232RNL-REEL/16836162
hat kein EDA Modell

https://www.digikey.at/de/products/detail/ftdi-future-technology-devices-international-ltd/FT232RL-REEL/1836385
hat EDA Modell


## **Komponentenauswahl: FT232R vs. FT232RN**

### **Ziel der Auswahl**
Für die serielle Kommunikation zwischen Mikrocontroller und PC wird ein USB-UART-Bridge-Chip benötigt, der stabile Datenübertragungen, geringe Latenz und einfache Integration bietet. Der Vergleich erfolgt zwischen dem **FT232R** und dem **FT232RN**, um die bestmögliche Komponente für das Projekt auszuwählen.

---

### **1. Funktionale Unterschiede**
| Merkmal                | FT232R                        | FT232RN                        | Kommentar                   |
|------------------------|--------------------------------|---------------------------------|-----------------------------|
| **Datenübertragungsrate** | Bis zu 3 Mbaud                | Bis zu 3 Mbaud                 | Keine Unterschiede          |
| **Signalstabilität**     | Standard Noise Tolerance      | Verbesserte Noise Immunity     | FT232RN ist robuster        |
| **USB-Interface**       | USB 2.0 Full-Speed            | USB 2.0 Full-Speed             | Gleichwertig                |
| **Zusatzfunktionen**     | Clock Output, EEPROM Support | Clock Output, verbesserter EEPROM Support | RN bietet mehr Optionen   |

---

### **2. Elektrische Spezifikationen**
| Merkmal                 | FT232R                        | FT232RN                        | Kommentar                   |
|-------------------------|-------------------------------|---------------------------------|-----------------------------|
| **Versorgungsspannung** | 3.3 V bis 5 V                | 3.3 V bis 5 V                  | Keine Unterschiede          |
| **Stromverbrauch**      | Höher bei identischer Last    | Optimiert für niedrigeren Verbrauch | RN effizienter           |
| **ESD-Schutz**          | Standard (±2 kV)              | Verbesserter Schutz (±4 kV)    | FT232RN ist robuster        |

---

### **3. Gehäuse und Pin-Kompatibilität**
| Merkmal                 | FT232R                        | FT232RN                        | Kommentar                   |
|-------------------------|-------------------------------|---------------------------------|-----------------------------|
| **Pin-Kompatibilität**  | Ja                           | Ja                              | 1:1 kompatibel              |
| **Gehäuse**             | SSOP28, QFN32                | SSOP28, QFN32                  | Keine Unterschiede          |

---

### **4. Software und Treiberunterstützung**
| Merkmal                 | FT232R                        | FT232RN                        | Kommentar                   |
|-------------------------|-------------------------------|---------------------------------|-----------------------------|
| **Treiber**             | FTDI VCP und D2XX            | FTDI VCP und D2XX              | Gleichwertig                |
| **Software-Features**   | EEPROM Konfiguration          | Erweiterte EEPROM-Konfiguration | RN bietet mehr Flexibilität |

---

### **5. Kosten**
| Merkmal                 | FT232R                        | FT232RN                        | Kommentar                   |
|-------------------------|-------------------------------|---------------------------------|-----------------------------|
| **Preis**               | Geringfügig niedriger         | Etwas teurer                   | RN bietet Mehrwert          |

---

### **6. Empfehlung für das Projekt**
Nach der Bewertung der technischen Daten wird der **FT232RN** empfohlen. Entscheidungsgründe:
- **Verbesserte Signalstabilität und Noise Immunity** erhöhen die Zuverlässigkeit des Systems.
- **Niedrigerer Stromverbrauch** macht ihn ideal für mobile oder energieeffiziente Anwendungen.
- **Erweiterter ESD-Schutz** bietet zusätzliche Sicherheit in industriellen Anwendungen.

--- 

### **Quellen**
- Datasheet FT232R, FTDI, 2020
	https://ftdichip.com/wp-content/uploads/2020/08/DS_FT232R.pdf
- Datasheet FT232RN, FTDI, 2024
	https://ftdichip.com/wp-content/uploads/2024/12/DS_FT232RN.pdf



