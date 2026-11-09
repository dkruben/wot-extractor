# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/meta_intro_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers import AccountSettings as AccountSettings
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui.impl.gen import R as R
from halloween.gui.halloween_account_settings import AccountSettingsKeys as AccountSettingsKeys
from halloween.gui.impl.gen.view_models.views.lobby.meta_intro_view_model import MetaIntroViewModel as MetaIntroViewModel
from halloween.gui.impl.lobby.base_view import BaseView as BaseView, HWLobbyWindow as HWLobbyWindow
from halloween.gui.sounds import playSound as playSound
from halloween.gui.sounds.sound_constants import META_INTRO_ENTER as META_INTRO_ENTER, META_INTRO_EXIT as META_INTRO_EXIT
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController as IHalloweenArtefactsController
from helpers import dependency as dependency

class MetaIntroView(BaseView):
    __slots__: tuple
    _hwArtefactsCtrl: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def _onClose(self):
        ...

class MetaIntroWindow(HWLobbyWindow):
    def __init__(self, parent=None):
        ...
