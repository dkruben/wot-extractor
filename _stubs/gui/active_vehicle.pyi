# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/active_vehicle.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from typing import TYPE_CHECKING as TYPE_CHECKING
import BigWorld as BigWorld
import AccountCommands as AccountCommands
from items.components.c11n_constants import SeasonType as SeasonType
from soft_exception import SoftException as SoftException
from typing import Any as TAny
_logger: Any

class ActiveVehicleSeasonType(object):
    _vehTypeDescrToSeason: Any
    def __init__(self):
        ...
    def get(self, vehTypeDescr, defaultSeasonType):
        ...
    def __setitem__(self, vehTypeDescr, seasonType):
        ...
    def __getitem__(self, vehTypeDescr):
        ...
    def __contains__(self, vehTypeDescr):
        ...
    def __updateServer(self, vehTypeDescr, seasonType):
        ...
    def __onSetActiveVehSeason(self, requestID, resultID, errorStr, ext=None):
        ...
