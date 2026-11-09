# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/crew_helpers/skill_model_setup.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.impl.gen.view_models.views.lobby.crew.common.skill.skill_model import BattleBooster as BattleBooster, SkillModel as SkillModel
from helpers import dependency as dependency
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items.Tankman import Tankman as Tankman, getBattleBooster as getBattleBooster, isSkillLearnt as isSkillLearnt
from gui.impl.gen.view_models.views.lobby.crew.common.skill.skill_simple_model import SkillSimpleModel as SkillSimpleModel
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.gui_items.tankman_skill import TankmanSkill as TankmanSkill
from gui.shared.items_cache import ItemsCache as ItemsCache
defaultPropsGetters: dict

class ModelProps(CONST_CONTAINER):
    NAME = 'name'
    LEVEL = 'level'
    ROLE_NAME = 'roleName'
    ICON_NAME = 'iconName'
    IS_ZERO = 'isZero'
    IS_IRRELEVANT = 'isIrrelevant'
    BATTLE_BOOSTER = 'battleBooster'

def getSkillName(skill, skillName=None, **__):
    ...
def getSkillLevel(skill, skillLevel=None, **__):
    ...
def getSkillIconName(skill, iconName=None, **__):
    ...
def getRoleName(skill, roleName=None, **__):
    ...
def skillSimpleModelSetup(model, customGetters=None, **kwargs):
    ...
def getIsZero(skill, tankman, role, isZero=None, **__):
    ...
def getIsIrrelevant(skill, **__):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getModelBattleBooster(skill, tankman, itemsCache=None, **__):
    ...
def skillModelSetup(model, customGetters=None, checkIrrelevant=True, **kwargs):
    ...
