# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/instructions_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import SoundGroups as SoundGroups
from gui.impl.gen.view_models.views.lobby.loadout.instructions.instructions_model import InstructionsModel as InstructionsModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel as BaseSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.lobby.hangar.presenters.loadout_presenter_base import LoadoutPresenterBase as LoadoutPresenterBase, LoadoutEntityProvider as LoadoutEntityProvider
from gui.impl.lobby.tank_setup.array_providers.base import BaseVehSectionContext as BaseVehSectionContext
from gui.impl.lobby.tank_setup.array_providers.battle_booster import OptDeviceBattleBoosterProvider as OptDeviceBattleBoosterProvider, CrewBattleBoosterProvider as CrewBattleBoosterProvider
from gui.impl.lobby.tank_setup.configurations.battle_booster import BattleBoosterTabs as BattleBoosterTabs
from gui.impl.lobby.tank_setup.interactors.battle_booster import BattleBoosterInteractor as BattleBoosterInteractor
from gui.impl.lobby.tank_setup.tank_setup_sounds import TankSetupSoundEvents as TankSetupSoundEvents
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.game_control import IWalletController as IWalletController
from gui.impl.lobby.tank_setup.interactors.base import InteractingItem as InteractingItem

# base nao representavel no stub: LoadoutPresenterBase[...]
class InstructionsPresenter:
    __wallet: Any
    _sectionName: Any
    _guiItemType: Any
    _provider: Any
    def __init__(self, interactingItem):
        ...
    def createSlotActions(self):
        ...
    def _getEvents(self):
        ...
    def _createProvider(self, vehInteractingItem):
        ...
    def _getCallbacks(self):
        ...
    def _updateInteractor(self, item=None):
        ...
    def _updateModel(self, recreate=True):
        ...
    def _onRevertItem(self, args):
        ...
    def __onAdd(self, args):
        ...
