# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/tankman.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from builtins import range as range
from typing import List as List, Optional as Optional
import nations as nations
from gui import makeHtmlString as makeHtmlString
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.genConsts.ICON_TEXT_FRAMES import ICON_TEXT_FRAMES as ICON_TEXT_FRAMES
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items.Tankman import getFullUserName as getFullUserName, getSpecialIconPath as getSpecialIconPath, Tankman as Tankman
from gui.shared.tooltips import ToolTipDataField as ToolTipDataField, TOOLTIP_TYPE as TOOLTIP_TYPE, formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from gui.shared.utils.skill_presenter_helper import getSkillBigIconPath as getSkillBigIconPath
from helpers import dependency as dependency, i18n as i18n, time_utils as time_utils
from helpers.i18n import makeString as makeString
from items.components.component_constants import EMPTY_STRING as EMPTY_STRING
from items.special_crew import CustomSkills as CustomSkills
from items.tankmen import TankmanDescr as TankmanDescr, MAX_SKILL_LEVEL as MAX_SKILL_LEVEL
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
_TIME_FORMAT_UNITS: list

class TankmanSkillListField(ToolTipDataField):
    def _getValue(self):
        ...
    @staticmethod
    def _getBaseSkills(tankman):
        ...
    def _addNewSkills(self, tankman, skillsList):
        ...

class BattleRoyaleTankmanSkillListField(TankmanSkillListField):
    __battleRoyaleController: Any
    def _getValue(self):
        ...
    def _addNewSkills(self, tankman, skillsList):
        ...

class NotRecruitedTooltipData(BlocksTooltipData):
    item: Any
    def __init__(self, ctx):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class SpecialTankmanTooltipData(BlocksTooltipData):
    __slots__: tuple
    def __init__(self, ctx):
        ...
    def _packBlocks(self, tankmanData, groupName, *args, **kwargs):
        ...
    def __getNewSkillCount(self, freeXP):
        ...

class BattleRoyaleTankmanTooltipDataBlock(BlocksTooltipData):
    _itemsCache: Any
    _lobbyContext: Any
    _skillIconNamePadding: dict
    item: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def _getSign(self, val):
        ...
    def _getBonusValue(self, tankman, ids):
        ...
    def _getVehicleName(self, vehicle=None, nativeVehicle=None):
        ...
    def _createLabel(self, innerBlock):
        ...
    def _createEarnedSkillsBlock(self, commonStatsBlock):
        ...
    def _getFullUserName(self, item):
        ...
    def _crewSpecialSkillsTitle(self):
        ...
    def _getTankmanDescription(self, _):
        ...
    def _getSkillList(self):
        ...
    def _createVehicleBlock(self, innerBlock, vehicle):
        ...

def getSkillIcon(skillName, customCrewName):
    ...
