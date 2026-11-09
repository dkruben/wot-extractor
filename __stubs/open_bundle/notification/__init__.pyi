# wot-extractor: STUB (.pyi) gerado a partir de sources/res/open_bundle/scripts/client/open_bundle/notification/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from open_bundle.gui.constants import GFNotificationTemplates as GFNotificationTemplates
from open_bundle.gui.impl.lobby.notifications.start_notification import StartNotification as StartNotification
from open_bundle.gui.impl.lobby.notifications.special_rewards_notification import SpecialRewardsNotification as SpecialRewardsNotification
from open_bundle.notification.listeners import OpenBundleListener as OpenBundleListener
from open_bundle.notification.actions_handlers import OpenBundleReminderHandler as OpenBundleReminderHandler
from gui.shared.system_factory import registerGamefaceNotifications as registerGamefaceNotifications, registerNotificationsActionsHandlers as registerNotificationsActionsHandlers, registerNotificationsListeners as registerNotificationsListeners
from gui.impl.gen import R as R
__NOTIFICATION_LAYOUT = R.views.open_bundle.mono.lobby.notifications

def registerOpenBundleNotifications():
    ...
