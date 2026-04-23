# -*- coding: utf-8 -*-
{
    'name': 'Alineas Demo Data – Südtirol',
    'version': '19.0.1.0.0',
    'summary': 'Realistische Demodaten für den Südtiroler Kontext: deutschsprachige Firmen mit italienischer Fiskalisierung.',
    'description': """
Alineas Demo Data – Südtirol
=============================

- Muster-Unternehmen (Bozen) mit IT-Kontenplan, Partita IVA, Codice Fiscale, SDI-Code
- 15 Südtiroler Partner aus Handel, Dienstleistungen und Industrie
- 20 Produkte mit deutschen Bezeichnungen (Dienstleistungen, Waren, Rohstoffe)
- 7 Rechnungsbelege (TD01, TD04)
- Alle E-Mail-Adressen sind Fake (.example) – kein versehentlicher Versand
- Kein Demo-Modus erforderlich: lädt beim Installieren des Moduls
""",
    'author': 'Alineas',
    'website': 'https://www.alineas.it',
    'category': 'Hidden',
    'depends': [
        'account',
        'l10n_it',
        'l10n_it_edi',
        'contacts',
        'sale_management',
        'purchase',
        'stock',
    ],
    'data': [
        'data/demo_company.xml',
        'data/demo_partners.xml',
        'data/demo_products.xml',
        'data/demo_invoices.xml',
    ],
    'pre_init_hook': 'pre_init_hook',
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
