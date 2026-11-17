# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from battle_royale.gui.Scaleform.daapi.view.battle.page import BattleRoyalePage as BattleRoyalePage
from battle_royale.gui.Scaleform.daapi.view.battle.player_stats_in_battle import BattleRoyalePlayerStats as BattleRoyalePlayerStats
from battle_royale.gui.Scaleform.daapi.view.battle.radar import RadarButton as RadarButton
from battle_royale.gui.Scaleform.daapi.view.battle.status_notifications.panel import BRStatusNotificationTimerPanel as BRStatusNotificationTimerPanel
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.battle.shared.page import BattlePageBusinessHandler as BattlePageBusinessHandler
from gui.Scaleform.framework import ViewSettings as ViewSettings, ScopeTemplates as ScopeTemplates, ComponentSettings as ComponentSettings
from gui.Scaleform.framework.package_layout import PackageBusinessHandler as PackageBusinessHandler
from gui.Scaleform.genConsts.BATTLE_CONTEXT_MENU_HANDLER_TYPE import BATTLE_CONTEXT_MENU_HANDLER_TYPE as BATTLE_CONTEXT_MENU_HANDLER_TYPE
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES as BATTLE_VIEW_ALIASES
from gui.app_loader import settings as app_settings
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController

class _BattleRoyaleBusinessHandler(PackageBusinessHandler):
    __slots__: tuple
    def __init__(self):
        ...
    def __handleVehConfiguratorEvent(self, event):
        ...

def getContextMenuHandlers():
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getViewSettings(battleRoyaleController=None):
    ...
def getBusinessHandlers():
    ...
