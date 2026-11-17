# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/event_banners/event_banners_container.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
import typing as typing
import Event as Event
from helpers import dependency as dependency
from soft_exception import SoftException as SoftException
from system_events import g_systemEvents as g_systemEvents
from typing import Dict as Dict, Type as Type
from gui.impl.lobby.user_missions.hangar_widget.event_banners.base_event_banner import BaseEventBanner as BaseEventBanner

class EventBannersContainer(object):
    _instance = None
    __eventsMap: Any
    onBannerUpdate: Any
    _initialized: Any
    def __new__(cls, *args, **kwargs):
        ...
    def __init__(self):
        ...
    @property
    def events(self):
        ...
    def registerEventBanner(self, eventBannerCls):
        ...
    def getEventBanner(self, key):
        ...
    def unregisterEventBanner(self, eventBannerCls):
        ...
    def startPersistentListening(self):
        ...
