# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/anomalies_watcher_mixin.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/anomalies_watcher_mixin.py
from __future__ import absolute_import
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class AnomaliesWatcherMixin(object):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, *args, **kwargs):
        super(AnomaliesWatcherMixin, self).__init__(*args, **kwargs)
        self.needToShow = False
        self.__isDisplayAllowed = True

    def updateVisibility(self):
        self.as_setVisibleS(self.__isDisplayAllowed and self.needToShow)

    @property
    def isDisplayAllowed(self):
        return self.__isDisplayAllowed

    @property
    def hwBattleGuiCtrl(self):
        return self.sessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.HW_BATTLE_GUI_CTRL)

    def _populate(self):
        super(AnomaliesWatcherMixin, self)._populate()
        hwBattleGuiCtrl = self.hwBattleGuiCtrl
        if hwBattleGuiCtrl:
            hwBattleGuiCtrl.onChangeAnomaliesViewVisibility += self.__onChangeAnomaliesViewVisibility

    def _dispose(self):
        hwBattleGuiCtrl = self.hwBattleGuiCtrl
        if hwBattleGuiCtrl:
            hwBattleGuiCtrl.onChangeAnomaliesViewVisibility -= self.__onChangeAnomaliesViewVisibility
        super(AnomaliesWatcherMixin, self)._dispose()

    def __onChangeAnomaliesViewVisibility(self, isVisible):
        self.__isDisplayAllowed = not isVisible
        self.updateVisibility()
