# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/perk_context_impl_base.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from visual_script.misc import ASPECT as ASPECT

class PerkContextImplBase(object):
    _perksController: Any
    _perkLevel: Any
    perkID: Any
    scopeID: Any
    vehicleID: Any
    def __init__(self, perksControllerWeakRef, perkID, perkLevel, scopeID):
        ...
    @property
    def vehicle(self):
        ...
    @property
    def perkLevel(self):
        ...
    @perkLevel.setter
    def perkLevel(self, value):
        ...
    def addFactorModifier(self, factor, value):
        ...
    def removeFactorModifiers(self, factor, numMods):
        ...
    def dropAllPerkModifiers(self):
        ...
    def notifyOnClient(self, *_):
        ...
    def notifyOnClientRibbon(self, *_):
        ...

class CrewContextImplBase(PerkContextImplBase):
    ASPECT = ASPECT.ALL
    _levelOverride: Any
    _tmanIdxs: Any
    def __init__(self, perksControllerWeakRef, perkID, perkLevel, scopeID, tmanIdxs):
        ...
