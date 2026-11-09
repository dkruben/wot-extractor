# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/hangar/vehicle_menu_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Map as Map, ViewModel as ViewModel

class VehicleMenuModel(ViewModel):
    __slots__: tuple
    DISABLED = 'disabled'
    ENABLED = 'enabled'
    WARNING = 'warning'
    CRITICAL = 'critical'
    UNAVAILABLE = 'unavailable'
    PRO_BOOST_TOOLTIP_LOCKED = 'locked'
    PRO_BOOST_TOOLTIP_ACTIVE = 'active'
    PRO_BOOST_TOOLTIP_LOCKED_ACTIVE = 'lockedActive'
    PRO_BOOST_TOOLTIP_INCOMPATIBLE_VEHICLE = 'incompatibleVehicle'
    PRO_BOOST_TOOLTIP_INCOMPATIBLE_MODE = 'incompatibleMode'
    BATTLE_NEEDED = 'battleNeeded'
    CREW_MEMBERS_RETIRED = 'crewMembersRetired'
    onNavigate: Any
    def __init__(self, properties=1, commands=1):
        ...
    def getMenuEntries(self):
        ...
    def setMenuEntries(self, value):
        ...
    @staticmethod
    def getMenuEntriesType():
        ...
    def _initialize(self):
        ...
