# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/armor_inspector_common/models.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from dict2model import models as models

class ArmorInspectorConfigModel(models.Model):
    __slots__: tuple
    enabled: Any
    linkButtonURL: Any
    disabledVehicle: Any
    def __init__(self, enabled, linkButtonURL, disabledVehicle):
        ...
    def _reprArgs(self):
        ...
    def isDisabledForVehicle(self, vehicleName):
        ...
