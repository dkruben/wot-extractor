# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/base/fun_vehicles_filter_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode as hasDesiredSubMode
from gui.impl.lobby.hangar.base.vehicles_filter_component import VehiclesFilterComponent as VehiclesFilterComponent
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from gui.shared.utils.requesters import RequestCriteria as RequestCriteria
FUN_RANDOM_CRITERIA: Any

class FunRandomVehiclesFilterComponent(VehiclesFilterComponent, FunSubModesWatcher):
    __baseCriteria: Any
    __subModeCriteria: Any
    def __init__(self, criteria=...):
        ...
    def initialize(self):
        ...
    def destroy(self):
        ...
    def __createCriteria(self):
        ...
    # decorador original: @hasDesiredSubMode(...)
    def __getSubModeCriteria(self):
        ...
    def __onSubModeChanged(self, *_):
        ...
