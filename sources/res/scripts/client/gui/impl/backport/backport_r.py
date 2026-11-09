# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/backport/backport_r.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/backport/backport_r.py
from __future__ import absolute_import
import typing, logging
from frameworks import wulf
_logger = logging.getLogger(__name__)

def text(resId, *args, **kwargs):
    if resId <= 0:
        _logger.warning('Invalid resId')
        return u''
    if args:
        try:
            return wulf.getTranslatedTextByResId(resId, args)
        except (TypeError, ValueError):
            _logger.warning("Arguments do not match string with resId '%r': %r", resId, args)
            return u''

    elif kwargs:
        try:
            return wulf.getTranslatedTextByResId(resId, kwargs)
        except (TypeError, ValueError):
            _logger.warning("Arguments do not match string with resId '%r': %r", resId, kwargs)
            return u''

    return wulf.getTranslatedTextByResId(resId)


def ntext(resId, n, *args, **kwargs):
    if resId <= 0:
        _logger.warning('Invalid resId')
        return u''
    if args:
        try:
            return wulf.getTranslatedPluralTextByResId(resId, n, args)
        except (TypeError, ValueError):
            _logger.warning("Arguments do not match string with resId '%r': %r", resId, args)
            return u''

    elif kwargs:
        try:
            return wulf.getTranslatedPluralTextByResId(resId, n, kwargs)
        except (TypeError, ValueError):
            _logger.warning("Arguments do not match string with resId '%r': %r", resId, kwargs)
            return u''

    return wulf.getTranslatedPluralTextByResId(resId, n)


def msgid(resId):
    return wulf.getTranslatedKey(resId)


def image(resId):
    return wulf.getImagePath(resId)


def sound(resId):
    return wulf.getSoundEffectId(resId)


def layout(resId):
    return wulf.getLayoutPath(resId)
