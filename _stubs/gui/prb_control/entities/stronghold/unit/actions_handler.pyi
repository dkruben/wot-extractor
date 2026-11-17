# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/stronghold/unit/actions_handler.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.prb_control.entities.base.external_battle_unit.base_external_battle_ctx import StopPlayersMatchingBaseExternalUnitCtx as StopPlayersMatchingBaseExternalUnitCtx
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.entities.base.unit.actions_handler import UnitActionsHandler as UnitActionsHandler
from gui.prb_control.entities.base.unit.ctx import BattleQueueUnitCtx as BattleQueueUnitCtx

class StrongholdActionsHandler(UnitActionsHandler):
    def showGUI(self):
        ...
    def exitFromQueue(self):
        ...
    def _canDoAutoSearch(self, unit, stats):
        ...
    def _sendBattleQueueRequest(self, vInvID=0, action=1):
        ...
    def exitFromPlayersMatchingMode(self):
        ...
