# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/persistent_data_cache/version.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/persistent_data_cache/version.py
from __future__ import absolute_import
import typing, constants
from helpers import version
from persistent_data_cache_common.common import getLogger
_logger = getLogger('Version')

def getClientPDCVersion():
    clientVersion = version.getClientVersion()
    locVersion = version.getLocalizationVersion()
    result = (
     clientVersion.version,
     clientVersion.meta.overrides,
     clientVersion.meta.client,
     clientVersion.meta.realm,
     locVersion.version,
     locVersion.revision,
     locVersion.language)
    if not constants.IS_DEVELOPMENT and '' in result:
        _logger.error('Invalid client version: %s', result)
        return None
    else:
        return result
