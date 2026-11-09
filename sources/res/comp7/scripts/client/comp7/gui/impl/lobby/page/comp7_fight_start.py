# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/page/comp7_fight_start.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/lobby/page/comp7_fight_start.py
from __future__ import absolute_import
from gui.impl.lobby.page.fight_start import FightStartPresenter
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller

class Comp7FightStartPresenter(FightStartPresenter):
    __comp7Controller = dependency.descriptor(IComp7Controller)

    def _getEvents(self):
        return super(Comp7FightStartPresenter, self)._getEvents() + (
         (
          self.__comp7Controller.onQualificationStateUpdated, self._onFightButtonUpdate),
         (
          self.__comp7Controller.onBanUpdated, self._onFightButtonUpdate),
         (
          self.__comp7Controller.onModeConfigChanged, self._onFightButtonUpdate),
         (
          self.__comp7Controller.onOfflineStatusUpdated, self._onFightButtonUpdate))
