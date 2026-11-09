# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/rally/BaseRallyView.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui.Scaleform.daapi.view.meta.BaseRallyViewMeta import BaseRallyViewMeta as BaseRallyViewMeta
from gui.prb_control.entities.base.cooldown import getPrbRequestCoolDown as getPrbRequestCoolDown
from gui.prb_control.entities.base.ctx import LeavePrbAction as LeavePrbAction
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared import events as events, g_eventBus as g_eventBus
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.utils.MethodsRules import MethodsRules as MethodsRules

class BaseRallyView(BaseRallyViewMeta, IGlobalListener, MethodsRules):
    def setData(self, initialData):
        ...
    def getCoolDownRequests(self):
        ...
    # decorador original: @MethodsRules.delayable(...)
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _handleSetPrebattleCoolDown(self, event):
        ...
    def _checkCoolDowns(self):
        ...
    def _doLeave(self, isExit=True):
        ...
    # decorador original: @MethodsRules.delayable(...)
    def _startListening(self):
        ...
    def _stopListening(self):
        ...
