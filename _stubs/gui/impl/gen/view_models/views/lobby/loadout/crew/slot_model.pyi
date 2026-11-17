# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/loadout/crew/slot_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import Array as Array, ViewModel as ViewModel

class SlotModel(ViewModel):
    __slots__: tuple
    COMMANDER_ROLE = 'commander'
    RADIOMAN_ROLE = 'radioman'
    DRIVER_ROLE = 'driver'
    GUNNER_ROLE = 'gunner'
    LOADER_ROLE = 'loader'
    def __init__(self, properties=3, commands=0):
        ...
    def getId(self):
        ...
    def setId(self, value):
        ...
    def getTankmanId(self):
        ...
    def setTankmanId(self, value):
        ...
    def getRoles(self):
        ...
    def setRoles(self, value):
        ...
    @staticmethod
    def getRolesType():
        ...
    def _initialize(self):
        ...
