# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/stronghold/unit/requester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from adisp import adisp_process as adisp_process
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.prb_control import settings as settings, prb_getters as prb_getters
from gui.prb_control.entities.base.ctx import PrbCtrlRequestCtx as PrbCtrlRequestCtx
from gui.prb_control.entities.base.requester import IUnitRequestProcessor as IUnitRequestProcessor
from gui.wgcg.strongholds.contexts import StrongholdLeaveCtx as StrongholdLeaveCtx, StrongholdAssignCtx as StrongholdAssignCtx, StrongholdChangeOpenedCtx as StrongholdChangeOpenedCtx, StrongholdSetVehicleCtx as StrongholdSetVehicleCtx, StrongholdSetReadyCtx as StrongholdSetReadyCtx, StrongholdKickPlayerCtx as StrongholdKickPlayerCtx, StrongholdBattleQueueCtx as StrongholdBattleQueueCtx, StrongholdGiveLeadershipCtx as StrongholdGiveLeadershipCtx, StrongholdSetReserveCtx as StrongholdSetReserveCtx, StrongholdSendInvitesCtx as StrongholdSendInvitesCtx, StrongholdUnassignCtx as StrongholdUnassignCtx, StrongholdUnsetReserveCtx as StrongholdUnsetReserveCtx, StrongholdJoinBattleCtx as StrongholdJoinBattleCtx, StrongholdSetEquipmentCommanderCtx as StrongholdSetEquipmentCommanderCtx, StrongholdMatchmakingInfoCtx as StrongholdMatchmakingInfoCtx, StrongholdSetSlotVehicleTypeFilter as StrongholdSetSlotVehicleTypeFilter, StrongholdStopPlayersMatchingCtx as StrongholdStopPlayersMatchingCtx, StrongholdSetSlotVehiclesFilter as StrongholdSetSlotVehiclesFilter
from helpers import dependency as dependency
from skeletons.gui.web import IWebController as IWebController
from soft_exception import SoftException as SoftException

class StrongholdUnitRequestProcessor(IUnitRequestProcessor):
    clansCtrl: Any
    __unitContextRemap: Any
    def init(self):
        ...
    def fini(self):
        ...
    def doRequest(self, ctx, methodName, *args, **kwargs):
        ...
    def doRequestChain(self, ctx, chain):
        ...
    def doRawRequest(self, methodName, *args, **kwargs):
        ...
    # decorador original: @adisp_process
    def _sendRequest(self, ctx, methodName, chain, callback, *args, **kwargs):
        ...
    def _sendNextRequest(self, ctx, chain):
        ...
