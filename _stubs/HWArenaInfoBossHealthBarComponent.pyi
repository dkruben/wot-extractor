# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/HWArenaInfoBossHealthBarComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from collections import namedtuple as namedtuple
from helpers import dependency as dependency, isPlayerAvatar as isPlayerAvatar
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
_logger: Any
BossLive: Any

class HWArenaInfoBossHealthBarComponent(DynamicScriptComponent):
    guiSessionProvider: Any
    __NO_LIVES_MIN_MAX_HEALTH: tuple
    __isActive: Any
    __lives: Any
    _livesHpRanges: Any
    _prevHealth: Any
    def __init__(self):
        ...
    @property
    def isActive(self):
        ...
    @property
    def prevHealth(self):
        ...
    @property
    def maxLives(self):
        ...
    @property
    def livesLeft(self):
        ...
    @property
    def hwBattleGuiCtrl(self):
        ...
    @property
    def bossCount(self):
        ...
    def clientOnBossHealthChanged(self, newHealth, prevHealth, bossVehicleID, attackerID, attackReasonID):
        ...
    def set_healthForLives(self, _):
        ...
    def set_minionsCount(self, prev):
        ...
    def set_isVisible(self, prev):
        ...
    def getBossCurrentLifeHealthValues(self):
        ...
    def _onAvatarReady(self):
        ...
    def __setHealthRanges(self):
        ...
    def __getMinMaxHealth(self, lifeNum):
        ...
    def __activate(self):
        ...
    def __checkLivesChanged(self):
        ...
    def __getLifeNumByHealth(self):
        ...
    def __updateMarkerMaxHealth(self):
        ...

def getArenaInfoBossHealthBarComponent():
    ...
