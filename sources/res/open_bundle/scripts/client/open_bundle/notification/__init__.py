# wot-extractor: codigo DESCOMPILADO de sources/res/open_bundle/scripts/client/open_bundle/notification/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: open_bundle/scripts/client/open_bundle/notification/__init__.py
from __future__ import absolute_import
from open_bundle.gui.constants import GFNotificationTemplates
from open_bundle.gui.impl.lobby.notifications.start_notification import StartNotification
from open_bundle.gui.impl.lobby.notifications.special_rewards_notification import SpecialRewardsNotification
from open_bundle.notification.listeners import OpenBundleListener
from open_bundle.notification.actions_handlers import OpenBundleReminderHandler
from gui.shared.system_factory import registerGamefaceNotifications, registerNotificationsActionsHandlers, registerNotificationsListeners
from gui.impl.gen import R
__NOTIFICATION_LAYOUT = R.views.open_bundle.mono.lobby.notifications

def registerOpenBundleNotifications():
    registerNotificationsListeners((OpenBundleListener,))
    registerNotificationsActionsHandlers((OpenBundleReminderHandler,))
    registerGamefaceNotifications({(GFNotificationTemplates.START_NOTIFICATION): (
                                                    __NOTIFICATION_LAYOUT.start_notification(), StartNotification), 
       (GFNotificationTemplates.SPECIAL_REWARDS_NOTIFICATION): (
                                                              __NOTIFICATION_LAYOUT.special_rewards_notification(), SpecialRewardsNotification)})
