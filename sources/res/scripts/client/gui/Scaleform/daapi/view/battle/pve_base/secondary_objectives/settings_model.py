# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/secondary_objectives/settings_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/pve_base/secondary_objectives/settings_model.py
from __future__ import absolute_import
import typing
from gui.Scaleform.daapi.view.battle.pve_base.base.settings_model import BaseWidgetSettingsModel
from pve_battle_hud import SecondaryObjectiveState

class SecondaryObjectiveServerModel(BaseWidgetSettingsModel):
    __slots__ = ('timer', 'finishTime', 'progress', 'params')

    def __init__(self, id, type, state, timer, finishTime, progress, params):
        super(SecondaryObjectiveServerModel, self).__init__(id, type, SecondaryObjectiveState(state))
        self.timer = timer
        self.finishTime = finishTime
        self.progress = progress
        self.params = params

    def __repr__(self):
        return '<SecondaryObjectiveServerModel>: id=%s, type=%s, state=%s, timer=%s, finishTime=%s, progress=%s, params=%s' % (
         self.id, self.type, self.state, self.timer, self.finishTime, self.progress, self.params)
