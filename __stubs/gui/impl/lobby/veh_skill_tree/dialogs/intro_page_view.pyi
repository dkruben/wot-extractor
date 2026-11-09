# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/veh_skill_tree/dialogs/intro_page_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.common.base_intro_view_model import BaseIntroViewModel as BaseIntroViewModel
from gui.impl.gen.view_models.views.lobby.common.intro_slide_model import IntroSlideModel as IntroSlideModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
_IMAGES = R.images.gui.maps.icons.skillTree.introPage
_TEXTS = R.strings.veh_skill_tree.intro

class IntroPageView(ViewImpl):
    __itemsCache: Any
    def __init__(self, layoutID, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self):
        ...
    @staticmethod
    def __createSlideModel(slideName):
        ...

class IntroPageWindow(LobbyNotificationWindow):
    __blur: Any
    def __init__(self, parent=None):
        ...
    def _finalize(self):
        ...
