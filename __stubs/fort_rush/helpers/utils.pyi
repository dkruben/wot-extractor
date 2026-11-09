# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/helpers/utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
import typing as typing
from helpers import dependency as dependency
from fort_rush.skeletons.battle_controller import IFortRushBattleController as IFortRushBattleController
from fort_rush_common.component_helpers import getVehicleRespawnComponent as getVehicleRespawnComponent
from constants import IS_CLIENT as IS_CLIENT
from typing import Optional as Optional
from RespawnFrameworkVehicleComponent import RespawnFrameworkVehicleComponent as RespawnFrameworkVehicleComponent
_logger: Any
avatar_getter = None

def getCurrentTeam(guiSessionProvider=None):
    ...
def mapOwnerTeamToMarkerTeam(ownerTeam, playerTeam):
    ...
def retrievePlayerRespawnComponent():
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isFREventProgressionQuest(questId, ctrl=None):
    ...
