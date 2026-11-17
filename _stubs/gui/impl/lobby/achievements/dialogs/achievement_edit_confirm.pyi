# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/achievements/dialogs/achievement_edit_confirm.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from BWUtil import AsyncReturn as AsyncReturn
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import Configs as Configs
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.dialogs.dialogs import showSingleDialogWithResultData as showSingleDialogWithResultData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.achievements.dialogs.edit_confirm_model import EditConfirmModel as EditConfirmModel, DialogType as DialogType
from gui.impl.lobby.achievements.profile_utils import isLayoutEnabled as isLayoutEnabled, isSummaryEnabled as isSummaryEnabled
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogView as FullScreenDialogView
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from helpers import dependency as dependency, server_settings as server_settings
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from wg_async import wg_async as wg_async, wg_await as wg_await
from typing import Dict as Dict
from frameworks.wulf import Window as Window

class EditConfirm(FullScreenDialogView):
    __slots__: tuple
    __lobbyContext: Any
    __dialogType: Any
    __additionalData: Any
    def __init__(self, dialogType):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _addListeners(self):
        ...
    def _getEvents(self):
        ...
    def _removeListeners(self):
        ...
    def _setBaseParams(self, model):
        ...
    def _getAdditionalData(self):
        ...
    def __onCancelAction(self):
        ...
    # decorador original: @server_settings.serverSettingsChangeListener(...)
    def __onServerSettingsChanged(self, diff):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __showErrorState(self, model=None):
        ...

# decorador original: @wg_async
def showDialog(dialogType, parent):
    ...
