# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_pass/intro_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers.settings_core.settings_constants import BattlePassStorageKeys as BattlePassStorageKeys
from frameworks.wulf import WindowFlags as WindowFlags, ViewSettings as ViewSettings
from gui.battle_pass.battle_pass_helpers import getIntroSlidesNames as getIntroSlidesNames
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_pass.battle_pass_intro_view_model import BattlePassIntroViewModel as BattlePassIntroViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import IBattlePassController as IBattlePassController

class IntroPresenter(ViewImpl):
    __battlePass: Any
    __settingsCore: Any
    __callback: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, callback, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __updateViewModel(self):
        ...
    def __setIntroShown(self):
        ...

class IntroWindow(LobbyWindow):
    __slots__: tuple
    def __init__(self, callback=None, parent=None):
        ...
