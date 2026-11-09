# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/hangar/presenters/comp7_light_loadout_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/impl/lobby/hangar/presenters/comp7_light_loadout_presenter.py
from __future__ import absolute_import
import typing
from gui.Scaleform.lobby_entry import getLobbyStateMachine
from gui.impl.gen import R
from gui.impl.lobby.hangar.presenters.consumables_presenter import ConsumablesPresenter
from gui.impl.lobby.hangar.presenters.equipments_presenter import EquipmentsPresenter
from gui.impl.lobby.hangar.presenters.instructions_presenter import InstructionsPresenter
from gui.impl.lobby.hangar.presenters.loadout_presenter import LoadoutPresenter, _LoadoutStatesObserver
from gui.impl.lobby.hangar.presenters.shells_presenter import ShellsPresenter
if typing.TYPE_CHECKING:
    from gui.impl.pub.view_component import ViewComponent

class _Comp7LightLoadoutStatesObserver(_LoadoutStatesObserver):

    @property
    def _stateID(self):
        from comp7_light.gui.impl.lobby.hangar.states import Comp7LightLoadoutState
        return Comp7LightLoadoutState.STATE_ID


class Comp7LightLoadoutPresenter(LoadoutPresenter):
    _STATES_OBSERVER = _Comp7LightLoadoutStatesObserver

    def _getChildComponents(self):
        hangar = R.aliases.hangar.shared
        return {(hangar.Equipments()): (lambda : EquipmentsPresenter(self._vehInteractingItem)), 
           (hangar.Instructions()): (lambda : InstructionsPresenter(self._vehInteractingItem)), 
           (hangar.Shells()): (lambda : Comp7LightShellsPresenter(self._vehInteractingItem)), 
           (hangar.Consumables()): (lambda : ConsumablesPresenter(self._vehInteractingItem))}


class Comp7LightShellsPresenter(ShellsPresenter):

    @property
    def isShellState(self):
        from comp7_light.gui.impl.lobby.hangar.states import Comp7LightShellsLoadoutState
        lsm = getLobbyStateMachine()
        return lsm.getStateByCls(Comp7LightShellsLoadoutState).isEntered()
