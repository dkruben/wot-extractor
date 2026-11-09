# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/page/footer/platoon_member_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import ViewModel as ViewModel

class PlatoonMemberModel(ViewModel):
    __slots__: tuple
    READY = 'ready'
    NOT_READY = 'notReady'
    IN_BATTLE = 'inBattle'
    SEARCHING = 'searching'
    EMPTY = 'empty'
    def __init__(self, properties=1, commands=0):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def _initialize(self):
        ...
