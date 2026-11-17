# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/vehicle_view_states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode as hasDesiredSubMode
from gui.vehicle_view_states import SelectedViewState as SelectedViewState

class FunRandomVehicleViewState(SelectedViewState, FunSubModesWatcher):
    _isCustomizationVisible: Any
    _isEliteShown: Any
    _isLevelShown: Any
    _isMaintenanceVisible: Any
    _isRoleShown: Any
    @classmethod
    def isSuitableVehicle(cls, vehicle):
        ...
    def setCustomizationVisible(self, customizationVisible):
        ...
    def setEliteShown(self, eliteShown):
        ...
    def setLevelShown(self, levelShown):
        ...
    def setMaintenanceVisible(self, maintenanceVisible):
        ...
    def setRoleShown(self, roleShown):
        ...
    def _resolveVehicleState(self, vehicle):
        ...
    # decorador original: @hasDesiredSubMode(...)
    def __resolveStateByCurrentSubMode(self, vehicle):
        ...
