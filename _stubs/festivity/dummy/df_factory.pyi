# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/festivity/dummy/df_factory.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from festivity.dummy.df_controller import DummyController as DummyController
from festivity.dummy.df_processor import DummyCommandsProcessor as DummyCommandsProcessor
from festivity.dummy.df_requester import DummyRequester as DummyRequester
from skeletons.festivity_factory import IFestivityFactory as IFestivityFactory

class DummyFactory(IFestivityFactory):
    __requester: Any
    __processor: Any
    __controller: Any
    def __init__(self):
        ...
    def getRequester(self):
        ...
    def getProcessor(self):
        ...
    def getController(self):
        ...
