# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/relogin_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from helpers import dependency as dependency
from skeletons.gui.game_control import IReloginController as IReloginController
from skeletons.helpers.statistics import IStatisticsCollector as IStatisticsCollector
_logger: Any

class ReloginController(IReloginController):
    statsCollector: Any
    __reloginChain: Any
    __reloginStoppedHandler: Any
    def __init__(self):
        ...
    @property
    def isActive(self):
        ...
    def fini(self):
        ...
    def doRelogin(self, peripheryID, onStoppedHandler=None, extraChainSteps=None):
        ...
    def __onReloginStopped(self, isCompleted):
        ...
    def __clearReloginChain(self):
        ...
