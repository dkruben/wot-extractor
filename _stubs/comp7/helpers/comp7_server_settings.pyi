# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/helpers/comp7_server_settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import copy as copy
import logging as logging
import typing as typing
from future.utils import viewitems as viewitems
import BattleReplay as BattleReplay
from Event import Event as Event
from Event import EventManager as EventManager
from comp7_common.comp7_constants import Configs as Configs
from comp7_ranks_common import Comp7Division as Comp7Division
from helpers import dependency as dependency
from helpers.server_settings import settingsBlock as settingsBlock
from shared_utils import makeTupleByDict as makeTupleByDict
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from typing import Dict as Dict, List as List, Tuple as Tuple
_logger: Any

# base nao representavel no stub: settingsBlock(...)
class _Comp7QualificationConfig:
    __slots__: tuple
    @classmethod
    def defaults(cls):
        ...

# base nao representavel no stub: settingsBlock(...)
class Comp7Config:
    __slots__: tuple
    @classmethod
    def defaults(cls):
        ...
    @classmethod
    def _preprocessData(cls, data):
        ...

# base nao representavel no stub: settingsBlock(...)
class Comp7RanksConfig:
    __slots__: tuple
    @classmethod
    def defaults(cls):
        ...
    @classmethod
    def _preprocessData(cls, data):
        ...
    @classmethod
    def __dictDivisionsToComp7Divisions(cls, divisions):
        ...

# base nao representavel no stub: settingsBlock(...)
class Comp7RewardsConfig:
    __slots__: tuple
    @classmethod
    def defaults(cls):
        ...
    def getCosts(self):
        ...

class Comp7ServerSettings(object):
    __lobbyContext: Any
    __comp7Config: Any
    __comp7RanksConfig: Any
    __comp7RewardsConfig: Any
    __serverSettings: Any
    __eventsManager: Any
    onComp7SettingsChanged: Any
    def __init__(self):
        ...
    @property
    def comp7Config(self):
        ...
    @property
    def comp7RanksConfig(self):
        ...
    @property
    def comp7RewardsConfig(self):
        ...
    def fini(self):
        ...
    def __onServerSettingsChanged(self, serverSettings):
        ...
    def __setInitValues(self):
        ...
    def __update(self, serverSettingsDiff):
        ...
    def __updateComp7(self, targetSettings):
        ...
    def __updateComp7PrestigeRanks(self, targetSettings):
        ...
    def __updateComp7Rewards(self, targetSettings):
        ...
