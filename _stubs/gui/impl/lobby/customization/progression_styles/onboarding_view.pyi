# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/customization/progression_styles/onboarding_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import IS_CUSTOMIZATION_INTRO_VIEWED as IS_CUSTOMIZATION_INTRO_VIEWED
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags
from functools import partial as partial
from gui.customization.constants import CustomizationModes as CustomizationModes
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.customization.progression_styles.onboarding_view_model import OnboardingViewModel as OnboardingViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from gui.Scaleform.daapi.view.lobby.customization.shared import CustomizationTabs as CustomizationTabs
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from helpers import dependency as dependency
from skeletons.gui.customization import ICustomizationService as ICustomizationService

class OnboardingView(ViewImpl):
    __slots__: tuple
    __customizationService: Any
    __isFirstRun: Any
    __styleCD: Any
    def __init__(self, ctx, layoutID):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onLoading(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onClose(self):
        ...
    def __onGotoStyle(self):
        ...
    @property
    def viewModel(self):
        ...

class OnboardingWindow(LobbyWindow):
    __slots__: tuple
    __blur: Any
    def __init__(self, ctx, parent):
        ...
    def _finalize(self):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def _onCustomizationLoadedCallback(styleCD, service=None):
    ...
