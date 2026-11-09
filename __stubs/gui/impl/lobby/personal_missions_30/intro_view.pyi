# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/personal_missions_30/intro_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import SoundGroups as SoundGroups
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.personal_missions_30.intro_screen_model import IntroScreenModel as IntroScreenModel
from gui.impl.lobby.personal_missions_30.personal_mission_constants import IntroKeys as IntroKeys
from gui.impl.lobby.personal_missions_30.views_helpers import setVideoOverlayOff as setVideoOverlayOff, setVideoOverlayOn as setVideoOverlayOn
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.impl import IGuiLoader as IGuiLoader

class IntroView(ViewImpl):
    videoKey: Any
    operationID: Any
    def __init__(self, layoutID, videoKey=None, operationID=None):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...

class IntroViewWindow(WindowImpl):
    settingsCore: Any
    gui: Any
    introKey = None
    def __init__(self, operationID=None):
        ...

class MainIntroViewWindow(IntroViewWindow):
    introKey: Any
    def __init__(self):
        ...

class OperationIntroViewWindow(IntroViewWindow):
    introKey: Any
    def __init__(self, operationID):
        ...
