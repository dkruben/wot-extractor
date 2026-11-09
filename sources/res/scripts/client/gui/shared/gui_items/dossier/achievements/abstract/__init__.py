# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/gui_items/dossier/achievements/abstract/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/abstract/__init__.py
from __future__ import absolute_import
from future.utils import viewvalues
from helpers import dependency
from skeletons.gui.server_events import IEventsCache
from .mixins import Deprecated
from .mixins import Quest
from .mixins import HasVehiclesList as _HasVehiclesList
from .mixins import NoProgressBar
from .class_progress import ClassProgressAchievement
from .historical import HistoricalAchievement
from .nation_specific import NationSpecificAchievement
from .rare import RareAchievement
from .regular import RegularAchievement
from .series import SeriesAchievement
from .regular_ext import RegularExtAchievement
from .simple_progress import SimpleProgressAchievement
from .stage import StageAchievement

class DeprecatedAchievement(Deprecated, RegularAchievement):
    pass


class QuestAchievement(Quest, RegularAchievement):
    pass


class DeprecatedClassAchievement(Deprecated, NoProgressBar, ClassProgressAchievement):
    pass


def isRareAchievement(achievement):
    return isinstance(achievement, RareAchievement)


def isSeriesAchievement(achievement):
    return isinstance(achievement, SeriesAchievement)


def achievementHasVehiclesList(achievement):
    return isinstance(achievement, _HasVehiclesList)


def getCompletedPersonalMissionsCount(branch, classifiers):
    eventsCache = dependency.instance(IEventsCache)

    def _filter(quest):
        return quest.isFullCompleted() and quest.getQuestClassifier().classificationAttr in classifiers

    result = 0
    for operation in viewvalues(eventsCache.getPersonalMissions().getOperationsForBranch(branch)):
        result += len(operation.getQuestsByFilter(_filter))

    return result


__all__ = ('ClassProgressAchievement', 'HistoricalAchievement', 'NationSpecificAchievement',
           'RareAchievement', 'RegularAchievement', 'RegularExtAchievement', 'SeriesAchievement',
           'SimpleProgressAchievement', 'DeprecatedAchievement', 'QuestAchievement',
           'isRareAchievement', 'isSeriesAchievement', 'achievementHasVehiclesList',
           'StageAchievement')
