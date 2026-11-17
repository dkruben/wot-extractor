# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dialogs/auxiliary/confirmed_item_to_upgrade.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl.lobby.dialogs.auxiliary.confirmed_item import ConfirmedItem as ConfirmedItem, ConfirmedArtefact as ConfirmedArtefact, ConfirmedOptDevice as ConfirmedOptDevice
from gui.impl.lobby.dialogs.auxiliary.confirmed_item_helpers import getOverlayTypeByItem as getOverlayTypeByItem
from gui.impl.gen.view_models.constants.item_highlight_types import ItemHighlightTypes as ItemHighlightTypes
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA

class ConfirmedItemToUpgrade(ConfirmedItem):
    @classmethod
    def createFromGUIItem(cls, item, ctx=None):
        ...

class ConfirmedArtefactToUpgrade(ConfirmedArtefact):
    @classmethod
    def createFromGUIItem(cls, item, ctx=None):
        ...

class ConfirmedOptDeviceToUpgrade(ConfirmedOptDevice):
    def getOverlayType(self):
        ...
    @classmethod
    def createFromGUIItem(cls, item, ctx=None):
        ...
    @staticmethod
    def __getOptDeviceCriteria():
        ...
