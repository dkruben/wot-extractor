# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/sub_views/base_equipment_setup.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel as BaseSetupModel
from gui.impl.lobby.tank_setup.sub_views.deal_base_setup import DealBaseSetupSubView as DealBaseSetupSubView
from gui.shared.event_dispatcher import showModuleInfo as showModuleInfo
from helpers import dependency as dependency
from skeletons.gui.impl import IGuiLoader as IGuiLoader

class BaseEquipmentSetupSubView(DealBaseSetupSubView):
    __slots__: tuple
    __gui: Any
    def _addListeners(self):
        ...
    def _onSelectItem(self, args):
        ...
    def _selectItem(self, slotID, item):
        ...
    def _onSwapSlots(self, actionType, args):
        ...
    def _swapSlots(self, currentSlotID, slotID, actionType):
        ...
    def _onRevertItem(self, args):
        ...
    def _onShowItemInfo(self, args):
        ...
    def __confirmDialogInShowing(self):
        ...
