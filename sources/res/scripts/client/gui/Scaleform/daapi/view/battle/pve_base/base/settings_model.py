# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/base/settings_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/pve_base/base/settings_model.py
from __future__ import absolute_import
from enum import IntEnum
from pve_battle_hud import WidgetType

class BaseWidgetSettingsModel(object):
    __slots__ = ('id', 'type', 'state')

    def __init__(self, id, type, state):
        super(BaseWidgetSettingsModel, self).__init__()
        self.id = id
        self.type = WidgetType(type)
        self.state = state

    def setState(self, state):
        self.state = state
