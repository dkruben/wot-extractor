# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/array_providers/consumable.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl.gen.view_models.constants.item_highlight_types import ItemHighlightTypes as ItemHighlightTypes
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.consumable_slot_model import ConsumableSlotModel as ConsumableSlotModel
from gui.impl.lobby.tank_setup.array_providers.base import VehicleBaseArrayProvider as VehicleBaseArrayProvider
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from gui.impl import backport as backport
from gui.impl.gen import R as R
OPEN_TAG = '{whiteSpanish_open}'
CLOSE_TAG = '{whiteSpanish_close}'

class ConsumableDeviceProvider(VehicleBaseArrayProvider):
    __slots__: tuple
    def getItemViewModel(self):
        ...
    def createSlot(self, item, ctx):
        ...
    def __fillDescription(self, model, item):
        ...
    def updateSlot(self, model, item, ctx):
        ...
    def _fillHighlights(self, model, item):
        ...
    def _mayInstall(self, item, slotID=None):
        ...
    @classmethod
    def _getItemTypeID(cls):
        ...
    def _getItemCriteria(self):
        ...
    def _getEquipment(self):
        ...

def formatValueToColorTag(value):
    ...
