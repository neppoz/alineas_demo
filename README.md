# Alineas Demo Data – Südtirol

Realistische Odoo-Demodaten für den **Südtiroler Kontext**: deutschsprachige Unternehmen mit vollständiger italienischer Fiskalisierung (Fatturazione Elettronica / SDI).

---

## Inhalt

### Unternehmen
- **Alpenvision GmbH** — Sitz in Bozen (BZ)
- Italienischer Kontenplan (`l10n_it`)
- Partita IVA, Codice Fiscale, SDI-Destinatario-Code, Steuerregime RF01
- IBAN-Bankkonto
- EDI-Proxy im **Demo-Modus** — simuliert den vollständigen SDI-Austausch ohne echte Zugangsdaten

### Partner (15)
Fiktive Südtiroler Unternehmen aus drei Branchen:

| Branche | Rolle |
|---|---|
| Handel (Lebensmittel, Baustoffe, Frischobst, Verpackung) | Kunden & Lieferanten |
| Dienstleistungen (Steuerberatung, IT, Logistik, Reinigung) | Kunden & Lieferanten |
| Industrie (Metallbau, Holzverarbeitung, Kunststoff, Maschinenbau) | Lieferanten & Kunden |

Jeder Partner hat: Name (DE), Adresse (Provinz BZ), VAT, Codice Fiscale, SDI-Code, PEC-E-Mail.  
Alle E-Mail-Adressen enden auf `.example` — kein versehentlicher E-Mail-Versand möglich.

### Produkte (20)
Deutsche Bezeichnungen, aufgeteilt in drei Kategorien:

- **Dienstleistungen** — Beratung, IT-Support, Software-Abo, Wartung, Transport
- **Handelswaren** — Laptop, Monitor, Bürostuhl, Schreibtisch, Drucker
- **Rohstoffe & Verbrauchsmaterial** — Stahlrohr, Alublech, Holzbalken, Schrauben, Sicherheitsausrüstung u.a.

### Rechnungen (7)
- 4 Ausgangsrechnungen (TD01)
- 1 Gutschrift (TD04)
- 2 Eingangsrechnungen (TD01)

Alle Belege im Entwurfsstatus mit korrekt gesetztem `l10n_it_document_type`.

### Bilder
- Firmenlogo (Alpenvision GmbH)
- Benutzeravatar (Admin)
- Produktbilder für alle 20 Artikel

Die Bilder werden mit [Pillow](https://python-pillow.org/) generiert. Das Skript liegt unter `static/img/generate_images.py`.

---

## Installation

1. Modul in den Odoo-Addons-Pfad legen
2. Neue Datenbank anlegen
3. Modul `alineas_demo` installieren

Odoo installiert alle Abhängigkeiten automatisch (`l10n_it_edi`, `sale_management`, `contacts`, `purchase`, `stock` etc.) und lädt anschließend die Demodaten. **Kein Demo-Modus erforderlich.**

Der Installationsfortschritt ist im Server-Log als `WARNING` sichtbar:

```
WARNING ... ALINEAS DEMO DATA – Installation gestartet ...
...
WARNING ... ALINEAS DEMO DATA – Installation abgeschlossen!
```

---

## Abhängigkeiten

```
account · l10n_it · l10n_it_edi · contacts · sale_management · purchase · stock
```

---

## SDI Demo-Modus

Das Modul konfiguriert einen EDI-Proxy-User mit `edi_mode = demo`. Damit wird der komplette FatturaPA-Workflow simuliert (Erstellen → XML generieren → Übertragung → Status-Rückmeldung), ohne echte SDI-Zugangsdaten zu benötigen. Ideal für Kundenpräsentationen.

---

## Kompatibilität

Getestet auf **Odoo 19.0**.

---

## Autor

**Neves Parrottino** — [Alineas](https://www.alineas.it) · Odoo Solution Partner  
help@alineas.it
