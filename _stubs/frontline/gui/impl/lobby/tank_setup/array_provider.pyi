# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/tank_setup/array_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from WeakMixin import WeakMixin as WeakMixin, Tapped as Tapped
from epic_constants import CATEGORIES_ORDER as CATEGORIES_ORDER
from frontline.gui.impl.gen.view_models.views.lobby.components.loadout.battle_ability_slot_model import BattleAbilitySlotModel as BattleAbilitySlotModel
from gui.impl.lobby.tank_setup.array_providers.base import VehicleBaseArrayProvider as VehicleBaseArrayProvider, BaseVehSectionContext as BaseVehSectionContext
from gui.impl.lobby.tank_setup.tank_setup_helper import NONE_ID as NONE_ID
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.artefacts import BattleAbility as BattleAbility
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from helpers.epic_game import searchRankForSlot as searchRankForSlot
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
from frameworks.wulf import Array as Array

class BattleAbilityMixin(WeakMixin, Tapped):
    @classmethod
    def fromBattleAbility(cls, item, **kwargs):
        ...

class BattleAbilityProvider(VehicleBaseArrayProvider):
    __sessionProvider: Any
    __epicMetaGameCtrl: Any
    def createSlot(self, item, ctx):
        ...
    def fillArray(self, array, ctx, itemFilter=None):
        ...
    def getItemViewModel(self):
        ...
    def getItemsList(self):
        ...
    def updateArray(self, array, ctx):
        ...
    def updateSlot(self, model, item, ctx):
        ...
    def _fillStatus(self, model, item, slotID):
        ...
    def _getCriteria(self):
        ...
    def _getEpicSkills(self):
        ...
    @classmethod
    def _getItemTypeID(cls):
        ...
    def _getCategoryRank(self, category):
        ...
