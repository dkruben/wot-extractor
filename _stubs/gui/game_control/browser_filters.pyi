# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/browser_filters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.shared import g_eventBus as g_eventBus
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showPersonalMissionCampaignSelectorWindow as showPersonalMissionCampaignSelectorWindow
from gui.shared.events import LoadViewEvent as LoadViewEvent, OpenLinkEvent as OpenLinkEvent
BrowserFilterResult: Any

def getFilters():
    ...
def _onShowInExternalBrowser(url, tags):
    ...
def _onGoToHangar(url, tags):
    ...
def _onGoToMissions(url, tags):
    ...
def _onGoToPersonalMissions(url, tags):
    ...
