# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dialogs/research_confirm.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.research_confirm_dialog_view_model import ResearchConfirmDialogViewModel as ResearchConfirmDialogViewModel
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogBaseView as FullScreenDialogBaseView
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache

class ResearchConfirmDialogWindow(FullScreenDialogBaseView):
    __itemsCache: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, researchedItemsText, xp, freeXP, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _onAcceptClick(self):
        ...
    def _onCancelClick(self):
        ...
