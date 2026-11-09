# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.


class IBattleController(object):
    __slots__: tuple
    def startControl(self, *args):
        ...
    def stopControl(self):
        ...
    def getControllerID(self):
        ...

class IBattleControllersRepository(object):
    __slots__: tuple
    @classmethod
    def create(cls, setup):
        ...
    def destroy(self):
        ...
    def getController(self, ctrlID):
        ...
    def addController(self, ctrl):
        ...
