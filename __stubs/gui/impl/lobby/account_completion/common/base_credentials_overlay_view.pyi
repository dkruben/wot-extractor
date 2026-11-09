# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/account_completion/common/base_credentials_overlay_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import EMAIL_CONFIRMATION_QUEST_ID as EMAIL_CONFIRMATION_QUEST_ID
from gui.impl.backport.backport_tooltip import createBackportTooltipContent as createBackportTooltipContent
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.account_completion.add_credentials_model import AddCredentialsModel as AddCredentialsModel
from gui.impl.gen.view_models.views.lobby.account_completion.tooltips.tooltip_constants import TooltipConstants as TooltipConstants
from gui.impl.lobby.account_completion.common import errors as errors
from gui.impl.lobby.account_completion.common.base_wgnp_overlay_view import BaseWGNPOverlayView as BaseWGNPOverlayView
from gui.impl.lobby.account_completion.common.field_presenters import EmailPresenter as EmailPresenter
from gui.impl.lobby.account_completion.utils.common import fillRewards as fillRewards, DISABLE_BUTTON_TIME as DISABLE_BUTTON_TIME
from helpers import dependency as dependency
from skeletons.gui.server_events import IEventsCache as IEventsCache
_WARNING_TIMEOUT = DISABLE_BUTTON_TIME

class BaseCredentialsOverlayView(BaseWGNPOverlayView):
    __slots__: tuple
    _REWARDS_TITLE: Any
    _eventsCache: Any
    _LAYOUT_DYN_ACCESSOR = R.views.lobby.account_completion.AddCredentialsView
    _VIEW_MODEL_CLASS = AddCredentialsModel
    _email: Any
    _tooltipItems: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def activate(self, initialEmail='', emailError='', *args, **kwargs):
        ...
    def deactivate(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _doFinalize(self):
        ...
    def _inputValueChangeHandler(self):
        ...
    def _inputFocusLostHandler(self):
        ...
    def _updateConfirmButtonAvailability(self):
        ...
    def _fillRewards(self, model):
        ...
    def _onSyncCompleted(self, *args):
        ...
    def _handleError(self, response):
        ...
    def _getEmailErrorMessage(self, response):
        ...
