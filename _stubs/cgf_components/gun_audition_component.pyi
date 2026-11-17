# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/gun_audition_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from Vehicular import GunAudition as GunAudition
from constants import IS_EDITOR as IS_EDITOR, IS_CGF_DUMP as IS_CGF_DUMP

class Vehicle(object):
    ...

class GunAuditionsSystem(CGF.System):
    GunAuditionActivated: Any
    VehicleAccess: Any
    Reactions: Any
    def update(self):
        ...
    def onGunAuditionAdded(self, gameObject, gunAudition, vehicleAccess):
        ...
