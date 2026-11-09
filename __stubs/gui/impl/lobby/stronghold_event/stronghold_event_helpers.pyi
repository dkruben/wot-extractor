# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/stronghold_event/stronghold_event_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
from typing import Optional as Optional, TYPE_CHECKING as TYPE_CHECKING, Any as Any
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import StrongholdEvent as StrongholdEvent
from gui.Scaleform.daapi.view.lobby.clans.clan_helpers import getStrongholdEventEnabled as getStrongholdEventEnabled
from gui.clans.clan_cache import g_clanCache as g_clanCache
from gui.clans.data_wrapper.stronghold_event import StrongholdEventSettingsData as StrongholdEventSettingsData
_logger: _Any
DEFAULT_EVENT_NAME = 'default_stronghold_event_name'

def getStrongholdEventName(useDefault=True):
    ...
def getSettings(settingName, defaultValue=None):
    ...
def setSettings(settingName, value):
    ...
def isStrongholdEventBannerAvailable():
    ...
