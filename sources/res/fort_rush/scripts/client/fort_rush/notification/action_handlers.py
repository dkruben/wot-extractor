# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/notification/action_handlers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/notification/action_handlers.py
from __future__ import absolute_import
import logging
from fort_rush.gui.shared.event_dispatcher import showProgressionView
from fort_rush.skeletons.battle_controller import IFortRushBattleController
from helpers import dependency
from notification.actions_handlers import NavigationDisabledActionHandler
from notification.settings import NOTIFICATION_TYPE

@dependency.replace_none_kwargs(ctrl=IFortRushBattleController)
def switchToFortRush(ctrl=None):
    ctrl.selectBattle()


class FortRushActionHandler(NavigationDisabledActionHandler):
    _frCtrl = dependency.descriptor(IFortRushBattleController)

    def doAction(self, model, entityID, action):
        logging.debug('[FORT_RUSH] FortRushActionHandler.doAction')
        switchToFortRush()

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return ('fortRushSwitchPrb', )

    def _canNavigate(self):
        result = super(FortRushActionHandler, self)._canNavigate()
        return self._frCtrl.isAvailable() and result


class _OpenFRProgressionHandler(FortRushActionHandler):

    @classmethod
    def getActions(cls):
        return ('openFRProgression', )

    def doAction(self, model, entityID, action):
        self._frCtrl.selectBattle(showProgressionView)
