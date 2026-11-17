# wot-extractor: STUB (.pyi) gerado a partir de sources/res/open_bundle/scripts/client/open_bundle/gui/shared/gui_items/processors/processors.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from future.utils import viewvalues as viewvalues
from adisp import adisp_process as adisp_process, adisp_async as adisp_async
from functools import partial as partial
from gui import SystemMessages as SystemMessages
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.gf_notifications.utils import pushGFNotification as pushGFNotification
from gui.shared.gui_items.processors import Processor as Processor, makeError as makeError, plugins as plugins
from gui.shared.gui_items.processors.plugins import MessageConfirmator as MessageConfirmator
from gui.shared.money import Currency as Currency, ZERO_MONEY as ZERO_MONEY, Money as Money
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from helpers import dependency as dependency
from helpers.time_utils import getServerUTCTime as getServerUTCTime, makeLocalServerTime as makeLocalServerTime
from messenger import g_settings as g_settings
from messenger.formatters import TimeFormatter as TimeFormatter
from open_bundle.gui.constants import GFNotificationTemplates as GFNotificationTemplates
from open_bundle.helpers.resources import getTextResource as getTextResource
from open_bundle.messenger.formatters.service_channel import OpenBundleAchievesFormatter as OpenBundleAchievesFormatter
from open_bundle.skeletons.open_bundle_controller import IOpenBundleController as IOpenBundleController
from skeletons.gui.game_control import IAchievements20EarningController as IAchievements20EarningController
from skeletons.gui.impl import IGuiLoader as IGuiLoader

class _ProcessNextStepConfirmator(MessageConfirmator):
    __bundleID: Any
    __stepNumber: Any
    def __init__(self, bundleID, stepNumber):
        ...
    def _gfMakeMeta(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def _confirm(self, callback):
        ...

class ProcessNextStepProcessor(Processor):
    __giuLoader: Any
    __achievements: Any
    __openBundle: Any
    __bundleID: Any
    __stepNumber: Any
    def __init__(self, bundleID, stepNumber):
        ...
    def _request(self, callback):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def __pushCommonNotification(self, ctx, cellRewards=True):
        ...
    def __pushUnicNotification(self, ctx):
        ...
    def __preformatCompensationValue(self, rewards):
        ...
    def __getCompensationValue(self, vehicles):
        ...
