# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/presenters/battle_royale_platoon_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/presenters/battle_royale_platoon_presenter.py
from __future__ import absolute_import
from skeletons.gui.game_control import IBattleRoyaleController
from gui.impl.lobby.page.platoon_presenter import PlatoonPresenter
from helpers import dependency

class BattleRoyalePlatoonPresenter(PlatoonPresenter):
    __battleRoyaleController = dependency.descriptor(IBattleRoyaleController)

    def _getEvents(self):
        return super(BattleRoyalePlatoonPresenter, self)._getEvents() + (
         (
          self.__battleRoyaleController.onPrimeTimeStatusUpdated, self.__update),)

    def __update(self, *_):
        self._onUpdatePlatoon()
