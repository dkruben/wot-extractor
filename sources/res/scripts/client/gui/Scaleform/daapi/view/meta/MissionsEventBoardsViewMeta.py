# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/MissionsEventBoardsViewMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MissionsEventBoardsViewMeta.py
from gui.Scaleform.daapi.view.lobby.missions.regular.missions_page import ElenMissionView

class MissionsEventBoardsViewMeta(ElenMissionView):

    def openBoardView(self):
        self._printOverrideError('openBoardView')

    def participateClick(self, eventID):
        self._printOverrideError('participateClick')

    def orderClick(self, eventID):
        self._printOverrideError('orderClick')

    def techniqueClick(self, eventID):
        self._printOverrideError('techniqueClick')

    def awardClick(self, eventID):
        self._printOverrideError('awardClick')

    def registrationClick(self, eventID):
        self._printOverrideError('registrationClick')

    def serverClick(self, eventID, server):
        self._printOverrideError('serverClick')

    def expand(self, id, value):
        self._printOverrideError('expand')

    def as_setMaintenanceS(self, visible, message1, message2, buttonLabel):
        if self._isDAAPIInited():
            return self.flashObject.as_setMaintenance(visible, message1, message2, buttonLabel)

    def as_setPlayFadeInTweenEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayFadeInTweenEnabled(value)
