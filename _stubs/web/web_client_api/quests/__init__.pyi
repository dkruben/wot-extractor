# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/quests/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import itertools as itertools
import logging as logging
import sys as sys
import typing as typing
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from past.builtins import basestring as basestring
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES
from gui.server_events.bonuses import HIDDEN_BONUSES as HIDDEN_BONUSES
from gui.Scaleform.daapi.view.lobby.missions.cards_formatters import CardBattleConditionsFormatters as CardBattleConditionsFormatters
from gui.server_events.cond_formatters import CONDITION_SIZE as CONDITION_SIZE
from helpers import dependency as dependency, i18n as i18n
from skeletons.gui.game_control import IMarathonEventsController as IMarathonEventsController
from skeletons.gui.server_events import IEventsCache as IEventsCache
from web.web_client_api import w2c as w2c, w2capi as w2capi, Field as Field, W2CSchema as W2CSchema
from gui.server_events.event_items import Quest as Quest
from web.web_client_api.common import sanitizeResPath as sanitizeResPath
_logger: Any

class _QuestsSchema(W2CSchema):
    ids: Any

class _RequestQuestBonusSchema(W2CSchema):
    quest_id_base: Any

class _RawQuestConditionsFormatters(CardBattleConditionsFormatters):
    MAX_CONDITIONS_IN_CARD = sys.maxsize
    ICON_SIZE = CONDITION_SIZE.NORMAL
    def _getFormattedField(self, field):
        ...

# decorador original: @w2capi(...)
class QuestsWebApi(W2CSchema):
    _eventsCache: Any
    _marathonsCtrl: Any
    # decorador original: @w2c(...)
    def handleGetTokens(self, command):
        ...
    # decorador original: @w2c(...)
    def handleGetQuests(self, command):
        ...
    # decorador original: @w2c(...)
    def handleGetQuestsOld(self, command):
        ...
    # decorador original: @w2c(...)
    def handleGetStep(self, command):
        ...
    # decorador original: @w2c(...)
    def requestQuestDescr(self, cmd):
        ...

def _formatQuestConditions(quest):
    ...
def _formatQuestBonuses(quest):
    ...
def _questAsDict(quest):
    ...
