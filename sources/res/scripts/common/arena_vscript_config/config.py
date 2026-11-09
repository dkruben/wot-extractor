# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/arena_vscript_config/config.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/arena_vscript_config/config.py
from __future__ import absolute_import
import typing, logging
from extension_utils import ResMgr
import section2dict
from arena_vscript_config.schemas import configSchema
if typing.TYPE_CHECKING:
    from arena_vscript_config.schemas import ConfigModel
_CONFIG_FILE = 'scripts/item_defs/arena_vscripts.xml'
_g_config = None
_logger = logging.getLogger(__name__)

def _readFromXml(xmlPath):
    section = ResMgr.openSection(xmlPath)
    if section is None:
        _logger.error('Broken xml schemas source: %s.', xmlPath)
        return
    else:
        rawData = section2dict.parse(section)
        ResMgr.purge(xmlPath, True)
        return configSchema.deserialize(rawData)


def init():
    global _g_config
    if _g_config is None:
        _g_config = _readFromXml(_CONFIG_FILE)
        _logger.info('Arena vscripts ConfigModel created from: %s.', _CONFIG_FILE)
    return


def getInstance():
    if _g_config is None:
        _logger.error('Arena vscripts ConfigModel not initialized.')
    return _g_config
