# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/battle_control/controllers/equipment_items.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import importlib as importlib
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
from gui.shared.system_factory import registerEquipmentItem as registerEquipmentItem
from gui.battle_control import avatar_getter as avatar_getter
from constants import EQUIPMENT_STAGES as EQUIPMENT_STAGES
from gui.Scaleform.genConsts.ANIMATION_TYPES import ANIMATION_TYPES as ANIMATION_TYPES
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control.controllers.consumables.equipment_ctrl import _RepairCrewAndModules as _RepairCrewAndModules, _EquipmentItem as _EquipmentItem, _ArcadeMineFieldItem as _ArcadeMineFieldItem, _ArtilleryItem as _ArtilleryItem, _TriggerItem as _TriggerItem, _ArcadeSmokeItem as _ArcadeSmokeItem, _ReplayItem as _ReplayItem, _ReplayOrderItem as _ReplayOrderItem, _ReplayAfterburningItem as _ReplayAfterburningItem, _ReplayBomberItem as _ReplayBomberItem, _ReplaySmokeItem as _ReplaySmokeItem, _ArcadeBomberItem as _ArcadeBomberItem, _AfterburningItem as _AfterburningItem, _ActivationError as _ActivationError, InCooldownError as InCooldownError, _ReplayArtilleryItem as _ReplayArtilleryItem
from battle_royale.gui.constants import BattleRoyaleEquipments as BattleRoyaleEquipments
MapCaseMode: Any
CorrodingShotInfo: Any

class _BuffItem(_TriggerItem):
    _animationType: Any
    def update(self, quantity, stage, timeRemaining, totalTime):
        ...

class _BomberStrikeSelector(object):
    def getStrikeSelector(self):
        ...

class _RepairBattleRoyaleCrewAndModules(_RepairCrewAndModules):
    def _canActivate(self, entityName=None, avatar=None):
        ...
    def __hasDebuffComponentsForStop(self, vehicle):
        ...

class _RegenerationKitBattleRoyaleItem(_EquipmentItem):
    def canActivate(self, entityName=None, avatar=None):
        ...
    def getActivationCode(self, entityName=None, avatar=None):
        ...
    def getAnimationType(self):
        ...

class _ArcadeMineFieldBattleRoyaleItem(_ArcadeMineFieldItem, _BomberStrikeSelector):
    def _getErrorMsg(self):
        ...

class _FireCircle(_TriggerItem):
    def getTags(self):
        ...
    def getEntitiesIterator(self, avatar=None):
        ...

class _CorrodingShotIndicator(object):
    guiSessionProvider: Any
    __EQUIPMENT_NAME = BattleRoyaleEquipments.CORRODING_SHOT
    @classmethod
    def updateIndicator(cls, stage, timeRemaining):
        ...

class _CorrodingShot(_TriggerItem):
    __slots__: tuple
    __crosshairIndicator: Any
    def __init__(self, descriptor, quantity, stage, timeRemaining, totalTime, tags):
        ...
    def getTags(self):
        ...
    def getEntitiesIterator(self, avatar=None):
        ...
    def canActivate(self, entityName=None, avatar=None):
        ...
    def canDeactivate(self):
        ...
    def update(self, quantity, stage, timeRemaining, totalTime):
        ...

class _BotSpawner(_ArtilleryItem, _BomberStrikeSelector):
    MAX_SHIFT = 5
    MIN_SHIFT = 0
    def getAimingControlMode(self):
        ...
    def _getErrorMsg(self):
        ...
    def getStrikeSelector(self):
        ...

class _ThunderStrike(_ArtilleryItem, _BomberStrikeSelector):
    MAX_SHIFT = 5
    MIN_SHIFT = -5
    def getAimingControlMode(self):
        ...
    def _getErrorMsg(self):
        ...
    def getStrikeSelector(self):
        ...

class _AdaptationHealthRestore(_TriggerItem):
    __duration: Any
    __cooldownSeconds: Any
    _totalTime: Any
    _animationType: Any
    def __init__(self, descriptor, quantity, stage, timeRemaining, totalTime, tags=None):
        ...
    def getTags(self):
        ...
    def getEntitiesIterator(self, avatar=None):
        ...
    def update(self, quantity, stage, timeRemaining, totalTime):
        ...

class _ShotPassion(_BuffItem):
    def getTags(self):
        ...
    def getEntitiesIterator(self, avatar=None):
        ...

class _ArcadeBomber(_ArcadeBomberItem, _BomberStrikeSelector):
    ...

class _ArcadeSmoke(_ArcadeSmokeItem, _BomberStrikeSelector):
    ...

class _BRReplayMinefield(_ReplayOrderItem, _BomberStrikeSelector):
    ...

class _BRReplayBomber(_ReplayBomberItem, _BomberStrikeSelector):
    ...

class _BRReplaySpawnBot(_ReplayOrderItem, _BomberStrikeSelector):
    ...

class _BRReplaySmoke(_ReplaySmokeItem, _BomberStrikeSelector):
    ...

class _BRReplayThunderStrike(_ReplayArtilleryItem, _BomberStrikeSelector):
    ...

class _GameplayConsumableItem(_TriggerItem):
    def getTags(self):
        ...
    def getEntitiesIterator(self, avatar=None):
        ...

class _RepairPointItem(_TriggerItem):
    def getTags(self):
        ...
    def getEntitiesIterator(self, avatar=None):
        ...

class _BRReplayCorrodingShot(_ReplayItem):
    __slots__: tuple
    __crosshairIndicator: Any
    def __init__(self, descriptor, quantity, stage, timeRemaining, totalTime, tags=None):
        ...
    def update(self, quantity, stage, timeRemaining, totalTime):
        ...

def registerBREquipmentsItems():
    ...
