# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/vehicle_hub/sub_presenters/armor/config/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/vehicle_hub/sub_presenters/armor/config/__init__.py
from __future__ import absolute_import
import typing, ResMgr, section2dict
from gui.impl.lobby.vehicle_hub.sub_presenters.armor.config.schemas import configSchema
if typing.TYPE_CHECKING:
    from gui.impl.lobby.vehicle_hub.sub_presenters.armor.config.models import ConfigModel
CONFIG_PATH = 'gui/armor_inspector.xml'
__config = None

def getConfig():
    global __config
    if __config is not None:
        return __config
    else:
        root = ResMgr.openSection(CONFIG_PATH)
        rawData = section2dict.parse(root)
        __config = configSchema.deserialize(rawData)
        return __config
