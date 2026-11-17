# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/veh_skill_tree/path_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class LineType(Enum):
    LEFTTORIGHT = 'leftToRight'
    RIGHTTOLEFT = 'rightToLeft'
    TOPTOBOTTOM = 'topToBottom'
    BOTTOMTOTOP = 'bottomToTop'
    LEFTTOBOTTOM = 'leftToBottom'
    BOTTOMTOLEFT = 'bottomToLeft'
    LEFTTOTOP = 'leftToTop'
    TOPTOLEFT = 'topToLeft'
    TOPTORIGHT = 'topToRight'
    RIGHTTOTOP = 'rightToTop'
    RIGHTTOBOTTOM = 'rightToBottom'
    BOTTOMTORIGHT = 'bottomToRight'

class PathModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=2, commands=0):
        ...
    def getId(self):
        ...
    def setId(self, value):
        ...
    def getLineType(self):
        ...
    def setLineType(self, value):
        ...
    def _initialize(self):
        ...
