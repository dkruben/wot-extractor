# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_respawn_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
from future.utils import listvalues as listvalues
import BigWorld as BigWorld
from frontline.gui.Scaleform.daapi.view.meta.FrontlineRespawnViewMeta import FrontlineRespawnViewMeta as FrontlineRespawnViewMeta
from frontline.gui.Scaleform.genConsts.FRONTLINE_BATTLE_VIEW_ALIASES import FRONTLINE_BATTLE_VIEW_ALIASES as FRONTLINE_BATTLE_VIEW_ALIASES
from frontline.gui.battle_control.controllers.frontline_respawn_ctrl import IFrontlineRespawnView as IFrontlineRespawnView
from gui.battle_control import avatar_getter as avatar_getter
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.Scaleform.locale.EPIC_BATTLE import EPIC_BATTLE as EPIC_BATTLE
from helpers import i18n as i18n
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_ERROR as LOG_ERROR
from gui.battle_control import minimap_utils as minimap_utils
from gui.Scaleform.daapi.view.battle.shared.respawn import respawn_utils as respawn_utils
from gui.sounds.epic_sound_constants import EPIC_SOUND as EPIC_SOUND, EPIC_TIME_WWEVENTS as EPIC_TIME_WWEVENTS
from math_common import round_py2_style_int as round_py2_style_int
import SoundGroups as SoundGroups
_BF_EB_COUNT_DOWN_SOUND_SECONDS = 10
_DEFAULT_RESPAWN_POSITIONS: tuple

class FrontlineRespawnView(FrontlineRespawnViewMeta, IFrontlineRespawnView):
    sessionProvider: Any
    __selectedLaneID: Any
    __selectedPointID: Any
    __disabled: Any
    __buttonStates: Any
    __timeOver: Any
    __countDownIsPlaying: Any
    __mapDim: Any
    __lastRespawnPositions: Any
    __carousel: Any
    __ammunitionPanel: Any
    __shop: Any
    __battleCtx: Any
    def __init__(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def _onUnregisterFlashComponent(self, viewPy, alias):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def onRespawnBtnClick(self):
        ...
    def onLocationSelected(self, pointIdx):
        ...
    def onDeploymentReady(self):
        ...
    def onRespawnInfoUpdated(self, respawnInfo):
        ...
    def isVehicleChanged(self, respawnInfo):
        ...
    def updateTimer(self, timeLeft, vehs, cooldowns, limits=None):
        ...
    def hide(self):
        ...
    def show(self, selectedID, vehs, cooldowns, limits=0):
        ...
    def start(self, vehs, isLimited):
        ...
    def setLimits(self, respawnLimits):
        ...
    def setSelectedLane(self, laneId):
        ...
    def setSelectedPoint(self, pointId):
        ...
    def setRespawnInfo(self, respawnInfo):
        ...
    def setRespawnInfoExt(self, vehInfo, setupIndexes):
        ...
    def setLaneState(self, laneID, enabled, blockedText):
        ...
    def setBattleCtx(self, battleCtx):
        ...
    def __makePointVO(self, x=0, y=0, isEnemyNear=False):
        ...
    def __playCountDownSound(self, play):
        ...
    def __playSound(self, eventName):
        ...
    def __updateSlotData(self, vehs, cooldowns, limits):
        ...
    def __getVehicleLimits(self, limits):
        ...
