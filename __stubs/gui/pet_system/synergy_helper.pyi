# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/pet_system/synergy_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
from helpers import dependency as dependency
from skeletons.gui.pet_system import IPetSystemController as IPetSystemController
from typing import Optional as Optional, Tuple as Tuple
PetID: Any
Synergy: Any
SynergyLevel: Any
SynergyProgress: Any

class SynergyItem(object):
    petController: Any
    @classmethod
    def getSynergyLevels(cls, petID=None):
        ...
    @classmethod
    def getSynergyPoints(cls, petID=None):
        ...
    @classmethod
    def getSynergyLevel(cls, petID=None):
        ...
    @classmethod
    def getSynergyProgression(cls, petID=None):
        ...
    @classmethod
    def isMaxSynergyLevel(cls, petID=None):
        ...
    @classmethod
    def isFirstClickSynergyAvailable(cls, petID=None):
        ...
