# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/shared/packers/bonus.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/shared/packers/bonus.py
from __future__ import absolute_import
import typing
from gui.server_events.awards_formatters import getDefaultFormattersMap, ItemsBonusFormatter
from gui.shared.missions.packers.bonus import ItemBonusUIPacker, BonusUIPacker, getDefaultBonusPackersMap
if typing.TYPE_CHECKING:
    from typing import Dict

def getSMFormattersMap():
    formattersMap = getDefaultFormattersMap()
    formattersMap['items'] = SMItemsBonusFormatter()
    return formattersMap


def getSMBonusPackersMap():
    bonusMap = getDefaultBonusPackersMap()
    bonusMap['items'] = SMItemBonusUIPacker()
    return bonusMap


def getSMBonusPacker():
    return BonusUIPacker(getSMBonusPackersMap())


class SMItemBonusUIPacker(ItemBonusUIPacker):

    @staticmethod
    def _itemsSortFunction(item):
        return -item[0].intCD


class SMItemsBonusFormatter(ItemsBonusFormatter):

    def _getItems(self, bonus):
        return sorted(bonus.getItems().items(), key=(lambda i: -i[0].intCD))
