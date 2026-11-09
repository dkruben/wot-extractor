# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/training/legacy/permissions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import PREBATTLE_ROLE as PREBATTLE_ROLE
from gui.prb_control.entities.base.legacy.permissions import LegacyPermissions as LegacyPermissions, ILegacyPermissions as ILegacyPermissions

class TrainingPermissions(LegacyPermissions):
    def canChangeVehicle(self):
        ...
    def canCreateSquad(self):
        ...
    @classmethod
    def isCreator(cls, roles):
        ...
    def canChangeSetting(self):
        ...
    def canStartBattle(self):
        ...

class TrainingIntroPermissions(ILegacyPermissions):
    def canCreateSquad(self):
        ...
