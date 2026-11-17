# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prestige/prestige_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from collections import namedtuple as namedtuple
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import GUI_START_BEHAVIOR as GUI_START_BEHAVIOR
from account_helpers.settings_core.settings_constants import GuiSettingsBehavior as GuiSettingsBehavior
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.impl.gen.view_models.views.lobby.prestige.prestige_emblem_model import PrestigeLevelGrade as PrestigeLevelGrade
from gui.impl.pub.notification_commands import WindowNotificationCommand as WindowNotificationCommand, NotificationEvent as NotificationEvent, EventNotificationCommand as EventNotificationCommand
from helpers import dependency as dependency
from prestige_system.prestige_common import PrestigeGrade as PrestigeGrade
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.impl import INotificationWindowController as INotificationWindowController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Tuple as Tuple, List as List, Dict as Dict, Set as Set
from prestige_system.prestige_milestones_common import PrestigeLevelType as PrestigeLevelType, MilestonesType as MilestonesType
from gui.impl.gen.view_models.views.lobby.prestige.prestige_emblem_model import PrestigeEmblemModel as PrestigeEmblemModel
_logger: Any
PrestigeVehiclesDossiersCut: Any
_MIN_SUB_GRADE_NUMBER = 1
_MAX_SUB_GRADE_NUMBER = 4
_INVALID_GRADE_NUMBER = -1
_COMPLEX_GRADES: tuple
_SIMPLE_GRADES: tuple
_gradeIDtoGradeUIMap: Any
EMPTY_GRADE_ID = 0
MAX_GRADE_ID: Any
DEFAULT_PRESTIGE: Any

def mapGradeIDToUI(gradeID):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getVehiclePrestigeMap(databaseID=None, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getVehiclePrestige(vehCD, databaseID=None, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getCurrentProgress(vehCD, currentLevel, remainingPts, lobbyContext=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getVehicleAchievedMilestones(vehCD, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def prestigePointsToXP(points, lobbyContext=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def hasVehiclePrestige(vehCD, checkElite=False, lobbyContext=None, itemsCache=None):
    ...
def getCurrentGrade(currentLvl, vehCD):
    ...
def getNextGradeLevel(currentLevel, vehCD):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getSortedGrades(vehCD, onlyMain=False, lobbyContext=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getMilestones(vehCD, lobbyContext=None):
    ...
def fillPrestigeEmblemModel(model, level, vehCD):
    ...
def needShowPrestigeRewardWindow(vehCD, oldLvl, newLvl):
    ...
def needShowPrestigeMilestonesRewardWindow(vehCD, level):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def showPrestigeVehicleStats(vehIntCD, lobbyContext=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def showPrestigeRewardWindow(vehIntCD, level, notificationMgr=None):
    ...
def showPrestigeMilestoneAchivedWindow(vehCD, level):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def openRewardScreens(vehCD, level, showRarityAnimation=False, attachment=None, notificationMgr=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def showPrestigeOnboardingWindow(notificationMgr=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isOnboardingViewed(settingsCore=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def setOnboardingViewed(settingsCore=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isFirstEntryNotificationShown(settingsCore=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def setFirstEntryNotificationShown(settingsCore=None):
    ...
