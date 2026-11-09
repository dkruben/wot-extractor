# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/vse_hud_settings_ctrl/settings/primary_objective.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/vse_hud_settings_ctrl/settings/primary_objective.py
from __future__ import absolute_import
import typing
from typing import List
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.base_models import TextClientModel

class PrimaryObjectiveClientModel(TextClientModel):
    __slots__ = ('id', 'header', 'subheader', 'startSound', 'remindTimers', 'remindSound',
                 'countdownTimer', 'countdownSound', 'success', 'successIcon', 'successSound',
                 'failure', 'failureIcon', 'failureSound')

    def __init__(self, id, header, subheader, startSound, remindTimers, remindSound, countdownTimer, countdownSound, success, successIcon, successSound, failure, failureIcon, failureSound):
        super(PrimaryObjectiveClientModel, self).__init__()
        self.id = id
        self.header = header
        self.subheader = subheader
        self.startSound = startSound
        self.remindTimers = sorted(remindTimers, reverse=True)
        self.remindSound = remindSound
        self.countdownTimer = countdownTimer
        self.countdownSound = countdownSound
        self.success = success
        self.successIcon = successIcon
        self.successSound = successSound
        self.failure = failure
        self.failureIcon = failureIcon
        self.failureSound = failureSound

    def getHeader(self):
        return self._getText(self.header)

    def getSubheader(self, params):
        return self._getPluralText(self.subheader, params)

    def getSuccess(self):
        return self._getText(self.success)

    def getFailure(self):
        return self._getText(self.failure)

    def __repr__(self):
        return '<PrimaryObjectiveClientModel>: id=%s, header=%s, subheader=%s, startSound=%s, remindTimers=%s, remindSound=%s, countdownTimer=%s, countdownSound=%s, success=%s, successIcon=%s, successSound=%s, failure=%s, failureIcon=%s, failureSound=%s' % (
         self.id, self.header, self.subheader, self.startSound, self.remindTimers, self.remindSound,
         self.countdownTimer, self.countdownSound, self.success, self.successIcon, self.successSound,
         self.failure, self.failureIcon, self.failureSound)
