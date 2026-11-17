# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/tutorial/control/sales/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from tutorial.control import ControlsFactory as ControlsFactory
from tutorial.control import context as core_ctx
from tutorial.control.sales import functional as functional
from tutorial.data.effects import EFFECT_TYPE as EFFECT_TYPE
from tutorial.control import functional as core_func

class SalesControlsFactory(ControlsFactory):
    def __init__(self):
        ...
    def createSoundPlayer(self):
        ...
    def createFuncScene(self, sceneModel):
        ...
    def createFuncChapterCtx(self):
        ...
    def createBonuses(self, completed):
        ...

class SalesBonusesRequester(core_ctx.BonusesRequester):
    def request(self, chapterID=None):
        ...
