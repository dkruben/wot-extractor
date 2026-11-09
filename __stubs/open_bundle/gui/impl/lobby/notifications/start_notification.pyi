# wot-extractor: STUB (.pyi) gerado a partir de sources/res/open_bundle/scripts/client/open_bundle/gui/impl/lobby/notifications/start_notification.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers import dependency as dependency
from open_bundle.gui.impl.gen.view_models.views.lobby.notifications.start_notification_model import StartNotificationModel as StartNotificationModel
from open_bundle.gui.shared.event_dispatcher import showOpenBundleMainView as showOpenBundleMainView
from open_bundle.helpers.account_settings import setStartNotificationShown as setStartNotificationShown
from open_bundle.skeletons.open_bundle_controller import IOpenBundleController as IOpenBundleController
from gui.impl.lobby.gf_notifications.notification_base import NotificationBase as NotificationBase

class StartNotification(NotificationBase):
    __openBundle: Any
    def __init__(self, resId, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def bundleID(self):
        ...
    def _getEvents(self):
        ...
    def _canNavigate(self):
        ...
    def _update(self):
        ...
    def __onSettingsChanged(self):
        ...
    def __onStatusChanged(self, bundleID):
        ...
    def __onOpenBundle(self):
        ...
