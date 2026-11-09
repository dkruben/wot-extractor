# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/missions/regular/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.missions.regular.missions_tab_bar import MissionsTabBarComponent as MissionsTabBarComponent
from gui.Scaleform.framework import ComponentSettings as ComponentSettings, GroupedViewSettings as GroupedViewSettings, ScopeTemplates as ScopeTemplates, ViewSettings as ViewSettings
from gui.Scaleform.framework.package_layout import PackageBusinessHandler as PackageBusinessHandler
from gui.Scaleform.genConsts.EVENTBOARDS_ALIASES import EVENTBOARDS_ALIASES as EVENTBOARDS_ALIASES
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES as QUESTS_ALIASES
from gui.app_loader import settings as app_settings
from gui.impl.lobby.mapbox.mapbox_progression_view import MapboxProgressionsComponent as MapboxProgressionsComponent
from gui.impl.lobby.battle_matters.battle_matters_main_view import BattleMattersMissionComponent as BattleMattersMissionComponent
from gui.impl.lobby.live_ops_web_events.browser_view import LiveOpsWebEventsInjectView as LiveOpsWebEventsInjectView
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE

class MissionsPackageBusinessHandler(PackageBusinessHandler):
    def __init__(self):
        ...
    def __loadMissionsPageOrUpdateCurrentTab(self, event):
        ...

def getStateMachineRegistrators():
    ...
def getContextMenuHandlers():
    ...
def getViewSettings():
    ...
def getBusinessHandlers():
    ...
