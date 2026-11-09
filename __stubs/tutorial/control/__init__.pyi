# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/tutorial/control/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from helpers.aop import Weaver as Weaver
from tutorial.logger import LOG_ERROR as LOG_ERROR
from tutorial.data.effects import EFFECT_TYPE_NAMES as EFFECT_TYPE_NAMES
from tutorial.data.conditions import CONDITION_TYPE as CONDITION_TYPE
g_tutorialWeaver: Any

class TutorialProxyHolder(object):
    _tutorial = None
    @property
    def _gui(self):
        ...
    @property
    def _data(self):
        ...
    @property
    def _funcChapterCtx(self):
        ...
    @property
    def _cache(self):
        ...
    @property
    def _bonuses(self):
        ...
    @property
    def _sound(self):
        ...
    @property
    def _descriptor(self):
        ...
    @property
    def _funcScene(self):
        ...
    @property
    def _ctrlFactory(self):
        ...

class ContentQuery(TutorialProxyHolder):
    def invoke(self, content, varID):
        ...
    def getVar(self, varID, default=None):
        ...

class ControlsFactory(object):
    _funcEffects: Any
    _contentQueries: Any
    _customFuncConditions: Any
    def __init__(self, funcEffects, contentQueries, customFuncConditions=None):
        ...
    def createBonuses(self, completed):
        ...
    def createSoundPlayer(self):
        ...
    def createFuncScene(self, sceneModel):
        ...
    def createFuncChapterCtx(self):
        ...
    def createContentQuery(self, name):
        ...
    def createFuncEffect(self, effect):
        ...
    def createFuncEffects(self, effects):
        ...
    def createCustomFuncCondition(self, condition):
        ...

def setTutorialProxy(tutorial):
    ...
def clearTutorialProxy():
    ...
def getServerSettings():
    ...
