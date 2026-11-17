# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/intro_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.common.battle_royale.br_helpers import currentHangarIsBattleRoyale as currentHangarIsBattleRoyale
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.common.intro_slide_model import IntroSlideModel as IntroSlideModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController, IHangarSpaceSwitchController as IHangarSpaceSwitchController
from battle_royale.gui.impl.gen.view_models.views.lobby.views.intro_view_model import IntroViewModel as IntroViewModel

class IntroView(ViewImpl, IGlobalListener):
    __battleRoyaleController: Any
    __spaceSwitchController: Any
    __isPageWasShow: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __onVisibleRouteChanged(self, routeInfo):
        ...
    def __onClose(self):
        ...
    def __onVideo(self):
        ...
    def __onSpaceUpdated(self):
        ...
    def __updateViewModel(self):
        ...
    @staticmethod
    def __createSlideModel(icon, title, description):
        ...

class IntroWindow(LobbyWindow):
    __slots__: tuple
    def __init__(self, ctx, parent):
        ...
