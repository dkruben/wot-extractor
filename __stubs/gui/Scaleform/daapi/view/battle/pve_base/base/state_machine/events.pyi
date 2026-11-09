# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/base/state_machine/events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from frameworks_common.state_machine import StateEvent as StateEvent, StringEvent as StringEvent

class ToStateEvent(StringEvent):
    def __init__(self, widgetStateName, **kwargs):
        ...

class OneSecondEvent(StateEvent):
    @property
    def lastTime(self):
        ...
    @property
    def currentTime(self):
        ...
