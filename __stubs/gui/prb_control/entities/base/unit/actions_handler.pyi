# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/base/unit/actions_handler.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import weakref as weakref
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui import DialogsInterface as DialogsInterface
from gui.Scaleform.daapi.view.dialogs import rally_dialog_meta as rally_dialog_meta
from gui.prb_control.entities.base import checkVehicleAmmoFull as checkVehicleAmmoFull
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.entities.base.unit.ctx import BattleQueueUnitCtx as BattleQueueUnitCtx, AutoSearchUnitCtx as AutoSearchUnitCtx
from gui.prb_control.settings import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
from wg_async import await_callback as await_callback, wg_async as wg_async
from gui.prb_control.entities.base.unit.entity import BaseUnitEntity as BaseUnitEntity

class AbstractActionsHandler(object):
    _entity: Any
    def __init__(self, entity):
        ...
    def showGUI(self):
        ...
    def setPlayerInfoChanged(self):
        ...
    def setPlayersChanged(self):
        ...
    def setUnitChanged(self, loadHangar=False):
        ...
    def executeInit(self, ctx):
        ...
    def executeFini(self):
        ...
    def executeRestore(self):
        ...
    def execute(self):
        ...
    def clear(self):
        ...
    def exitFromQueue(self):
        ...
    def _sendBattleQueueRequest(self, vInvID=0, action=1):
        ...

class UnitActionsHandler(AbstractActionsHandler):
    def executeInit(self, ctx):
        ...
    def executeFini(self):
        ...
    # decorador original: @wg_async
    def execute(self):
        ...
    def _canDoAutoSearch(self, unit, stats):
        ...
