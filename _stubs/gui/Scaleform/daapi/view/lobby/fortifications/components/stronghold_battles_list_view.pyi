# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/fortifications/components/stronghold_battles_list_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from adisp import adisp_process as adisp_process
from frameworks.wulf import WindowLayer as WindowLayer
from helpers import dependency as dependency
from skeletons.gui.game_control import IBrowserController as IBrowserController
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.shared import events as events
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.clans.clan_helpers import getStrongholdBattlesListUrl as getStrongholdBattlesListUrl
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.locale.FORTIFICATIONS import FORTIFICATIONS as FORTIFICATIONS
from gui.Scaleform.daapi.view.lobby.strongholds.web_handlers import createStrongholdsWebHandlers as createStrongholdsWebHandlers
from gui.Scaleform.daapi.view.meta.StrongholdBattlesListViewMeta import StrongholdBattlesListViewMeta as StrongholdBattlesListViewMeta
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA as POP_UP_CRITERIA
from shared_utils import BoundMethodWeakref as BoundMethodWeakref

class StrongholdBattlesListView(StrongholdBattlesListViewMeta):
    browserCtrl: Any
    childBrowsers: Any
    __browserId: Any
    __browserCreated: Any
    __hasFocus: Any
    __browser: Any
    def __init__(self):
        ...
    def addChildBrowserAlias(self, browserAlias):
        ...
    def viewSize(self, width, height):
        ...
    def updateBrowser(self):
        ...
    def onFocusChange(self, hasFocus):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    # decorador original: @adisp_process
    def __loadBrowser(self, width, height):
        ...
    def __showBrowser(self):
        ...
    def __updateSkipEscape(self):
        ...
