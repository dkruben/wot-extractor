# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/battle_pass/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from itertools import chain as chain
from future.utils import viewitems as viewitems
from past.builtins import basestring as basestring
from gui.impl.gen import R as R
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events, g_eventBus as g_eventBus
from gui.shared.event_dispatcher import showBattlePass as showBattlePass, showBattlePassTankmenVoiceover as showBattlePassTankmenVoiceover, showShop as showShop
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from web.common import formatBattlePassInfo as formatBattlePassInfo
from web.web_client_api import Field as Field, W2CSchema as W2CSchema, WebCommandException as WebCommandException, w2c as w2c, w2capi as w2capi
_logger: Any
_R_VIEWS = R.aliases.battle_pass
_VIEWS_IDS: dict
_VIEWS_COMMANDS: dict

class _ShowViewSchema(W2CSchema):
    id: Any
    chapter_id: Any
    tankman: Any

# decorador original: @w2capi(...)
class BattlePassWebApi(W2CSchema):
    __battlePass: Any
    # decorador original: @w2c(...)
    def handleShowView(self, cmd):
        ...
    # decorador original: @w2c(...)
    def handleGetInfo(self, _):
        ...
    # decorador original: @w2c(...)
    def finishBattlePassPurchase(self, _):
        ...
    def __getTankmenScreenID(self, groupName):
        ...

class BattlePassWebApiMixin(object):
    # decorador original: @w2c(...)
    def openBattlePassMainProgression(self, _):
        ...
    # decorador original: @w2c(...)
    def openBattlePassMainWithBuy(self, _):
        ...
    # decorador original: @w2c(...)
    def openBattlePassMainWithBuyLevels(self, _):
        ...

def _isValidViewID(_, data):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _isValidChapterID(_, data, battlePass):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _isValidTankman(_, data, battlePass):
    ...
