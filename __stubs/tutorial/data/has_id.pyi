# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/tutorial/data/has_id.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any

class IHasID(object):
    def getID(self):
        ...
    def setID(self, entityID):
        ...
    def clear(self):
        ...

class IHasTargetID(object):
    def getTargetID(self):
        ...
    def setTargetID(self, targetID):
        ...

class HasID(IHasID):
    _id: Any
    _type: Any
    def __init__(self, entityID=None, entityType=0, **kwargs):
        ...
    def getID(self):
        ...
    def getType(self):
        ...
    def setID(self, entityID):
        ...

class HasTargetID(IHasTargetID):
    _targetID: Any
    def __init__(self, targetID, **kwargs):
        ...
    def getTargetID(self):
        ...
    def setTargetID(self, targetID):
        ...

class HasIDAndTarget(HasID, HasTargetID):
    _targetID: Any
    def __init__(self, entityID=None, targetID=None, entityType=0):
        ...
