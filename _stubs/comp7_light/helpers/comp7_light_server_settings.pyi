# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/helpers/comp7_light_server_settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
from future.utils import viewitems as viewitems
from shared_utils import makeTupleByDict as makeTupleByDict
import BattleReplay as BattleReplay
from Event import Event as Event
from Event import EventManager as EventManager
from comp7_light_constants import Configs as Configs
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_logger: Any

# base nao representavel no stub: namedtuple(...)
class _Comp7LightConfig:
    __slots__: tuple
    def __new__(cls, **kwargs):
        ...
    def asDict(self):
        ...
    def replace(self, data):
        ...
    @classmethod
    def defaults(cls):
        ...

class Comp7LightServerSettings(object):
    __lobbyContext: Any
    __comp7LightConfig: Any
    __serverSettings: Any
    __eventsManager: Any
    onServerSettingsChanged: Any
    def __init__(self):
        ...
    @property
    def comp7LightConfig(self):
        ...
    def fini(self):
        ...
    def __onServerSettingsChanged(self, serverSettings):
        ...
    def __setInitialValues(self):
        ...
    def __update(self, serverSettingsDiff):
        ...
