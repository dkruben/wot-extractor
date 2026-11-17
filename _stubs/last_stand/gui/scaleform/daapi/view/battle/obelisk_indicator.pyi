# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/obelisk_indicator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from LSObeliskInfoComponent import LSObeliskInfoComponent as LSObeliskInfoComponent, ObeliskInfoStates as ObeliskInfoStates
from last_stand.gui.scaleform.daapi.view.meta.ObeliskMeta import ObeliskMeta as ObeliskMeta
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache

class LSObeliskIndicator(ObeliskMeta):
    __itemsCache: Any
    curObeliskName: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _onStateChange(self, state):
        ...
    def _onObeliskObserved(self, obeliskIntCD):
        ...
