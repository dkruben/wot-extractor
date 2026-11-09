# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/primary_objective/settings_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/pve_base/primary_objective/settings_model.py
from __future__ import absolute_import
import typing
from gui.Scaleform.daapi.view.battle.pve_base.base.settings_model import BaseWidgetSettingsModel
from pve_battle_hud import PrimaryObjectiveState

class PrimaryObjectiveServerModel(BaseWidgetSettingsModel):
    __slots__ = ('timer', 'finishTime', 'progresses', 'params')

    def __init__(self, id, type, state, timer, finishTime, progresses, params):
        super(PrimaryObjectiveServerModel, self).__init__(id, type, PrimaryObjectiveState(state))
        self.timer = timer
        self.finishTime = finishTime
        self.progresses = progresses
        self.params = params

    def __repr__(self):
        return '<PrimaryObjectiveServerModel>: id=%s, type=%s, state=%s, timer=%s, finishTime=%s, progresses=%s, params=%s' % (
         self.id, self.type, self.state, self.timer, self.finishTime, self.progresses, self.params)
