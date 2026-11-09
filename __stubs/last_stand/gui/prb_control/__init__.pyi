# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/prb_control/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
import typing as typing
from constants import MIN_VEHICLE_LEVEL as MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL as MAX_VEHICLE_LEVEL
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from last_stand_common.last_stand_constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from gui.prb_control.prb_helpers import DefaultVehicleAutoSearchHelper as DefaultVehicleAutoSearchHelper
from helpers import dependency as dependency
from last_stand.skeletons.ls_controller import ILSController as ILSController

class LSVehicleAutoSearchHelper(DefaultVehicleAutoSearchHelper):
    __lsCtrl: Any
    @classmethod
    def getVehiclesLevelsChecker(cls):
        ...
