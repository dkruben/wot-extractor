# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/gf_notifications/notification_base.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.pub import ViewImpl as ViewImpl
from PlayerEvents import g_playerEvents as g_playerEvents
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.impl.lobby.gf_notifications.cache import getCache as getCache
from gui.prb_control.entities.base.listener import IPrbListener as IPrbListener
from gui.shared import g_eventBus as g_eventBus
from gui.shared.events import HidePopoverEvent as HidePopoverEvent

class NotificationBase(ViewImpl, IPrbListener):
    __slots__: tuple
    _isPopUp: Any
    _linkageData: Any
    def __init__(self, resId, model, *args, **kwargs):
        ...
    @property
    def linkageData(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _update(self):
        ...
    def _getEvents(self):
        ...
    def _finalize(self):
        ...
    def _getPayload(self):
        ...
    def _canNavigate(self):
        ...
    def _closeNotificationCenter(self):
        ...
    def __updatePrebattleControls(self, *_):
        ...
