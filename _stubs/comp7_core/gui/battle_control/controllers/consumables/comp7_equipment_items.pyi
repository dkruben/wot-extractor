# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/battle_control/controllers/consumables/comp7_equipment_items.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from PlayerEvents import g_playerEvents as g_playerEvents
from comp7_core_constants import ROLE_EQUIPMENT_TAG as ROLE_EQUIPMENT_TAG
from constants import EQUIPMENT_STAGES as EQUIPMENT_STAGES
from gui.Scaleform.genConsts.BATTLE_MARKERS_CONSTS import BATTLE_MARKERS_CONSTS as BATTLE_MARKERS_CONSTS
from gui.battle_control.controllers.consumables.equipment_ctrl import _ActivationError as _ActivationError, _ReplayItem as _ReplayItem, _VisualScriptItem as _VisualScriptItem
_logger: Any
_ROLE_SKILL_ITEM_CLASS_BY_NAME: dict
_REPLAY_ROLE_SKILL_ITEM_CLASS_BY_NAME: dict
EQUIPMENT_TAG_TO_ITEM: dict
REPLAY_EQUIPMENT_TAG_TO_ITEM: dict

class Comp7RoleSkillUnavailable(_ActivationError):
    def __new__(cls, name):
        ...
    def __init__(self, name):
        ...

class Comp7RoleSkillAlreadyActivated(_ActivationError):
    def __new__(cls, name):
        ...
    def __init__(self, name):
        ...

class Comp7RoleSkillCooldown(_ActivationError):
    def __new__(cls, name):
        ...
    def __init__(self, name):
        ...

class Comp7FastRechargeGunTemperatureLow(_ActivationError):
    def __new__(cls, name):
        ...
    def __init__(self, name):
        ...

class _RoleSkillVSItem(_VisualScriptItem):
    __FORBIDDEN_STAGES_TO_ACTIVATE: tuple
    _prevQuantity: Any
    _quantity: Any
    def update(self, quantity, stage, timeRemaining, totalTime):
        ...
    def _getErrorMsg(self):
        ...
    def getQuantity(self):
        ...
    def canActivate(self, entityName=None, avatar=None):
        ...

class _DeferredRoleSkillVSItem(_RoleSkillVSItem):
    _ACTIVATION_COOLDOWN = 0.2
    _lastActivationTime = 0
    def __init__(self, *args):
        ...
    def clear(self):
        ...
    def canActivate(self, entityName=None, avatar=None):
        ...
    def __onRoundFinished(self, *_):
        ...

class _RoleSkillReconVSItem(_DeferredRoleSkillVSItem):
    def _getAimingControlMode(self):
        ...

class _RoleSkillArtyVSItem(_DeferredRoleSkillVSItem):
    def _getAimingControlMode(self):
        ...
    def getMarker(self):
        ...
    def getMarkerColor(self):
        ...

class _ReplayRoleSkillVSItem(_ReplayItem, _RoleSkillVSItem):
    def getAnimationType(self):
        ...
    def update(self, quantity, stage, timeRemaining, totalTime):
        ...
    def canActivate(self, entityName=None, avatar=None):
        ...
    def _getErrorMsg(self):
        ...

class _ReplayRoleSkillArtyVSItem(_ReplayRoleSkillVSItem):
    def getMarker(self):
        ...

def _comp7ItemFactory(descriptor, quantity, stage, timeRemaining, totalTime, tag=None):
    ...
def _replayComp7ItemFactory(descriptor, quantity, stage, timeRemaining, totalTime, tag=None):
    ...
