# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/fort_rush_welcome_screen.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from fort_rush.account_helpers.account_settings import setWelcomeScreenSeen as setWelcomeScreenSeen, isWelcomeScreenSeen as isWelcomeScreenSeen
from fort_rush.gui.impl.gen.view_models.views.lobby.fort_rush_welcome_screen_view_model import FortRushWelcomeScreenViewModel as FortRushWelcomeScreenViewModel
from fort_rush.gui.sounds.sound_constants import FORT_RUSH_PROMO_SOUND_SPACE as FORT_RUSH_PROMO_SOUND_SPACE
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from gui.shared import g_eventBus as g_eventBus, events as events
from gui.shared.event_dispatcher import showBrowserOverlayView as showBrowserOverlayView
from gui.sounds.filters import switchVideoOverlaySoundFilter as switchVideoOverlaySoundFilter

class FortRushWelcomeScreenView(ViewImpl):
    LAYOUT_ID: Any
    _COMMON_SOUND_SPACE = FORT_RUSH_PROMO_SOUND_SPACE
    def __init__(self, layoutID=..., *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onViewLoaded(self):
        ...
    def _onClose(self):
        ...
    def _onVideoPlay(self):
        ...
    def _onBrowserClosed(self):
        ...

class FortRushWelcomeScreenViewWindow(WindowImpl):
    def __init__(self, parent=None):
        ...
