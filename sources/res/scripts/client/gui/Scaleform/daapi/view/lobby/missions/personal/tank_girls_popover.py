# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/missions/personal/tank_girls_popover.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/missions/personal/tank_girls_popover.py
from __future__ import absolute_import
from gui.server_events.events_dispatcher import showTankwomanAward
from gui.shared.formatters import text_styles
from gui.Scaleform.daapi.view.meta.TankgirlsPopoverMeta import TankgirlsPopoverMeta
from gui.Scaleform.locale.PERSONAL_MISSIONS import PERSONAL_MISSIONS
from gui.server_events import events_helpers
from helpers import dependency
from shared_utils import first
from skeletons.gui.server_events import IEventsCache

class TankgirlsPopover(TankgirlsPopoverMeta):
    __eventsCache = dependency.descriptor(IEventsCache)

    def onRecruitClick(self, idx):
        self.__getMissionAward(idx)
        self.destroy()

    def _populate(self):
        super(TankgirlsPopover, self)._populate()
        self.__eventsCache.onProgressUpdated += self.__onQuestsUpdated
        self.__update()

    def _dispose(self):
        self.__eventsCache.onProgressUpdated -= self.__onQuestsUpdated
        super(TankgirlsPopover, self)._dispose()

    def __update(self):
        tankwomenQuests = []
        for quest, opName in events_helpers.getTankmanRewardQuests():
            tankwomenQuests.append({'id': (str(quest.getID())), 
               'operationLabel': (text_styles.standard(opName)), 
               'missionLabel': (text_styles.main(quest.getShortUserName())), 
               'recruitBtnLabel': (PERSONAL_MISSIONS.PERSONALMISSIONS_TANKGIRLSPOPOVER_RECRUITBTN)})

        self.as_setListDataProviderS(tankwomenQuests)

    def __getMissionAward(self, eventID):
        quest = self.__eventsCache.getPersonalMissions().getAllQuests()[int(eventID)]
        bonus = quest.getTankmanBonus()
        if quest.needToGetReward() and bonus.tankman is not None:
            showTankwomanAward(quest.getID(), first(bonus.tankman.getTankmenData()))
        return

    def __onQuestsUpdated(self, *args):
        self.__update()
