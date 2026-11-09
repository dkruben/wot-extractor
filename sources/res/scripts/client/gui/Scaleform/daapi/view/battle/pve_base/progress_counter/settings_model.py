# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/progress_counter/settings_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/pve_base/progress_counter/settings_model.py
from __future__ import absolute_import
import typing
from gui.Scaleform.daapi.view.battle.pve_base.base.settings_model import BaseWidgetSettingsModel
from pve_battle_hud import ProgressCounterState

class ProgressCounterServerModel(BaseWidgetSettingsModel):
    __slots__ = ('params', )

    def __init__(self, id, type, state, params):
        super(ProgressCounterServerModel, self).__init__(id, type, ProgressCounterState(state))
        self.params = params

    def __repr__(self):
        return '<ProgressCounterServerModel>: id=%s, type=%s, state=%s, params=%s' % (
         self.id, self.type, self.state, self.params)
