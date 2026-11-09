# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/tournament/unit/requester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_process as adisp_process
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.prb_control import settings as settings, prb_getters as prb_getters
from gui.prb_control.entities.base.ctx import PrbCtrlRequestCtx as PrbCtrlRequestCtx
from gui.prb_control.entities.base.requester import IUnitRequestProcessor as IUnitRequestProcessor
from helpers import dependency as dependency
from skeletons.gui.web import IWebController as IWebController
from soft_exception import SoftException as SoftException
from gui.wgcg.tournament.contexts import TournamentJoinBattleCtx as TournamentJoinBattleCtx, TournamentLeaveModeCtx as TournamentLeaveModeCtx, TournamentMatchmakingInfoCtx as TournamentMatchmakingInfoCtx, TournamentAssignCtx as TournamentAssignCtx, TournamentUnassignCtx as TournamentUnassignCtx, TournamentChangeOpenedCtx as TournamentChangeOpenedCtx, TournamentSetVehicleCtx as TournamentSetVehicleCtx, TournamentSetReadyCtx as TournamentSetReadyCtx, TournamentKickPlayerCtx as TournamentKickPlayerCtx, TournamentBattleQueueCtx as TournamentBattleQueueCtx, TournamentGiveLeadershipCtx as TournamentGiveLeadershipCtx, TournamentSendInvitesCtx as TournamentSendInvitesCtx, TournamentSetSlotVehicleTypeFilter as TournamentSetSlotVehicleTypeFilter, TournamentSetSlotVehiclesFilter as TournamentSetSlotVehiclesFilter, TournamentStopPlayersMatchingCtx as TournamentStopPlayersMatchingCtx

class TournamentUnitRequestProcessor(IUnitRequestProcessor):
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
