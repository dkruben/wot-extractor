# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/array_providers/battle_booster.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.impl.gen.view_models.constants.item_highlight_types import ItemHighlightTypes as ItemHighlightTypes
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_slot_model import BaseSlotModel as BaseSlotModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.battle_booster_slot_model import BattleBoosterSlotModel as BattleBoosterSlotModel
from gui.impl.lobby.tank_setup.array_providers.base import VehicleBaseArrayProvider as VehicleBaseArrayProvider
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from web.web_client_api.shop.formatters import formatValueToColorTag as formatValueToColorTag

class BaseBattleBoosterProvider(VehicleBaseArrayProvider):
    __slots__: tuple
    def getItemViewModel(self):
        ...
    def createSlot(self, item, ctx):
        ...
    def updateSlot(self, model, item, ctx):
        ...
    def _fillHighlights(self, model, item):
        ...
    def _fillStatus(self, model, item, slotID):
        ...
    def _fillDescription(self, model, item):
        ...
    @classmethod
    def _getItemTypeID(cls):
        ...
    def _getEquipment(self):
        ...
    def _getItemSortKey(self, item, ctx):
        ...
    def _getInstaledBoosterSet(self):
        ...

class OptDeviceBattleBoosterProvider(BaseBattleBoosterProvider):
    __slots__: tuple
    def _getItemCriteria(self):
        ...
    def _fillDescription(self, model, item):
        ...

class CrewBattleBoosterProvider(BaseBattleBoosterProvider):
    __slots__: tuple
    def _getItemCriteria(self):
        ...
    def _fillHighlights(self, model, item):
        ...
    def _fillDescription(self, model, item):
        ...
