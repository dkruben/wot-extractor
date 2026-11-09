# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/page/comp7_prebattle_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/lobby/page/comp7_prebattle_presenter.py
from __future__ import absolute_import
from gui.impl.lobby.page.prebattle_presenter import PrebattlePresenter
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller
from skeletons.gui.shared import IItemsCache

class Comp7PrebattlePresenter(PrebattlePresenter):
    __comp7Controller = dependency.descriptor(IComp7Controller)
    __itemsCache = dependency.descriptor(IItemsCache)

    def _getEvents(self):
        return super(Comp7PrebattlePresenter, self)._getEvents() + (
         (
          self.__comp7Controller.onQualificationStateUpdated, self._onPrebattleUpdate),
         (
          self.__comp7Controller.onBanUpdated, self._onPrebattleUpdate),
         (
          self.__comp7Controller.onModeConfigChanged, self._onPrebattleUpdate),
         (
          self.__comp7Controller.onOfflineStatusUpdated, self._onPrebattleUpdate),
         (
          self.__itemsCache.onSyncCompleted, self._update))

    def _update(self, _, __):
        self._onPrebattleUpdate()
