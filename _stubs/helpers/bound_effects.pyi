# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/bound_effects.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
from future.utils import listitems as listitems
import BigWorld as BigWorld
import helpers as helpers
from helpers.EffectsList import EffectsListPlayer as EffectsListPlayer

class StaticSceneBoundEffects(object):
    _models: Any
    __incrementalEffectID: Any
    _matProv: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def addNew(self, position, effectsList, keyPoints, callbackOnStop, **args):
        ...
    def stop(self, effectID):
        ...
    def __callbackBeforeDestroy(self, effectID, callbackOnStop):
        ...

class ModelBoundEffects(object):
    __model: Any
    _effects: Any
    def __init__(self, model):
        ...
    def destroy(self):
        ...
    def stop(self, forceDelete=False):
        ...
    def addNew(self, matProv, effectsList, keyPoints, waitForKeyOff=False, **args):
        ...
    def addNewToNode(self, node, matProv, effectsList, keyPoints, waitForKeyOff=False, excludeTags=None, **args):
        ...
    def reattachTo(self, model):
        ...
