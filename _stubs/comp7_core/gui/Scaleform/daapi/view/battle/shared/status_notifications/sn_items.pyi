# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/shared/status_notifications/sn_items.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.battle.shared.status_notifications import sn_items as sn_items
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_TYPES import BATTLE_NOTIFICATIONS_TIMER_TYPES as _TIMER_TYPES
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from gui.impl import backport as backport
from gui.impl.gen import R as R

class _Comp7LocalizationProvider(sn_items.LocalizationProvider):
    @property
    def _stringResource(self):
        ...

class Comp7HealingSN(_Comp7LocalizationProvider, sn_items.HealingSN):
    ...

class _Comp7BuffSN(_Comp7LocalizationProvider, sn_items.TimerSN):
    _ITEM_ID = None
    _VIEW_TYPE_ID = None
    _isSourceVehicle: Any
    _isVisible: Any
    def __init__(self, updateCallback):
        ...
    def start(self):
        ...
    def getItemID(self):
        ...
    def getViewTypeID(self):
        ...
    def isSourceVehicle(self):
        ...
    def _update(self, value):
        ...

class _Comp7PulseVisibleSourceRelatedBuffSN(_Comp7BuffSN):
    _isPulseVisible: Any
    def _update(self, value):
        ...

class AoeHealSN(_Comp7PulseVisibleSourceRelatedBuffSN):
    _ITEM_ID = VEHICLE_VIEW_STATE.AOE_HEAL
    _VIEW_TYPE_ID = _TIMER_TYPES.COMP7_AOE_HEAL
    def _getTitle(self, value):
        ...

class AoeInspireSN(_Comp7PulseVisibleSourceRelatedBuffSN):
    _ITEM_ID = VEHICLE_VIEW_STATE.AOE_INSPIRE
    _VIEW_TYPE_ID = _TIMER_TYPES.COMP7_AOE_INSPIRE
    def _getTitle(self, value):
        ...

class RiskyAttackBuffSN(_Comp7BuffSN):
    _ITEM_ID = VEHICLE_VIEW_STATE.RISKY_ATTACK_BUFF
    _VIEW_TYPE_ID = _TIMER_TYPES.COMP7_RISKY_ATTACK
    def _getTitle(self, value):
        ...

class RiskyAttackHealSN(_Comp7BuffSN):
    _ITEM_ID = VEHICLE_VIEW_STATE.RISKY_ATTACK_HEAL
    _VIEW_TYPE_ID = _TIMER_TYPES.COMP7_RISKY_ATTACK_HEAL
    def _getTitle(self, value):
        ...

class BerserkSN(_Comp7BuffSN):
    _ITEM_ID = VEHICLE_VIEW_STATE.BERSERK
    _VIEW_TYPE_ID = _TIMER_TYPES.COMP7_BERSERK
    def _getTitle(self, value):
        ...

class SniperSN(_Comp7BuffSN):
    _ITEM_ID = VEHICLE_VIEW_STATE.SNIPER
    _VIEW_TYPE_ID = _TIMER_TYPES.COMP7_SNIPER
    def _getTitle(self, value):
        ...

class AllySupportSN(_Comp7BuffSN):
    _ITEM_ID = VEHICLE_VIEW_STATE.ALLY_SUPPORT
    _VIEW_TYPE_ID = _TIMER_TYPES.COMP7_ALLY_SUPPORT
    def _getTitle(self, value):
        ...

class HunterSN(_Comp7BuffSN):
    _ITEM_ID = VEHICLE_VIEW_STATE.HUNTER
    _VIEW_TYPE_ID = _TIMER_TYPES.COMP7_HUNTER
    def _getTitle(self, value):
        ...

class JuggernautSN(_Comp7BuffSN):
    _ITEM_ID = VEHICLE_VIEW_STATE.JUGGERNAUT
    _VIEW_TYPE_ID = _TIMER_TYPES.COMP7_JUGGERNAUT
    def _getTitle(self, value):
        ...

class SureShotSN(_Comp7BuffSN):
    _ITEM_ID = VEHICLE_VIEW_STATE.SURE_SHOT
    _VIEW_TYPE_ID = _TIMER_TYPES.COMP7_SURE_SHOT
    def _getTitle(self, value):
        ...

class ConcentrationSN(_Comp7BuffSN):
    _ITEM_ID = VEHICLE_VIEW_STATE.CONCENTRATION
    _VIEW_TYPE_ID = _TIMER_TYPES.COMP7_CONCENTRATION
    def _getTitle(self, value):
        ...

class MarchSN(_Comp7BuffSN):
    _ITEM_ID = VEHICLE_VIEW_STATE.MARCH
    _VIEW_TYPE_ID = _TIMER_TYPES.COMP7_MARCH
    def _getTitle(self, value):
        ...

class AggressiveDetectionSN(_Comp7BuffSN):
    _ITEM_ID = VEHICLE_VIEW_STATE.AGGRESSIVE_DETECTION
    _VIEW_TYPE_ID = _TIMER_TYPES.COMP7_AGGRESSIVE_DETECTION
    def _getTitle(self, value):
        ...

class IlluminationFlareSN(_Comp7BuffSN):
    _ITEM_ID = VEHICLE_VIEW_STATE.ILLUMINATION_FLARE_SPOTTED
    _VIEW_TYPE_ID = _TIMER_TYPES.COMP7_ILLUMINATION_FLARE
    _isVisible: Any
    def _update(self, value):
        ...
    def _getTitle(self, value):
        ...
