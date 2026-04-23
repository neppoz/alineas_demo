# -*- coding: utf-8 -*-
import logging

_logger = logging.getLogger(__name__)


def pre_init_hook(env):
    _logger.warning("=" * 60)
    _logger.warning("ALINEAS DEMO DATA – Installation gestartet ...")
    _logger.warning("Südtiroler Demodaten werden geladen (Firma, Partner, Produkte, Rechnungen)")
    _logger.warning("=" * 60)


def post_init_hook(env):
    _logger.warning("=" * 60)
    _logger.warning("ALINEAS DEMO DATA – Installation abgeschlossen!")
    _logger.warning("Alpenvision GmbH + 15 Partner + 20 Produkte + 7 Rechnungen bereit.")
    _logger.warning("=" * 60)
