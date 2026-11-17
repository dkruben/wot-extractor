# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/battle/vehicle_ban/ban_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
import logging as logging
from comp7.gui.impl.gen.view_models.views.battle.constants import Constants as Constants
from comp7.gui.impl.gen.view_models.views.battle.enums import BanState as BanState
from comp7_core_constants import ArenaPrebattlePhase as ArenaPrebattlePhase
from constants import VEHICLE_SELECTION_BLOCK_DELAY as VEHICLE_SELECTION_BLOCK_DELAY
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from helpers import dependency as dependency
from math_common import round_py2_style_int as round_py2_style_int
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Optional as Optional
_logger: Any

def convertVehicleCD(vehicleCD):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def fillComp7VehicleModel(model, vehicleCD, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _getRoleEquipmentKey(vehicleItem, comp7Controller=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _getOriginalVehicleCD(vehicleCD, comp7Controller=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getOwnDatabaseID(sessionProvider=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def fillBanProgressionModel(model, vehicleBanCtrl, comp7Controller=None, sessionProvider=None):
    ...
