# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/vse_hud_settings_ctrl/settings/progress_counter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/vse_hud_settings_ctrl/settings/progress_counter.py
from __future__ import absolute_import
import typing
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.base_models import TextClientModel

class ProgressCounterClientModel(TextClientModel):
    __slots__ = ('id', 'header', 'icon')

    def __init__(self, id, header, icon):
        super(ProgressCounterClientModel, self).__init__()
        self.id = id
        self.header = header
        self.icon = icon

    def getHeader(self, params):
        return self._getPluralText(self.header, params)

    def __repr__(self):
        return '<ProgressCounterClientModel>: id=%s, header=%s, icon=%s' % (
         self.id, self.header, self.icon)
