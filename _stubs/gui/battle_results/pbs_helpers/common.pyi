# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/pbs_helpers/common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import json as json
from itertools import chain as chain
from collections import namedtuple as namedtuple
from constants import FINISH_REASON as FINISH_REASON
from gui import SystemMessages as SystemMessages
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.locale.BATTLE_RESULTS import BATTLE_RESULTS as BATTLE_RESULTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from dossiers2.ui.achievements import MARK_ON_GUN_RECORD as MARK_ON_GUN_RECORD, MARK_OF_MASTERY_RECORD as MARK_OF_MASTERY_RECORD, MARK_OF_MASTERY as MARK_OF_MASTERY, MARK_ON_GUN as MARK_ON_GUN, ACHIEVEMENT_TYPE as ACHIEVEMENT_TYPE
from gui.impl.gen.view_models.views.lobby.battle_results.postbattle_achievement_model import PostbattleAchievementModel as PostbattleAchievementModel
from helpers import dependency as dependency
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from gui.battle_results.reusable import _ReusableInfo as _ReusableInfo
from gui.battle_results.reusable.players import PlayerInfo as PlayerInfo
from gui.battle_results.reusable.shared import VehicleSummarizeInfo as VehicleSummarizeInfo
from gui.battle_results.stats_ctrl import BattleResults as BattleResults
from gui.shared.gui_items.dossier.achievements.abstract import RegularAchievement as RegularAchievement
_PlayerNames: Any
_AchievementData: Any

# decorador original: @dependency.replace_none_kwargs(...)
def getBattleResults(arenaUniqueID, battleResults=None):
    ...
def isPersonalBattleResult(summarizeInfo, battleResult):
    ...
def isRealNameVisible(reusable, playerInfo):
    ...
def getArenaNameStr(reusable):
    ...
def getRegularFinishResultResource(finishReason, teamResult):
    ...
def getUserNames(playerInfo, isPlayerRealNameVisible):
    ...
def getEnemies(reusable, result):
    ...
def pushNoBattleResultsDataMessage():
    ...
def getVehicleLevel(reusable):
    ...
def getAchievementCustomData(item):
    ...
def getPersonalAchievements(battleResults):
    ...
def getTeamPlayerAchievements(player, reusable):
    ...
def prepareAchievementData(item, groupID, reusable):
    ...
def getAchievementTooltipType(achievementName):
    ...
def getAchievementTooltipArgs(achievement, reusable):
    ...
