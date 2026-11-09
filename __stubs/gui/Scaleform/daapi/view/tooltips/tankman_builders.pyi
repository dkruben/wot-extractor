# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/tooltips/tankman_builders.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl import backport as backport
from gui.impl.backport.backport_tooltip import DecoratedTooltipWindow as DecoratedTooltipWindow
from gui.impl.gen import R as R
from gui.impl.lobby.crew.tooltips.advanced_tooltip_view import AdvancedTooltipView as AdvancedTooltipView
from gui.impl.lobby.crew.tooltips.commander_bonus_additional_tooltip import CommanderBonusAdditionalTooltip as CommanderBonusAdditionalTooltip
from gui.impl.lobby.crew.tooltips.commander_bonus_tooltip import CommanderBonusTooltip as CommanderBonusTooltip
from gui.impl.lobby.crew.tooltips.crew_perks_additional_tooltip import CrewPerksAdditionalTooltip as CrewPerksAdditionalTooltip
from gui.impl.lobby.crew.tooltips.crew_perks_tooltip import CrewPerksTooltip as CrewPerksTooltip
from gui.impl.lobby.crew.tooltips.empty_skill_tooltip import EmptySkillTooltip as EmptySkillTooltip
from gui.impl.lobby.crew.tooltips.mentor_assignment_tooltip import MentorAssignmentTooltip as MentorAssignmentTooltip
from gui.impl.lobby.crew.tooltips.mentoring_license_tooltip import MentoringLicenseTooltip as MentoringLicenseTooltip
from gui.impl.lobby.crew.tooltips.skill_untrained_additional_tooltip import SkillUntrainedAdditionalTooltip as SkillUntrainedAdditionalTooltip
from gui.impl.lobby.crew.tooltips.skill_untrained_tooltip import SkillUntrainedTooltip as SkillUntrainedTooltip
from gui.impl.lobby.crew.tooltips.skills_efficiency_tooltip import SkillsEfficiencyTooltip as SkillsEfficiencyTooltip
from gui.impl.lobby.crew.tooltips.tankman_tooltip import TankmanTooltip as TankmanTooltip
from gui.shared.tooltips import advanced as advanced, TOOLTIP_COMPONENT as TOOLTIP_COMPONENT, WulfTooltipData as WulfTooltipData
from gui.shared.tooltips import contexts as contexts, ToolTipBaseData as ToolTipBaseData
from gui.shared.tooltips import tankman as tankman
from gui.shared.tooltips.advanced import TANKMAN_MOVIES as TANKMAN_MOVIES
from gui.shared.tooltips.builders import DataBuilder as DataBuilder, AdvancedTooltipWindowBuilder as AdvancedTooltipWindowBuilder, TooltipWindowBuilder as TooltipWindowBuilder
from gui.shared.tooltips.contexts import ToolTipContext as ToolTipContext
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.shared import IItemsCache as IItemsCache
__all__: tuple

class BattleRoyaleTankmanTooltipBuilder(DataBuilder):
    __slots__: tuple
    __battleRoyaleController: Any
    def __init__(self, tooltipType, linkage):
        ...
    def _buildData(self, _advanced, invID, *args, **kwargs):
        ...

class NotRecruitedTankmanTooltipBuilder(DataBuilder):
    __slots__: tuple
    def __init__(self, tooltipType, linkage):
        ...
    def _buildData(self, _advanced, invID, *args, **kwargs):
        ...

class SpecialTankmanTooltipBuilder(DataBuilder):
    __slots__: tuple
    def __init__(self, tooltipType, linkage):
        ...

class CrewPerkTooltipData(ToolTipBaseData):
    def __init__(self, context, toolTipType=...):
        ...
    def getDisplayableData(self, skillName, skillRole, tankmanId, skillLevel=None, showAdditionalInfo=True, crewCustomName='', isBonus=None, skillIdx=-1, guiTankman=None, vehicle=None, *args, **kwargs):
        ...
    def buildToolTip(self, *args, **kwargs):
        ...
    def setSupportAdvanced(self, supportAdvanced):
        ...

class CrewPerkTooltipDataAdditional(CrewPerkTooltipData):
    def getDisplayableData(self, skillName, skillRole, tankmanId, skillLevel=None, isCommonExtraAvailable=False, showAdditionalInfo=True, isBonus=None, skillIdx=-1, showCrewAssist=False, *args, **kwargs):
        ...

class SkillUntrainedTooltipData(ToolTipBaseData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, *args, **kwargs):
        ...

class SkillUntrainedTooltipDataAdditional(SkillUntrainedTooltipData):
    def getDisplayableData(self, *args, **kwargs):
        ...

class CommanderBonusTooltipData(ToolTipBaseData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, tankmanId=None, *args, **kwargs):
        ...

class CommanderBonusTooltipDataAdditional(CommanderBonusTooltipData):
    def getDisplayableData(self, tankmanId=None, *args, **kwargs):
        ...

class TankmanTooltipData(ToolTipBaseData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, *args, **kwargs):
        ...

class TankmanTooltipAdditional(ToolTipBaseData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, tankmanID=None, *args, **kwargs):
        ...

class SkillsEfficiencyTooltipData(ToolTipBaseData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, *args, **kwargs):
        ...

class SkillsEfficiencyTooltipAdditional(ToolTipBaseData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, *args, **kwargs):
        ...

class MentorLicenseTooltipContext(ToolTipContext):
    goodiesCache: Any
    def __init__(self, fieldsToExclude=None):
        ...
    def buildItem(self, goodieID):
        ...

class MentorLicenseTooltipData(WulfTooltipData):
    def __init__(self, context):
        ...
    def getTooltipContent(self, itemID, *args, **kwargs):
        ...

class MentorAssignmentTooltipData(ToolTipBaseData):
    def __init__(self, context):
        ...
    @staticmethod
    def getDisplayableData(*args, **kwargs):
        ...

class MentorAssignmentTooltipAdditional(ToolTipBaseData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, tankmanID=None, *args, **kwargs):
        ...

class EmptySkillTooltipData(ToolTipBaseData):
    itemsCache: Any
    def __init__(self, context):
        ...
    def getDisplayableData(self, tankmanId, *args, **kwargs):
        ...

def _advancedPerkCondition(skillName, *_):
    ...
def getTooltipBuilders():
    ...
