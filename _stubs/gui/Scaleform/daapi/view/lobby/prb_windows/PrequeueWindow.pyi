# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/prb_windows/PrequeueWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from adisp import adisp_process as adisp_process
from gui.Scaleform.daapi.view.meta.PrequeueWindowMeta import PrequeueWindowMeta as PrequeueWindowMeta
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.managers.windows_stored_data import DATA_TYPE as DATA_TYPE, TARGET_ID as TARGET_ID
from gui.Scaleform.managers.windows_stored_data import stored_window as stored_window
from gui.prb_control.entities.base.ctx import LeavePrbAction as LeavePrbAction
from gui.prb_control.entities.base.pre_queue.listener import IPreQueueListener as IPreQueueListener
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from messenger.gui.Scaleform.view.lobby import MESSENGER_VIEW_ALIAS as MESSENGER_VIEW_ALIAS

# decorador original: @stored_window(...)
class PrequeueWindow(PrequeueWindowMeta, IPreQueueListener):
    __queueName: Any
    def __init__(self, queueName='prequeue'):
        ...
    def onWindowClose(self):
        ...
    def onWindowMinimize(self):
        ...
    def requestToEnqueue(self):
        ...
    def requestToLeave(self):
        ...
    def showFAQWindow(self):
        ...
    def isEnqueueBtnEnabled(self):
        ...
    def isLeaveBtnEnabled(self):
        ...
    def startListening(self):
        ...
    def stopListening(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _handleCurrentVehicleChanged(self):
        ...
    # decorador original: @adisp_process
    def _doLeave(self, isExit=True):
        ...
