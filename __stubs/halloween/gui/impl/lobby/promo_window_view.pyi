# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/promo_window_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers import AccountSettings as AccountSettings
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags, ViewFlags as ViewFlags, WindowLayer as WindowLayer
from gui.impl.gen import R as R
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from halloween.gui.impl.gen.view_models.views.lobby.promo_window_view_model import PromoWindowViewModel as PromoWindowViewModel
from halloween.gui.impl.lobby.base_view import BaseView as BaseView
from halloween.gui.halloween_account_settings import AccountSettingsKeys as AccountSettingsKeys
from halloween.uilogging.loggers import HWMetricsLogger as HWMetricsLogger
from halloween.uilogging.logging_constants import HWLogKeys as HWLogKeys, HWLogActions as HWLogActions
from helpers import dependency as dependency, int2roman as int2roman
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController as IHalloweenArtefactsController
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController

class PromoWindowView(BaseView):
    __hwArtefactsCtrl: Any
    __halloweenCtrl: Any
    __slots__: tuple
    layoutID: Any
    __uiLogger: Any
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
    def _finalize(self):
        ...

class PromoWindow(LobbyNotificationWindow):
    def __init__(self, layoutID, parent=None):
        ...
