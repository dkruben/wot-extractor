# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/seniority_awards/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/seniority_awards/__init__.py
from __future__ import absolute_import
from gui.impl.gen import R
from gui.impl.lobby.gf_notifications import GFNotificationTemplates
from gui.impl.lobby.seniority_awards.notifications.available_tokens_notification import AvailableTokensNotification
from gui.impl.lobby.seniority_awards.notifications.manual_claim_notification import ManualClaimNotification
from gui.impl.lobby.seniority_awards.notifications.vehicle_selection_notification import VehicleSelectionNotification
from gui.shared.system_factory import registerGamefaceNotifications
registerGamefaceNotifications({(GFNotificationTemplates.SENIORITY_AWARD_TOKENS_NOTIFICATION): (
                                                                 R.views.mono.seniority_awards.notifications.tokens(), AvailableTokensNotification), 
   (GFNotificationTemplates.SENIORITY_AWARD_VEHICLE_SELECTION_NOTIFICATION): (
                                                                            R.views.mono.seniority_awards.notifications.vehicles(), VehicleSelectionNotification), 
   (GFNotificationTemplates.SENIORITY_AWARD_MANUAL_CLAIM_NOTIFICATION): (
                                                                       R.views.mono.seniority_awards.notifications.manual_claim(), ManualClaimNotification)})
