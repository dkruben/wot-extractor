# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/shared/event_dispatcher.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from fort_rush.skeletons.battle_controller import IFortRushBattleController as IFortRushBattleController
from frameworks.wulf import WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.impl.pub.notification_commands import WindowNotificationCommand as WindowNotificationCommand
from gui.shared.event_dispatcher import showBrowserOverlayView as showBrowserOverlayView
from helpers import dependency as dependency
from skeletons.gui.impl import INotificationWindowController as INotificationWindowController
FR_INFO_PAGE = 'frEventInfoPage'

# decorador original: @dependency.replace_none_kwargs(...)
def isCustomizationHangarDisabled(ctrl=None):
    ...
def showFortRushBattleResultView(arenaUniqueID):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def showProgressionView(ctrl=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def showWelcomeScreen(ctrl=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def showAwardWindow(rewardData, notificationsMgr=None):
    ...
def showFortRushInfoPage():
    ...
