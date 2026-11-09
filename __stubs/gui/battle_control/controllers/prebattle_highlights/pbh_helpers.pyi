# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/prebattle_highlights/pbh_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
from collections import namedtuple as namedtuple
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from CGF import TransformComponent as TransformComponent
from GenericComponents import getGlobalTagStorage as getGlobalTagStorage
from cgf_components.prefab_path_component import PyPrefabPathComponent as PyPrefabPathComponent
from gui.battle_control.avatar_getter import getSpaceID as getSpaceID
from gui.battle_control.controllers.prebattle_highlights.pbh_constants import TANK_POS_TEMPLATE as TANK_POS_TEMPLATE
from helpers.dependency import replace_none_kwargs as replace_none_kwargs
from shared_utils import first as first
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from CGF import GameObject as GameObject
from typing import Optional as Optional
_logger: Any
_PBH_PREFAB_TAG = 'pbh_root'
_PBH_ANCHOR_TAG = 'pbh_anchor'
_PBH_SPACE_PREFAB_TAG = 'pbh_space_object'
_PBH_PET_ANCHOR_TEMPLATE = 'pbh_pet_top{}_{}'
PbhAnchorData: Any

class PbhSounds(CONST_CONTAINER):
    GROUP = 'STATE_ext_pbh'
    GROUP_ON = 'STATE_ext_pbh_on'
    GROUP_OFF = 'STATE_ext_pbh_off'
    EXIT_EVENT = 'pbh_stage_exit'
    ESC_EVENT = 'dc_ui_exit'
    ENTER_EVENT = 'pbh_stage_01'

def getPbhPrefabGo():
    ...
def getPointTransformComponent(position, size):
    ...
# decorador original: @replace_none_kwargs(...)
def timeUntilEndOfPeriod(sessionProvider=None):
    ...
def getPbhAnchorData():
    ...
def getPbhPetAnchorGo(position, size):
    ...
def getPbhSpacePrefab():
    ...
