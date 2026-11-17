# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/promo_window_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers import AccountSettings as AccountSettings
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags, ViewFlags as ViewFlags, WindowLayer as WindowLayer
from gui.impl.gen import R as R
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from last_stand.gui.impl.gen.view_models.views.lobby.promo_window_view_model import PromoWindowViewModel as PromoWindowViewModel
from last_stand.gui.impl.lobby.base_view import BaseView as BaseView
from last_stand.gui.ls_account_settings import AccountSettingsKeys as AccountSettingsKeys
from helpers import dependency as dependency
from last_stand.skeletons.ls_artefacts_controller import ILSArtefactsController as ILSArtefactsController
from last_stand.skeletons.ls_controller import ILSController as ILSController

class PromoWindowView(BaseView):
    lsArtifactsCtrl: Any
    __lsCtrl: Any
    __slots__: tuple
    layoutID: Any
    def __init__(self, layoutID=None):
        ...
    @property
    def isHiddenMenu(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def _onClose(self):
        ...

class PromoWindow(LobbyNotificationWindow):
    def __init__(self, layoutID, parent=None):
        ...
