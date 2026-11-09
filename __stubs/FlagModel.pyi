# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/FlagModel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from Math import Matrix as Matrix
import BigWorld as BigWorld
import AnimationSequence as AnimationSequence
FlagSettings: Any

class FlagModel(object):
    model: Any
    __flagCompoundModel: Any
    __flagStaffFashion: Any
    __flagFashion: Any
    __flagAnimator: Any
    __spaceID: Any
    def __init__(self):
        ...
    def setupFlag(self, position, flagSettings, color):
        ...
    def changeFlagColor(self, color):
        ...
    def startFlagAnimation(self):
        ...
