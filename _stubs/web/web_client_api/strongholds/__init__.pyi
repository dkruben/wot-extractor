# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/strongholds/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
from past.builtins import long as long
from adisp import adisp_process as adisp_process
from constants import JOIN_FAILURE as JOIN_FAILURE, PREBATTLE_TYPE as PREBATTLE_TYPE
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from helpers import dependency as dependency
from gui import DialogsInterface as DialogsInterface
from gui.SystemMessages import pushMessage as pushMessage, SM_TYPE as SM_TYPE
from gui.prb_control.dispatcher import g_prbLoader as g_prbLoader
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction, LeavePrbAction as LeavePrbAction
from gui.prb_control.entities.base.external_battle_unit.base_external_battle_ctx import CreateBaseExternalUnitCtx as CreateBaseExternalUnitCtx, JoinBaseExternalUnitCtx as JoinBaseExternalUnitCtx
from gui.prb_control.formatters import messages as messages
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from gui.shared import actions as actions
from gui.shared.items_parameters import params_helper as params_helper, formatters as formatters
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.game_control import IReloginController as IReloginController
from skeletons.gui.shared import IItemsCache as IItemsCache
from web.web_client_api import w2capi as w2capi, w2c as w2c, W2CSchema as W2CSchema, Field as Field
_logger: Any

class _StrongholdsJoinBattleSchema(W2CSchema):
    unit_id: Any
    periphery_id: Any

class _GetReserveParamsSchema(W2CSchema):
    reserve_intCDs: Any

# decorador original: @w2capi(...)
class StrongholdsWebApi(object):
    __itemsCache: Any
    __connectionMgr: Any
    # decorador original: @w2c(...)
    # decorador original: @adisp_process
    def handleOpenList(self, cmd):
        ...
    # decorador original: @w2c(...)
    # decorador original: @adisp_process
    def handleLeaveMode(self, cmd):
        ...
    # decorador original: @w2c(...)
    # decorador original: @adisp_process
    def handleBattleChosen(self, cmd):
        ...
    # decorador original: @w2c(...)
    # decorador original: @adisp_process
    def handleJoinBattle(self, cmd):
        ...
    # decorador original: @w2c(...)
    def getReserveParams(self, cmd):
        ...
    # decorador original: @w2c(...)
    def getAvailablePeripheries(self, _):
        ...
