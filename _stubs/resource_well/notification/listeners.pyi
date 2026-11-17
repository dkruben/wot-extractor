# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/notification/listeners.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from typing import Optional as Optional
from gui import SystemMessages as SystemMessages
from gui.SystemMessages import SM_TYPE as SM_TYPE
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from helpers import dependency as dependency
from notification.listeners import _NotificationListener as _NotificationListener
from resource_well.gui.feature.constants import PurchaseMode as PurchaseMode
from resource_well.gui.feature.resource_well_helpers import isStartNotificationShown as isStartNotificationShown, isFinishNotificationShown as isFinishNotificationShown, setStartNotificationShown as setStartNotificationShown, setFinishNotificationShown as setFinishNotificationShown
from resource_well.notification.decorators import ResourceWellStartDecorator as ResourceWellStartDecorator
from shared_utils import first as first
from skeletons.gui.resource_well import IResourceWellController as IResourceWellController
_logger: Any

class ResourceWellListener(_NotificationListener):
    __RESOURCE_WELL_MESSAGES = R.strings.messenger.serviceChannelMessages.resourceWell
    __START_ENTITY_ID = 0
    __resourceWell: Any
    __prevIsEnabled: Any
    __prevIsFinished: Any
    def __init__(self):
        ...
    def start(self, model):
        ...
    def stop(self):
        ...
    def __onEventStateUpdated(self):
        ...
    def __tryNotify(self):
        ...
    def __checkPause(self):
        ...
    def __pushPaused(self):
        ...
    def __pushEnabled(self):
        ...
    def __pushStarted(self):
        ...
    def __getSingleVehicleText(self):
        ...
    def __getTwoVehiclesText(self):
        ...
    def __pushFinished(self):
        ...
