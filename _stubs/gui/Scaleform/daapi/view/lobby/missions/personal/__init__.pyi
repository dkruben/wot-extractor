# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/missions/personal/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from operator import methodcaller as methodcaller
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.missions.personal.personal_missions_first_entry_award_view import PersonalMissionFirstEntryAwardView as PersonalMissionFirstEntryAwardView
from gui.Scaleform.daapi.view.lobby.missions.personal.tank_girls_popover import TankgirlsPopover as TankgirlsPopover
from gui.Scaleform.framework import ViewSettings as ViewSettings, ScopeTemplates as ScopeTemplates, GroupedViewSettings as GroupedViewSettings, ComponentSettings as ComponentSettings
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.framework.package_layout import PackageBusinessHandler as PackageBusinessHandler
from gui.Scaleform.genConsts.PERSONAL_MISSIONS_ALIASES import PERSONAL_MISSIONS_ALIASES as PERSONAL_MISSIONS_ALIASES
from gui.app_loader import settings as app_settings
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showPersonalMissionCampaignSelectorWindow as showPersonalMissionCampaignSelectorWindow
from gui.shared.events import LoadViewEvent as LoadViewEvent

class PersonalMissionsPackageBusinessHandler(PackageBusinessHandler):
    def __init__(self):
        ...
    def loadAwardsView(self, event):
        ...
    def loadPersonalMissionsView(self, event):
        ...

def getStateMachineRegistrators():
    ...
def getContextMenuHandlers():
    ...
def getViewSettings():
    ...
def getBusinessHandlers():
    ...
