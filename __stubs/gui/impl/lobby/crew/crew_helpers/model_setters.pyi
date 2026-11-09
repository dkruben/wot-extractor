# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/crew_helpers/model_setters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import math as math
from collections import defaultdict as defaultdict
from itertools import chain as chain
from typing import TYPE_CHECKING as TYPE_CHECKING
from constants import NEW_PERK_SYSTEM as NPS
from gui.impl.auxiliary.vehicle_helper import fillVehicleInfo as fillVehicleInfo
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.common.crew_skill_list_model import CrewSkillListModel as CrewSkillListModel
from gui.impl.gen.view_models.views.lobby.crew.common.crew_skill_model import CrewSkillModel as CrewSkillModel
from gui.impl.gen.view_models.views.lobby.crew.common.skill.skill_progression_model import SkillProgressionModel as SkillProgressionModel
from gui.impl.gen.view_models.views.lobby.crew.crew_constants import CrewConstants as CrewConstants
from gui.impl.gen.view_models.views.lobby.crew.tankman_model import TankmanCardState as TankmanCardState, TankmanKind as TankmanKind, TankmanLocation as TankmanLocation, TankmanRole as TankmanRole
from gui.impl.lobby.crew.crew_helpers.skill_helpers import getTmanNewSkillCount as getTmanNewSkillCount
from gui.impl.lobby.crew.crew_helpers.skill_model_setup import skillModelSetup as skillModelSetup
from gui.impl.lobby.crew.dialogs.recruit_window.recruit_dialog_utils import getIconBackground as getIconBackground
from gui.shared.gui_items.Tankman import SKILL_EFFICIENCY_UNTRAINED as SKILL_EFFICIENCY_UNTRAINED
from gui.shared.gui_items.tankman_skill import getTankmanSkill as getTankmanSkill
from helpers import dependency as dependency, time_utils as time_utils
from items.tankmen import MAX_SKILLS_EFFICIENCY as MAX_SKILLS_EFFICIENCY, MAX_SKILL_LEVEL as MAX_SKILL_LEVEL
from skeletons.gui.game_control import ISpecialSoundCtrl as ISpecialSoundCtrl
from skeletons.gui.shared import IItemsCache as IItemsCache
from .skill_formatters import SkillLvlFormatter as SkillLvlFormatter
from typing import Optional as Optional, List as List
from frameworks.wulf import Array as Array
from gui.shared.gui_items.Tankman import Tankman as Tankman
BARRACK_RECRUIT_BG_DYN = R.images.gui.maps.icons.tankmen.windows.recruits.barracks

def setTankmanModel(tm, tman, tmanNativeVeh, tmanVeh=None):
    ...
def setTmanSkillsModel(sm, tman, useOnlyFull=False, possibleSkillsLevels=None, fillBonusSkills=True, isRecruit=False, compVeh=None, customCrewName=''):
    ...
def setTmanMajorSkillsModel(listVM, tman, useOnlyFull=False, possibleSkillsLevels=None, customCrewName='', isRecruit=False):
    ...
def setTmanBonusSkillsModel(listVM, tman, bonusSlotsLevels=None, selectedRole=None, selectedSkills=None):
    ...
def getCrewWidgetTmanSkillModelNPS(tman, skill, role, level=None):
    ...
def getNewSkillCrewWidgetTmanSkillModelNPS(level=None, isZero=False):
    ...
def setReplacedTankmanModel(tm, tman, tmanNativeVeh):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def setRecruitTankmanModel(tm, recruitInfo, specialSoundCtrl=None, useOnlyFullSkills=True):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def setTankmanRestoreInfo(vm, itemsCache=None):
    ...
def ifWGMAvailableButtonUpdate(vm, itemsCache, button, checkIsPriceSelected):
    ...
def setSkillProgressionModel(vm, tankman, skillIndex, isZero):
    ...
