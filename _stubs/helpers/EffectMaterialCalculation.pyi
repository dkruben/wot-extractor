# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/EffectMaterialCalculation.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
import material_kinds as material_kinds
from constants import DESTRUCTIBLE_MATKIND as DESTRUCTIBLE_MATKIND, IS_EDITOR as IS_EDITOR
from DestructiblesCache import DESTR_TYPE_STRUCTURE as DESTR_TYPE_STRUCTURE
import AreaDestructibles as AreaDestructibles
SurfaceMaterial: Any

def calcSurfaceMaterialNearPoint(point, normal, spaceID, defaultEffectMaterial='ground'):
    ...
def calcEffectMaterialIndex(matKind):
    ...
def isDestructibleBroken(chunkID, itemIndex, matKind, itemFilename):
    ...
