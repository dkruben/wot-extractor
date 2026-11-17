# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/tank_setup/interactor.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from BWUtil import AsyncReturn as AsyncReturn
from adisp import adisp_process as adisp_process
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel as BaseSetupModel
from frontline.gui.impl.gen.view_models.views.lobby.views.frontline_const import FrontlineConst as FrontlineConst
from gui.impl.lobby.tank_setup.interactors.base import BaseAutoRenewal as BaseAutoRenewal
from gui.impl.lobby.tank_setup.interactors.base_equipment import BaseEquipmentInteractor as BaseEquipmentInteractor
from gui.shared.event_dispatcher import showFrontlineConfirmDialog as showFrontlineConfirmDialog
from gui.shared.gui_items.items_actions import factory as ActionsFactory
from helpers import dependency as dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
from wg_async import wg_await as wg_await, wg_async as wg_async, await_callback as await_callback
from frontline.gui.frontline_helpers import becomeNonPlayerState as becomeNonPlayerState

class ReservesAutoRenewal(BaseAutoRenewal):
    __slots__: tuple
    def getValue(self):
        ...
    # decorador original: @adisp_process
    def processVehicleAutoRenewal(self, callback):
        ...

class FrontlineInteractor(BaseEquipmentInteractor):
    __slots__: tuple
    __epicController: Any
    _checkboxState: Any
    _playerLayout: Any
    def __init__(self, vehItem):
        ...
    def getName(self):
        ...
    def getInstalledLayout(self):
        ...
    def getCurrentLayout(self):
        ...
    def getSetupLayout(self):
        ...
    def getCheckboxState(self):
        ...
    def applyAutoRenewal(self, callback):
        ...
    def revert(self):
        ...
    def updateFrom(self, vehicle, onlyInstalled=True):
        ...
    def getPendingPurchaseSkillIds(self):
        ...
    # decorador original: @adisp_process
    def confirm(self, callback, skipDialog=True):
        ...
    # decorador original: @wg_async
    def applyQuit(self, callback, skipApplyAutoRenewal):
        ...
    def setCheckboxState(self, state):
        ...
    # decorador original: @wg_async
    def showExitConfirmDialog(self):
        ...
    def getChangedList(self):
        ...
    def _createAutoRenewal(self):
        ...
