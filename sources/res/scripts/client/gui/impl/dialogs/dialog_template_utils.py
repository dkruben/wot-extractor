# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/dialogs/dialog_template_utils.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/dialogs/dialog_template_utils.py
from __future__ import absolute_import
import typing
from past.builtins import long
import constants
from frameworks.wulf import PyResAccessor
from gui.Scaleform.genConsts.CURRENCIES_CONSTANTS import CURRENCIES_CONSTANTS
from gui.impl import backport
from helpers import dependency
from skeletons.gui.impl import IGuiLoader
if typing.TYPE_CHECKING:
    from gui.impl.pub import ViewImpl

def toString(value):
    if isinstance(value, PyResAccessor):
        return backport.text(value())
    if isinstance(value, (long, int)):
        return backport.text(value)
    return value


def findDialogTemplatesByUniqueID(uniqueID):
    from gui.impl.dialogs.dialog_template import DialogTemplateView
    guiLoader = dependency.instance(IGuiLoader)

    def predicate(view):
        return isinstance(view, DialogTemplateView) and view.dialogUniqueID == uniqueID

    return guiLoader.windowsManager.findViews(predicate)


def checkDialogTemplateIsOpened(uniqueID):
    return len(findDialogTemplatesByUniqueID(uniqueID)) != 0


def closeDialogTemplate(uniqueID):
    for dlg in findDialogTemplatesByUniqueID(uniqueID):
        dlg.destroyWindow()


def getCurrencyTooltipAlias(currency):
    if constants.IS_SINGAPORE and currency in CURRENCIES_CONSTANTS.SINGAPORE_ALTERNATIVE_CURRENCIES_SET:
        return currency + 'StatsFullScreen'
    return currency + 'InfoFullScreen'
