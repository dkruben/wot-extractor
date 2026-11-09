# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/user_missions/user_missions_hub_content_inject.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/user_missions/user_missions_hub_content_inject.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.meta.UserMissionsHubContentInjectMeta import UserMissionsHubContentInjectMeta
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor

class UserMissionsHubContentInject(InjectComponentAdaptor, UserMissionsHubContentInjectMeta):

    def __init__(self, tabID, questId, challengeId):
        super(UserMissionsHubContentInject, self).__init__()
        self.tabID = tabID
        self.questId = questId
        self.challengeId = challengeId

    def _makeInjectView(self):
        from gui.impl.lobby.user_missions.hub.hub_view import HubView
        return HubView(self.tabID, self.questId, self.challengeId)
