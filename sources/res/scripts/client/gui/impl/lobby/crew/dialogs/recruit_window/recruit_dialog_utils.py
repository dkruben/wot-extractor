# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/dialogs/recruit_window/recruit_dialog_utils.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/dialogs/recruit_window/recruit_dialog_utils.py
from gui.impl.gen.resources import R
from gui.impl import backport
from gui.server_events import recruit_helper
from gui.shared.utils.functions import replaceHyphenToUnderscore
RECRUIT_BG_DYN = R.images.gui.maps.icons.tankmen.windows.recruits.recruit_dialog

def getTitle(name=None):
    if name:
        title = backport.text(R.strings.dialogs.recruitDialog.name.title(), name=name)
    else:
        title = backport.text(R.strings.dialogs.recruitDialog.title())
    return title


def getTitleFromTokenData(tokenData):
    name = tokenData.getFullUserNameByNation().strip()
    if tokenData.getSmallIcon() in (recruit_helper._TANKWOMAN_ICON, recruit_helper._TANKMAN_ICON):
        name = None
    return getTitle(name)


def getIconName(iconID):
    return iconID.split('.')[0]


def getIcon(iconName='', isFemale=False):
    specialID = R.images.gui.maps.icons.tankmen.icons.special.dyn(attr=('{}').format(replaceHyphenToUnderscore(iconName)))
    if specialID is not None and specialID.exists():
        return (specialID(), True)
    else:
        bigID = R.images.gui.maps.icons.tankmen.icons.big.dyn(attr=('{}').format(replaceHyphenToUnderscore(iconName)))
        if bigID is not None and bigID.exists():
            return (bigID(), False)
        icon = (isFemale or recruit_helper)._TANKMAN_ICON if 1 else recruit_helper._TANKWOMAN_ICON
        return (R.images.gui.maps.icons.tankmen.icons.special.dyn(replaceHyphenToUnderscore(getIconName(icon)))(), True)


def getIconBackground(resurceID=None, dynIconName=None, dynPath=RECRUIT_BG_DYN):
    for event in recruit_helper.RecruitSourceID.EVENTS:
        if resurceID and event in resurceID or dynIconName and event in dynIconName:
            return dynPath.bg_recruitment_twitch()

    if resurceID and resurceID[:2] == 'ny':
        return dynPath.bg_recruitment_ny()
    return dynPath.bg_recruitment_regular()


def getSortedItems(unsortedItems, itemsOrderedList):
    sortedItems = []
    for name in itemsOrderedList:
        if name in unsortedItems:
            sortedItems.append(name)

    return sortedItems
