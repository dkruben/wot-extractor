# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/marathon/example_marathon.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen import R as R
from gui.marathon.marathon_event import MarathonEvent as MarathonEvent
from gui.marathon.marathon_event_container import MarathonEventContainer as MarathonEventContainer
from gui.marathon.marathon_event_controller import marathonCreator as marathonCreator
from gui.Scaleform.locale.QUESTS import QUESTS as QUESTS

class ExampleMarathonEvent(MarathonEvent):
    @property
    def label(self):
        ...
    @property
    def tabTooltip(self):
        ...
    @property
    def entryTooltip(self):
        ...
    @property
    def tokenPrefix(self):
        ...
    @property
    def grindPostfix(self):
        ...
    @property
    def proPostfix(self):
        ...
    @property
    def finishedPostfix(self):
        ...
    @property
    def packagePrefix(self):
        ...
    @property
    def packageTemplate(self):
        ...
    @property
    def isNeedHandlingEscape(self):
        ...
    def createMarathonWebHandlers(self):
        ...

# decorador original: @marathonCreator(...)
class ExampleMarathon(MarathonEventContainer):
    prefix: Any
    tokenPrefix: Any
    packagePrefix: Any
    packageTemplate: Any
    hangarFlagName: Any
    grindPostfix: Any
    proPostfix: Any
    finishedPostfix: Any
    questsInChain: Any
    minVehicleLevel: Any
    questsPerStep: Any
    def _override(self):
        ...
