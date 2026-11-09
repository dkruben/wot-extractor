# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/components/gun_installation_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import DEFAULT_GUN_INSTALLATION_INDEX as DEFAULT_GUN_INSTALLATION_INDEX
from items.components import shared_components as shared_components
from items.components import component_constants as component_constants
from items.vehicle_items import Gun as Gun

class GunInstallationSlot(object):
    __slots__: tuple
    installationIndex: Any
    gun: Any
    __objectSlots: Any
    def __init__(self, installationIndex, gun):
        ...
    def __deepcopy__(self, memodict=...):
        ...
    def __repr__(self):
        ...
    @classmethod
    def isMainInstallationIndex(cls, installationIndex):
        ...
    @classmethod
    def getPartSlotNameByIndex(cls, installationIndex):
        ...
    @property
    def partSlotName(self):
        ...
    @property
    def objectSlots(self):
        ...
    def getSlotPrefabs(self, styleName=None):
        ...
    def isMainInstallation(self):
        ...
    def __collectObjectSlots(self):
        ...
