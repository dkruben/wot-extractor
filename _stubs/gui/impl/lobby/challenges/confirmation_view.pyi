# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/challenges/confirmation_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.price_item_model import PriceItemModel as PriceItemModel
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogBaseView as FullScreenDialogBaseView
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from gui.impl.gen.view_models.views.lobby.challenges.confirmation_model import ConfirmationModel as ConfirmationModel
from shared_utils import first as first
from skeletons.gui.challenges import IChallengesController as IChallengesController
from skeletons.gui.shared import IItemsCache as IItemsCache

class ChallengesConfirmationView(FullScreenDialogBaseView):
    __itemsCache: Any
    __challenges: Any
    __additionalData: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _getCallbacks(self):
        ...
    def _onLoading(self, challengeID, confirmationType, isFree, *args, **kwargs):
        ...
    def _getAdditionalData(self):
        ...
    def __confirm(self):
        ...
    def __cancel(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __setBalance(self, value=None, model=None):
        ...
