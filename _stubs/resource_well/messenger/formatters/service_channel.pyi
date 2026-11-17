# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/messenger/formatters/service_channel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from helpers import dependency as dependency, time_utils as time_utils
from messenger import g_settings as g_settings
from messenger.formatters import TimeFormatter as TimeFormatter
from messenger.formatters.service_channel import WaitItemsSyncFormatter as WaitItemsSyncFormatter
from messenger.formatters.service_channel_helpers import MessageData as MessageData
from resource_well.gui.feature.constants import PurchaseMode as PurchaseMode
from resource_well.notification.decorators import ResourceWellLockButtonDecorator as ResourceWellLockButtonDecorator
from skeletons.gui.resource_well import IResourceWellController as IResourceWellController

class ResourceWellRewardFormatter(WaitItemsSyncFormatter):
    __TEMPLATE = 'ResourceWellRewardReceivedMessage'
    __R_MESSAGES = R.strings.messenger.serviceChannelMessages.resourceWell.reward
    __resourceWell: Any
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    def __getMainMessage(self, rewardID, message):
        ...
    def __getAdditionalMessage(self, rewardID, message):
        ...

class ResourceWellNoVehiclesFormatter(WaitItemsSyncFormatter):
    __TEMPLATE = 'ResourceWellNoVehiclesMessage'
    __BUTTON_TEMPLATE = 'ResourceWellNoVehiclesWithButtonMessage'
    __R_MESSAGES = R.strings.messenger.serviceChannelMessages.resourceWell
    __resourceWell: Any
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
