# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dog_tags/customization_confirm_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings
from constants import DOG_TAGS_CONFIG as DOG_TAGS_CONFIG
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.dog_tags.customization_confirm_dialog_model import CustomizationConfirmDialogModel as CustomizationConfirmDialogModel
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogBaseView as FullScreenDialogBaseView
from gui.impl.lobby.dog_tags.dog_tag_composer import DogTagComposerLobby as DogTagComposerLobby
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.web import IWebController as IWebController
from account_helpers.dog_tags import DogTags as DogTagsAccountHelper
_logger: Any

class CustomizationConfirmDialog(FullScreenDialogBaseView):
    __slots__: tuple
    _webCtrl: Any
    lobbyContext: Any
    __dogTagsHelper: Any
    __composer: Any
    __backgroundId: Any
    __engravingId: Any
    __additionalData: Any
    __isLocked: Any
    def __init__(self, backgroundId, engravingId):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __onClose(self):
        ...
    def __onConfirm(self):
        ...
    def __onDiscard(self):
        ...
    def _getAdditionalData(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def _finalize(self):
        ...
    def __onServerSettingsChange(self, diff):
        ...
