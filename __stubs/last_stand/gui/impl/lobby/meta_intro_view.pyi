# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/meta_intro_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers import AccountSettings as AccountSettings
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui.impl.gen import R as R
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from last_stand.gui.ls_account_settings import AccountSettingsKeys as AccountSettingsKeys
from last_stand.gui.impl.gen.view_models.views.lobby.meta_intro_view_model import MetaIntroViewModel as MetaIntroViewModel
from last_stand.gui.impl.lobby.base_view import BaseView as BaseView
from last_stand.gui.sounds import playSound as playSound
from last_stand.gui.sounds.sound_constants import META_INTRO_ENTER as META_INTRO_ENTER, META_INTRO_EXIT as META_INTRO_EXIT
from last_stand.skeletons.ls_artefacts_controller import ILSArtefactsController as ILSArtefactsController
from helpers import dependency as dependency

class MetaIntroView(BaseView):
    __slots__: tuple
    lsArtifactsCtrl: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _onClose(self):
        ...
    def _onSettingUpdate(self, *_):
        ...

class MetaIntroWindow(LobbyWindow):
    def __init__(self, parent=None):
        ...
