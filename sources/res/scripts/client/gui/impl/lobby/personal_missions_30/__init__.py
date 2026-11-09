# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/personal_missions_30/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/personal_missions_30/__init__.py
from __future__ import absolute_import
from frameworks.wulf import WindowLayer
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ViewSettings, ScopeTemplates
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.app_loader import settings as app_settings
from gui.shared import EVENT_BUS_SCOPE

def getStateMachineRegistrators():
    from gui.impl.lobby.personal_missions_30.state import registerTransitions, registerStates
    return (
     registerStates, registerTransitions)


def getViewSettings():
    from gui.impl.lobby.personal_missions_30.campaign_selector_view import CampaignSelectorWindow
    from gui.impl.lobby.personal_missions_30.main_view import PersonalMissions3Window
    return (
     ViewSettings(VIEW_ALIAS.CAMPAIGN_SELECTOR, CampaignSelectorWindow, '', WindowLayer.SUB_VIEW, VIEW_ALIAS.CAMPAIGN_SELECTOR, ScopeTemplates.LOBBY_SUB_SCOPE),
     ViewSettings(VIEW_ALIAS.PERSONAL_MISSIONS_3, PersonalMissions3Window, '', WindowLayer.SUB_VIEW, VIEW_ALIAS.PERSONAL_MISSIONS_3, ScopeTemplates.LOBBY_SUB_SCOPE))


def getBusinessHandlers():
    return (
     PMBusinessHandler(),)


class PMBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = (
         (
          VIEW_ALIAS.CAMPAIGN_SELECTOR, self.loadView),
         (
          VIEW_ALIAS.PERSONAL_MISSIONS_3, self.loadView))
        super(PMBusinessHandler, self).__init__(listeners, app_settings.APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)


def getContextMenuHandlers():
    return ()
