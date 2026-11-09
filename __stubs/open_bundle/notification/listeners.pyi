# wot-extractor: STUB (.pyi) gerado a partir de sources/res/open_bundle/scripts/client/open_bundle/notification/listeners.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import uuid as uuid
from gui.impl import backport as backport
from gui.impl.lobby.gf_notifications.cache import getCache as getCache
from helpers import dependency as dependency
from helpers.time_utils import getServerUTCTime as getServerUTCTime, makeLocalServerTime as makeLocalServerTime, ONE_DAY as ONE_DAY
from messenger.formatters import TimeFormatter as TimeFormatter
from notification.listeners import _NotificationListener as _NotificationListener
from open_bundle.gui.constants import GFNotificationTemplates as GFNotificationTemplates
from open_bundle.helpers.account_settings import isReminderNotificationShown as isReminderNotificationShown, isStartNotificationShown as isStartNotificationShown, setReminderNotificationShown as setReminderNotificationShown
from open_bundle.helpers.resources import getTextResource as getTextResource
from open_bundle.notification.decorators import OpenBundleStartDecorator as OpenBundleStartDecorator, OpenBundleReminderDecorator as OpenBundleReminderDecorator
from open_bundle.skeletons.open_bundle_controller import IOpenBundleController as IOpenBundleController

class OpenBundleListener(_NotificationListener):
    __openBundle: Any
    __ENTITY_ID = 0
    __openingCtx: Any
    def __init__(self):
        ...
    def start(self, model):
        ...
    def stop(self):
        ...
    def __tryNotify(self):
        ...
    def __onStatusChanged(self, bundleID):
        ...
    def __pushEventNotification(self, bundleID):
        ...
    def __pushStartNotification(self, bundleID):
        ...
    def __pushReminderNotification(self, bundleID):
        ...
