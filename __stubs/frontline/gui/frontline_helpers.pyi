# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/frontline_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import defaultdict as defaultdict
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from itertools import chain as chain
from typing import List as List
import BigWorld as BigWorld
import CommandMapping as CommandMapping
import typing as typing
from frontline.gui.impl.gen.view_models.views.lobby.views.frontline_const import FrontlineState as FrontlineState
from frontline_common.frontline_constants import RESERVES_MODIFIER_NAMES as RESERVES_MODIFIER_NAMES
from constants import FINISH_REASON as FINISH_REASON
from gui.Scaleform.daapi.view.common.keybord_helpers import getHotKeysInfo as getHotKeysInfo
from gui.Scaleform.daapi.view.lobby.epicBattle.epic_helpers import createEpicParam as createEpicParam
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus
from helpers import time_utils as time_utils, dependency as dependency, i18n as i18n
from items import vehicles as vehicles
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
TEMPLATES: Any

class FLBattleTypeDescription(object):
    @staticmethod
    def getDescription(reservesModifier=None):
        ...
    @staticmethod
    def getShortDescription(reservesModifier=None):
        ...
    @staticmethod
    def getTitle(reservesModifier=None):
        ...
    @staticmethod
    def getBattleTypeIconPath(reservesModifier=None, sizeFolder='c_136x136'):
        ...
    @staticmethod
    def __getDescription(descriptionType, reservesModifier):
        ...
    @staticmethod
    def __getRS():
        ...
    @staticmethod
    def __getRI():
        ...

class AbilitiesTemplates(object):
    __templateDir: Any
    def __init__(self, templateDir):
        ...
    @property
    def default(self):
        ...
    @property
    def seconds(self):
        ...
    @property
    def meters(self):
        ...
    @property
    def percents(self):
        ...
    @property
    def percentsBySecond(self):
        ...
    @property
    def skillParams(self):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def getFrontlineState(withPrimeTime=False, epicController=None):
    ...
def getStatesUnavailableForHangar():
    ...
def getReserveIconPath(icon):
    ...
def getHotKeyListCommands():
    ...
def getHotKeyInfoListByIndex(index):
    ...
def isHangarAvailable():
    ...
def getSkillParams(skillLevelData):
    ...
def becomeNonPlayerState():
    ...
def isFinishedCycleState(frontlineState=None):
    ...
def isAnnouncedCycleState(frontlineState=None):
    ...
def makeNewEpicBattleFinishResultLabel(finishReason, teamResult):
    ...
