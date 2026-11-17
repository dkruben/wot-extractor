# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/e_sport/unit/actions_handler.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from PlayerEvents import g_playerEvents as g_playerEvents
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui import DialogsInterface as DialogsInterface, SystemMessages as SystemMessages
from gui.Scaleform.daapi.view.dialogs import rally_dialog_meta as rally_dialog_meta
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.entities.base import vehicleAmmoCheck as vehicleAmmoCheck
from gui.prb_control.entities.base.unit.actions_handler import UnitActionsHandler as UnitActionsHandler
from gui.prb_control.entities.base.unit.ctx import BattleQueueUnitCtx as BattleQueueUnitCtx, AutoSearchUnitCtx as AutoSearchUnitCtx
from gui.prb_control.settings import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG

class ESportActionsHandler(UnitActionsHandler):
    def __init__(self, entity):
        ...
    def executeInit(self, ctx):
        ...
    # decorador original: @vehicleAmmoCheck
    def execute(self):
        ...
    def clear(self):
        ...
    def showGUI(self):
        ...
    def __onKickedFromQueue(self):
        ...
