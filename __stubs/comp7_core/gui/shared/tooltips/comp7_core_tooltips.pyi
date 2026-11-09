# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/shared/tooltips/comp7_core_tooltips.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from copy import copy as copy
from future.utils import lfilter as lfilter, viewitems as viewitems
from gui import g_htmlTemplates as g_htmlTemplates
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles, getRoleText as getRoleText
from gui.shared.items_parameters import formatters as params_formatters
from gui.shared.tooltips import formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from gui.shared.tooltips.module import ModuleTooltipBlockConstructor as ModuleTooltipBlockConstructor
from gui.shared.utils.functions import stripColorTagDescrTags as stripColorTagDescrTags
from helpers_common import castNumberToPrettyStr as castNumberToPrettyStr, getPercentFromFloat as getPercentFromFloat
from items import tankmen as tankmen
from typing import Optional as Optional
from items.artefacts import Equipment as Equipment, VisualScriptEquipment as VisualScriptEquipment
_logger: Any
EQUIPMENT_TOOLTIP_PREPROCESSORS: dict

class RoleSkillBattleTooltipData(BlocksTooltipData):
    def __init__(self, context):
        ...
    @property
    def _modeController(self):
        ...
    def _packBlocks(self, roleName, equipmentName):
        ...
    @staticmethod
    def __packTooltipBlock(roleName, equipment, startLevel, modeController):
        ...

class RoleSkillLobbyTooltipData(BlocksTooltipData):
    _PARAMS_TEMPLATE: Any
    def __init__(self, context):
        ...
    @property
    def _modeController(self):
        ...
    def _packBlocks(self, equipmentName, roleName, startLevel):
        ...
    @classmethod
    def __packHeaderBlock(cls, equipment, roleName, modeController):
        ...
    @classmethod
    def __packDescriptionBlock(cls, equipment, roleName, startLevel, modeController):
        ...
    @classmethod
    def __formatEquipmentParams(cls, description):
        ...
    @staticmethod
    def __packInfoBlock():
        ...
    @staticmethod
    def __getCooldown(equipment, roleName, modeController):
        ...
    @staticmethod
    def __getRoleSkillIcon(equipment):
        ...

class TooltipPreprocessor(object):
    @staticmethod
    def processParams(params):
        ...

class Comp7AoeHealTooltipPreprocessor(TooltipPreprocessor):
    @staticmethod
    def processParams(params):
        ...

class Comp7AllyHunterTooltipPreprocessor(TooltipPreprocessor):
    @staticmethod
    def processParams(params):
        ...

class Comp7ConcentrationTooltipPreprocessor(TooltipPreprocessor):
    @staticmethod
    def processParams(params):
        ...

class Comp7BerserkTooltipPreprocessor(TooltipPreprocessor):
    @staticmethod
    def processParams(params):
        ...

class Comp7FastRechargeTooltipPreprocessor(TooltipPreprocessor):
    @staticmethod
    def processParams(params):
        ...

class Comp7JuggernautTooltipPreprocessor(TooltipPreprocessor):
    @staticmethod
    def processParams(params):
        ...

class Comp7SureShotTooltipPreprocessor(TooltipPreprocessor):
    @staticmethod
    def processParams(params):
        ...

class Comp7SniperTooltipPreprocessor(TooltipPreprocessor):
    @staticmethod
    def processParams(params):
        ...

class Comp7RiskyAttackTooltipPreprocessor(TooltipPreprocessor):
    @staticmethod
    def processParams(params):
        ...

class Comp7ReconTooltipPreprocessor(TooltipPreprocessor):
    @staticmethod
    def processParams(params):
        ...

class Comp7AggressiveDetectionTooltipPreprocessor(TooltipPreprocessor):
    @staticmethod
    def processParams(params):
        ...

class Comp7MarchTooltipPreprocessor(TooltipPreprocessor):
    @staticmethod
    def processParams(params):
        ...

def getCooldown(equipment, cooldownSecondsOverride=None):
    ...
def getStartLevelBattleTooltipText(startLevel):
    ...
def getRoleSkillDescription(equipment, roleName, startLevel, modeController):
    ...
def getPoIEquipmentDescription(equipment, modeController):
    ...
def getRoleEquipmentTooltipParts(vehicle, modeController):
    ...
