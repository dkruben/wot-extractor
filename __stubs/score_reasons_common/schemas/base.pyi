# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/common/score_reasons_common/schemas/base.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import List as List
from dict2model import fields as fields, models as models, schemas as schemas, validate as validate
scoreReasonSchema: Any
ScopeSchema: Any
ExtensionSchema: Any

class ScoreReasonModel(models.Model):
    __slots__: tuple
    name: Any
    def __init__(self, name):
        ...
    def _reprArgs(self):
        ...

class ScopeType(object):
    TEAM = 'team'
    VEHICLE = 'vehicle'

class ScopeModel(models.Model):
    __slots__: tuple
    scopeType: Any
    reason: Any
    def __init__(self, scopeType, reason):
        ...
    def _reprArgs(self):
        ...

class ExtensionModel(models.Model):
    __slots__: tuple
    name: Any
    scope: Any
    def __init__(self, name, scope):
        ...
    def _reprArgs(self):
        ...
