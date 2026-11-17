# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/comp7_helpers/comp7_gui_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import GUI_START_BEHAVIOR as GUI_START_BEHAVIOR, COMP7_UI_SECTION as COMP7_UI_SECTION, COMP7_LAST_SEASON as COMP7_LAST_SEASON, COMP7_LAST_SEASON_WHERE_STATISTICS_SHOWN as COMP7_LAST_SEASON_WHERE_STATISTICS_SHOWN
from comp7_common_const import seasonNameBySeasonNumber as seasonNameBySeasonNumber
from comp7_common_const import seasonPointsCodeBySeasonNumber as seasonPointsCodeBySeasonNumber
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from skeletons.gui.shared import IItemsCache as IItemsCache

class ProgressCacherUI(object):
    __uiSection: Any
    __settings: Any
    __progress: Any
    def __init__(self, uiSection, subsection, default):
        ...
    def finalize(self):
        ...
    def reset(self, keys):
        ...
    def setUiFlag(self):
        ...
    def setProgress(self, key, progress):
        ...
    def getDelta(self, key, newProgress):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def isSeasonStatisticsShouldBeShown(comp7Controller=None):
    ...
def isComp7OnboardingShouldBeShown():
    ...
def isComp7WhatsNewShouldBeShown():
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def updateComp7LastSeason(comp7Ctrl=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isViewShown(key, settingsCore=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _needToShowComp7Intro(comp7Ctrl=None, includePreannounced=False, includeNext=False):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _hasParticipantToken(comp7Controller=None, itemsCache=None):
    ...
