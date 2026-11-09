# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/badges/BadgesCollector.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/badges/BadgesCollector.py
import operator
from collections import defaultdict
import typing
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.badge import Badge

class BadgesCollector(object):

    def __init__(self):
        self.__receivedBadges = []
        self.__notReceivedBadges = []
        self.__suffixBadges = []
        self.__notReceivedSuffixBadges = []

    def getReceivedPrefixBadges(self):
        return tuple(self.__receivedBadges)

    def getNotReceivedPrefixBadges(self):
        return tuple(self.__notReceivedBadges)

    def getNotReceivedSuffixBadges(self):
        return tuple(self.__notReceivedSuffixBadges)

    def getSuffixAchievedBadges(self):
        return tuple(self.__suffixBadges)

    def updateCollector(self, badges=None):
        if badges is not None:
            self.__clear()
            self.__preprocessBadges(badges)
        return

    def __isReceivedPrefixBadges(self, badge):
        return badge.isPrefixLayout() and badge.isAchieved

    def __isNotReceivedPrefixBadges(self, badge):
        return badge.isPrefixLayout() and not badge.isAchieved and badge.isVisibleAsAchievable() and not badge.isObsolete()

    def __isNotReceivedSuffixBadge(self, badge):
        return badge.isSuffixLayout() and not badge.isAchieved

    def __isSuffixAchivedBadge(self, badge):
        return badge.isSuffixLayout() and badge.isAchieved

    def __clear(self):
        self.__receivedBadges = []
        self.__notReceivedBadges = []
        self.__notReceivedSuffixBadges = []
        self.__suffixBadges = []

    def __preprocessBadges(self, badges):
        cache = defaultdict(list)
        for badge in badges:
            if self.__isSuffixAchivedBadge(badge):
                self.__suffixBadges.append(badge)
            elif badge.isCollapsible():
                cache[badge.group].append(badge)
            elif self.__isNotReceivedPrefixBadges(badge) and badge.isVisibleAsAchievable():
                self.__notReceivedBadges.append(badge)
            elif self.__isNotReceivedSuffixBadge(badge) and badge.isVisibleAsAchievable():
                self.__notReceivedSuffixBadges.append(badge)
            elif self.__isReceivedPrefixBadges(badge):
                self.__receivedBadges.append(badge)

        for cachedBadges in cache.itervalues():
            byClass = sorted(cachedBadges, key=operator.methodcaller('getBadgeClass'), reverse=True)
            for cachedBadge in byClass:
                if self.__isNotReceivedPrefixBadges(cachedBadge) and cachedBadge.isVisibleAsAchievable():
                    self.__notReceivedBadges.append(cachedBadge)
                elif self.__isReceivedPrefixBadges(cachedBadge):
                    self.__receivedBadges.append(cachedBadge)
                    break

        self.__suffixBadges.sort()
        self.__notReceivedBadges.sort()
        self.__receivedBadges.sort()
