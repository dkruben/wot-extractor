# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/BWLogicNodeTree.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Math as Math

class BWLogicalNode(object):
    localMatrix: Any
    identifier: Any
    children: Any
    def __init__(self, identifier, localMatrix):
        ...
    def addChild(self, child):
        ...
    def calcWorld(self, parentTransform, localMatrices, worldMatrices):
        ...

class BWNodeTreeTemplate(object):
    nodeList: Any
    root: Any
    def __init__(self, dataSection):
        ...
    def _loadNodes(self, dataSection):
        ...
    def processNodes(self, parentTransform, inputs):
        ...

class BWLogicalNodeTreeLocal(object):
    input: Any
    templateTree: Any
    def __init__(self, templateTree):
        ...
    def processNodes(self, parentTransform):
        ...

class BWLogicalNodeTreeLocalAndWorld(BWLogicalNodeTreeLocal):
    output: Any
    def __init__(self, templateTree):
        ...
    def processNodes(self, parentTransform):
        ...
