# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/ui/battle_royale.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/battle_royale.py
from __future__ import absolute_import
from constants import QUEUE_TYPE
from gui.prb_control.dispatcher import g_prbLoader
from gui.prb_control.entities.base.ctx import PrbAction
from gui.prb_control.settings import PREBATTLE_ACTION_NAME
from gui.shared.event_dispatcher import showHangar
from helpers import dependency
from skeletons.gui.game_control import IBattleRoyaleController
from web.web_client_api import w2c, W2CSchema

class OpenBattleRoyaleHangarMixin(object):
    battleRoyaleController = dependency.descriptor(IBattleRoyaleController)

    @w2c(W2CSchema, 'battle_royale_hangar')
    def selectBRMode(self, _):
        result = False
        dispatcher = g_prbLoader.getDispatcher()
        if dispatcher is not None and self.battleRoyaleController.isEnabled():
            isPrbActive = dispatcher.getFunctionalState().isInPreQueue(QUEUE_TYPE.BATTLE_ROYALE)
            if not isPrbActive:
                actionName = PREBATTLE_ACTION_NAME.BATTLE_ROYALE
                result = yield dispatcher.doSelectAction(PrbAction(actionName))
            else:
                result = isPrbActive
            if result:
                showHangar()
        yield {'success': result}
        return
