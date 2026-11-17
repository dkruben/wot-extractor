# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/presenters/packers/tooltips/efficiency_tooltips.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from constants import DEATH_REASON_ALIVE as DEATH_REASON_ALIVE
from frameworks.wulf.view.array import fillResourcesArray as fillResourcesArray
from gui.battle_results.pbs_helpers.common import getEnemies as getEnemies
from gui.battle_results.presenters.packers.interfaces import ITooltipPacker as ITooltipPacker
from gui.impl.gen.resources import R as R
from gui.impl.gen.view_models.views.lobby.battle_results.tooltips.critical_damage_group_model import CriticalDamageGroupModel as CriticalDamageGroupModel
from gui.impl.gen.view_models.views.lobby.battle_results.tooltips.critical_damage_tooltip_model import CriticalDamageTooltipModel as CriticalDamageTooltipModel
from gui.impl.gen.view_models.views.lobby.battle_results.tooltips.efficiency_item_model import Unit as Unit, EfficiencyItemModel as EfficiencyItemModel
from soft_exception import SoftException as SoftException
from gui.impl.gen.view_models.views.lobby.battle_results.efficiency_param_constants import EfficiencyParamConstants as EfficiencyParamConstants
from gui.battle_results.stats_ctrl import BattleResults as BattleResults
from gui.battle_results.reusable import _ReusableInfo as _ReusableInfo
from gui.battle_results.reusable.shared import VehicleSummarizeInfo as VehicleSummarizeInfo
from frameworks.wulf import PyResAccessor as PyResAccessor
from gui.impl.gen.view_models.views.lobby.battle_results.tooltips.efficiency_tooltip_model import EfficiencyTooltipModel as EfficiencyTooltipModel
_STR_PATH = R.strings.battle_results.common
_IMG_PATH = R.images.gui.maps.icons.library.efficiency.statsParameters
PARAMETERS_TO_TOOLTIP_MAP: dict

class BaseParameter(object):
    _UNITS_TO_RESOURCE_IDS_MAP: dict
    _TITLE = None
    _DESCRIPTION = None
    _ICON = None
    _ITEM_LABELS: tuple
    _STATUS = None
    @classmethod
    def getTitle(cls):
        ...
    @classmethod
    def getIcon(cls):
        ...
    @classmethod
    def getDescription(cls):
        ...
    @classmethod
    def getLables(cls):
        ...
    @classmethod
    def getValues(cls, *args):
        ...
    @classmethod
    def getStatuses(cls, *args):
        ...

class SpottedParameter(BaseParameter):
    _TITLE = _STR_PATH.tooltip.spotted.header
    _DESCRIPTION = _STR_PATH.tooltip.spotted.description
    _ICON = _IMG_PATH.spotted

class CapturePointsParameter(BaseParameter):
    _TITLE = _STR_PATH.tooltip.capture.header
    _DESCRIPTION = _STR_PATH.tooltip.capture.description
    _ICON = _IMG_PATH.capturePoints
    _ITEM_LABELS: tuple
    @classmethod
    def getValues(cls, playerResult, isAdditionalValuesVisible, _):
        ...

class DefencePointsParameter(BaseParameter):
    _TITLE = _STR_PATH.tooltip.defence.header
    _DESCRIPTION = _STR_PATH.tooltip.defence.description
    _ICON = _IMG_PATH.droppedCapturePoints
    _ITEM_LABELS: tuple
    @classmethod
    def getValues(cls, playerResult, isAdditionalValuesVisible, _):
        ...

class KillsParameter(BaseParameter):
    _TITLE = _STR_PATH.tooltip.kill.header
    _DESCRIPTION = _STR_PATH.tooltip.killCommon.description
    _ICON = _IMG_PATH.kills
    _STATUS = _STR_PATH.tooltip
    @classmethod
    def getStatuses(cls, reusable, results, userName, isZeroValuesVisible=False):
        ...

class DamageDealtParameter(BaseParameter):
    _TITLE = _STR_PATH.tooltip.damage.header
    _DESCRIPTION = _STR_PATH.tooltip.damage.description
    _ICON = _IMG_PATH.damageDealt
    _ITEM_LABELS: tuple
    @classmethod
    def getValues(cls, playerResult, _, isZeroValuesVisible=False):
        ...

class StunParameter(BaseParameter):
    _TITLE = _STR_PATH.tooltip.stun.header
    _DESCRIPTION = _STR_PATH.tooltip.stun.description
    _ICON = _IMG_PATH.damageAssistedStun
    _ITEM_LABELS: tuple
    @classmethod
    def getValues(cls, playerResult, _, isZeroValuesVisible=False):
        ...

class DamageAssistedParameter(BaseParameter):
    _TITLE = _STR_PATH.tooltip.assist.header
    _DESCRIPTION = _STR_PATH.tooltip.assist.description
    _ICON = _IMG_PATH.damageAssisted
    _ITEM_LABELS: tuple
    @classmethod
    def getValues(cls, playerResult, _, isZeroValuesVisible=False):
        ...

class DamageBlockedByArmorParameter(BaseParameter):
    _TITLE = _STR_PATH.tooltip.armor.header
    _DESCRIPTION = _STR_PATH.tooltip.armor.description
    _ICON = _IMG_PATH.damageBlockedByArmor
    _ITEM_LABELS: tuple
    @classmethod
    def getValues(cls, playerResult, _, isZeroValuesVisible=False):
        ...

class EfficiencyTooltipsPacker(ITooltipPacker):
    _TOOLTIPS = PARAMETERS_TO_TOOLTIP_MAP
    @classmethod
    def packTooltip(cls, model, battleResults, ctx=None):
        ...
    @staticmethod
    def _getEfficiencyParameter(paramType):
        ...
    @staticmethod
    def __packDetails(detailsModel, values, labels):
        ...

class CriticalDamageTooltipPacker(ITooltipPacker):
    @classmethod
    def packTooltip(cls, model, battleResults, ctx=None):
        ...
    @classmethod
    def _packDetails(cls, detailsModel, battleResults, ctx):
        ...
    @staticmethod
    def _packDetailsGroup(detailsModel, crits, groupType):
        ...

def getEnemyInfo(userName, reusable, results):
    ...
def getPlayerResults(battleResults, userName):
    ...
def getStunValues(playerResult, isZeroValuesVisible=False):
    ...
def getDamageValues(playerResult, isZeroValuesVisible=False):
    ...
def getArmorValues(playerResult, isZeroValuesVisible=False):
    ...
def getAssistValues(playerResult, isZeroValuesVisible=False):
    ...
def getKilledReasons(reusable, results, userName, isZeroValuesVisible=False):
    ...
def getCapturePointsValues(playerResult):
    ...
def getDefencePointsValues(playerResult):
    ...
