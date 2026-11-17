# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/sub_views/shell_setup.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from functools import partial as partial
from gui.shared import sound_helpers as sound_helpers
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel as BaseSetupModel
from gui.impl.lobby.tank_setup.configurations.shell import ShellTabsController as ShellTabsController, ShellDealPanel as ShellDealPanel
from gui.impl.lobby.tank_setup.sub_views.deal_base_setup import DealBaseSetupSubView as DealBaseSetupSubView
from gui.shared.items_parameters import getShellsLoadSize as getShellsLoadSize
from gui.shared.event_dispatcher import showModuleInfo as showModuleInfo

class ShellSetupSubView(DealBaseSetupSubView):
    __slots__: tuple
    def updateSlots(self, slotID, fullUpdate=True, updateData=True):
        ...
    def _createTabsController(self):
        ...
    def _getDealPanel(self):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def _updateSlots(self, fullUpdate=True, updateData=True):
        ...
    def __onItemsSyncCompleted(self, *_):
        ...
    def __onSwapSlots(self, actionType, args):
        ...
    def __onShowItemInfo(self, args):
        ...
    def __onShellUpdate(self, args):
        ...
