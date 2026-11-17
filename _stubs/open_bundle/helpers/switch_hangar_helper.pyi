# wot-extractor: STUB (.pyi) gerado a partir de sources/res/open_bundle/scripts/client/open_bundle/helpers/switch_hangar_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from helpers import dependency as dependency
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, g_eventBus as g_eventBus, events as events

class SwitchHangarHelper(IGlobalListener):
    __hangarSpace: Any
    __actionOnModeSwitched: Any
    def __init__(self):
        ...
    def stop(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def selectRandomBattle(self, callback):
        ...
    def isRandomPrbActive(self):
        ...
    def __tryCallAction(self):
        ...
