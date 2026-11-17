# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/base/squad/mixins.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.prb_control.entities.base.squad.components import SquadRestrictionsProvider as SquadRestrictionsProvider

class SquadRestrictionsMixin(object):
    __squadRestrictionsProvider: Any
    def __init__(self):
        ...
    def initRestrictedRoleDataProvider(self, unit):
        ...
    def finiRestrictedRoleDataProvider(self):
        ...
    def isSquadRestrictionValid(self):
        ...
    def isVehicleSuitableForSquad(self, vehicle):
        ...
    def hasSlotForVehicle(self, vehicle):
        ...
    @property
    def squadRestrictions(self):
        ...
    @classmethod
    def _createSquadRestrictionsProvider(cls):
        ...
