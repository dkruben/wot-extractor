# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/presenters/loadout_panel_presenter/loadout_panel_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/presenters/loadout_panel_presenter/loadout_panel_presenter.py
from __future__ import absolute_import
from gui.impl.pub.view_component import ViewComponent
from gui.impl.pub.view_impl import TViewModel
from gui.impl.gen import R
from battle_royale.gui.impl.lobby.views.presenters.loadout_panel_presenter.battle_royale_loadout_presenter import BattleRoyaleLoadoutPresenter
from battle_royale.gui.impl.lobby.views.presenters.loadout_panel_presenter.commander_presenter import CommanderPresenter
from CurrentVehicle import g_currentVehicle
from gui.Scaleform.daapi.view.common.battle_royale.br_helpers import isIncorrectVehicle

class LoadoutContainerPresenter(ViewComponent[TViewModel]):
    _BATTLE_ROYALE_LOADOUT = R.aliases.battle_royale.loadoutPanelContainer
    _CHILDREN = {(_BATTLE_ROYALE_LOADOUT.Loadout()): BattleRoyaleLoadoutPresenter, 
       (_BATTLE_ROYALE_LOADOUT.Commander()): CommanderPresenter}

    def _getEvents(self):
        return (
         (
          g_currentVehicle.onChanged, self.__onCurrentVehicleChanged),)

    def _onLoading(self, *args, **kwargs):
        self.__onCurrentVehicleChanged()
        super(LoadoutContainerPresenter, self)._onLoading(*args, **kwargs)

    def __onCurrentVehicleChanged(self):
        if not g_currentVehicle.isPresent():
            return
        vehicle = g_currentVehicle.item
        if isIncorrectVehicle(vehicle):
            return
        self._addChild(self._BATTLE_ROYALE_LOADOUT.Commander(), vehicle)
        self._addChild(self._BATTLE_ROYALE_LOADOUT.Loadout(), vehicle)

    def _addChild(self, posId, vehicle):
        uid = self._childrenUidByPosition.get(posId)
        child = self._childrenByUid.get(uid) or self._getChild(posId)
        if not child:
            child = self._CHILDREN[posId]()
            self._registerChild(posId, child)
        child.update(vehicle)
