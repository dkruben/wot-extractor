# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/mode_selector/items/spec_mode_selector_item.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import operator as operator
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.mode_selector.items.base_item import ModeSelectorLegacyItem as ModeSelectorLegacyItem
from gui.prb_control.entities.battle_session.legacy.requester import AutoInvitesRequester as AutoInvitesRequester
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.impl import IGuiLoader as IGuiLoader

class SpecModeSelectorItem(ModeSelectorLegacyItem):
    __slots__: tuple
    __guiLoader: Any
    __requester: Any
    def handleClick(self):
        ...
    def _getIsDisabled(self):
        ...
    def _onInitializing(self):
        ...
    def _onDisposing(self):
        ...
    def __onListReceived(self, sessions):
        ...
