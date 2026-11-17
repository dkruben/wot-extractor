# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/classic/team_bases_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE
from gui.Scaleform.daapi.view.meta.TeamBasesPanelMeta import TeamBasesPanelMeta as TeamBasesPanelMeta
from gui.Scaleform.locale.INGAME_GUI import INGAME_GUI as I18N_INGAME_GUI
from gui.battle_control.controllers import team_bases_ctrl as team_bases_ctrl
from gui.shared.utils.functions import getBattleSubTypeBaseNumber as getBattleSubTypeBaseNumber
from gui.shared.utils.functions import isControlPointExists as isControlPointExists
from helpers import dependency as dependency
from helpers import i18n as i18n, time_utils as time_utils
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_MAX_INVADERS_COUNT = 3
_SETTINGS_TO_TEAM: dict
_SETTINGS_TO_CONTROL_POINT: dict

class _TeamBaseSettingItem(object):
    __slots__: tuple
    _weight: Any
    _color: Any
    _capturing: Any
    _captured: Any
    _blocked: Any
    _arenaTypeID: Any
    _team: Any
    _baseID: Any
    _subTypeBaseID: Any
    def __init__(self, weight, color, capturing, captured, blocked):
        ...
    def setup(self, arenaTypeID, baseID, team):
        ...
    def getWeight(self):
        ...
    def getColor(self):
        ...
    def getCapturingString(self, points):
        ...
    def getBlockedString(self):
        ...
    def getCapturedString(self):
        ...
    def getBattleSubTypeBaseNumber(self):
        ...

class TeamBasesPanel(TeamBasesPanelMeta, team_bases_ctrl.ITeamBasesListener):
    sessionProvider: Any
    __basesDict: Any
    def __init__(self):
        ...
    def setOffsetForEnemyPoints(self):
        ...
    def addCapturingTeamBase(self, clientID, playerTeam, points, _, timeLeft, invadersCnt, capturingStopped):
        ...
    def addCapturedTeamBase(self, clientID, playerTeam, timeLeft, invadersCnt):
        ...
    def updateTeamBasePoints(self, clientID, points, rate, timeLeft, invadersCnt):
        ...
    def blockTeamBaseCapturing(self, clientID, points):
        ...
    def stopTeamBaseCapturing(self, clientID, points):
        ...
    def setTeamBaseCaptured(self, clientID, playerTeam):
        ...
    def removeTeamBase(self, clientID):
        ...
    def removeTeamsBases(self):
        ...
    @staticmethod
    def __getInvadersCountStr(count):
        ...

def _getSettingItem(clientID, ownTeam, arenaTypeID):
    ...
