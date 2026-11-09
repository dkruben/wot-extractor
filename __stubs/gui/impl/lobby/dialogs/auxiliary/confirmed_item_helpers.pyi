# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dialogs/auxiliary/confirmed_item_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from enum import IntEnum as IntEnum
from gui.impl.gen.view_models.constants.item_highlight_types import ItemHighlightTypes as ItemHighlightTypes
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from gui.shared.gui_items.gui_item import GUIItem as GUIItem
_HIGHLIGHTS_TYPE_TO_CRITERIA: dict
_OVERLAY_TYPE_TO_CRITERIA: dict

class ConfirmedItemWarningTypes(IntEnum):
    DEPENDS_ON_DEVICES = 1
    PAIR_MODIFICATIONS_WILL_BE_DEMOUNT = 2

class BaseConfirmedItemWarning(object):
    __slots__: tuple
    def getType(self):
        ...

class DependsOnDevicesWarning(BaseConfirmedItemWarning):
    __slots__: tuple
    __devicesName: Any
    def __init__(self, devicesName):
        ...
    def getType(self):
        ...
    def getDevicesName(self):
        ...

class PairModificationsWillBeDemount(BaseConfirmedItemWarning):
    def getType(self):
        ...

def _equipmentPlusCriteria():
    ...
def _equipmentBuiltInCriteria():
    ...
def _optionalDeviceSimpleCriteria():
    ...
def _optionalDeviceTrophyBasicCriteria():
    ...
def _optionalDeviceTrophyUpgradedCriteria():
    ...
def _optionalDeviceModernizedWithLevelCriteria(level=None):
    ...
def getHighlightsTypeByItem(item, typeToCriteria=None):
    ...
def getOverlayTypeByItem(item, typeToCriteria=None):
    ...
