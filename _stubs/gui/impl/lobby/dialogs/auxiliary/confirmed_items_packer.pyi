# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dialogs/auxiliary/confirmed_items_packer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.impl.lobby.dialogs.auxiliary.confirmed_item import ConfirmedItem as ConfirmedItem
from gui.impl.lobby.dialogs.auxiliary.confirmed_item_to_upgrade import ConfirmedItemToUpgrade as ConfirmedItemToUpgrade
from gui.shared.gui_items.fitting_item import FittingItem as FittingItem
from typing import Iterable as Iterable, Dict as Dict, Callable as Callable, Set as Set, Tuple as Tuple

class ConfirmedItemsPacker(object):
    _ctx: Any
    def __init__(self, **kwargs):
        ...
    def packItemsType(self, items, typesToCombine=None):
        ...
    def packItems(self, items, filterFunc=None, sortFunction=None):
        ...
    @classmethod
    def _getItemClass(cls):
        ...

class ConfirmedItemsToUpgradePacker(ConfirmedItemsPacker):
    @classmethod
    def _getItemClass(cls):
        ...
