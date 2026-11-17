# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/matchmaker/active_test_confirm_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.matchmaker.active_test_confirm_view_model import ActiveTestConfirmViewModel as ActiveTestConfirmViewModel
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogView as FullScreenDialogView
from gui.shared import g_eventBus as g_eventBus, events as events
from helpers import dependency as dependency
from skeletons.connection_mgr import IConnectionManager as IConnectionManager

class ActiveTestConfirmView(FullScreenDialogView):
    __connectionMgr: Any
    __startTime: Any
    __finishTime: Any
    __link: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onInventoryResync(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __onOpenPortalClicked(self):
        ...
