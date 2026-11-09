# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/game_control/award_controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/game_control/award_controller.py
from __future__ import absolute_import
from comp7_light.gui.comp7_light_constants import SCH_CLIENT_MSG_TYPE
from comp7_light.gui.shared.event_dispatcher import showBattleQuestAwardsWindow
from chat_shared import SYS_MESSAGE_TYPE
from gui.game_control.AwardController import PunishWindowHandler, ServiceChannelHandler
from helpers import dependency
from skeletons.gui.system_messages import ISystemMessages

class Comp7LightProgressionStageHandler(ServiceChannelHandler):
    __systemMessages = dependency.descriptor(ISystemMessages)
    _CLIENT_MSG_TYPE = SCH_CLIENT_MSG_TYPE.COMP7_LIGHT_PROGRESSION_NOTIFICATIONS

    def __init__(self, awardCtrl):
        super(Comp7LightProgressionStageHandler, self).__init__(SYS_MESSAGE_TYPE.comp7LightProgressionNotification.index(), awardCtrl)

    def _showAward(self, ctx):
        _, message = ctx
        stages = message.data.get('stages', set())
        for stage in stages:
            if stage.get('showAwardWindow', False):
                showBattleQuestAwardsWindow(stage)

        self._showMessages(ctx)

    def _showMessages(self, ctx):
        self.__systemMessages.proto.serviceChannel.pushClientMessage(self._getMessage(ctx), self._CLIENT_MSG_TYPE)

    @staticmethod
    def _getMessage(ctx):
        _, message = ctx
        return message


class Comp7LightPunishWindowHandler(PunishWindowHandler):

    @property
    def channelType(self):
        return SYS_MESSAGE_TYPE.comp7LightBattleResults.index()
