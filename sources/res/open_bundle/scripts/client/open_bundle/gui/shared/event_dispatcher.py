# wot-extractor: codigo DESCOMPILADO de sources/res/open_bundle/scripts/client/open_bundle/gui/shared/event_dispatcher.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: open_bundle/scripts/client/open_bundle/gui/shared/event_dispatcher.py
from __future__ import absolute_import
from gui.impl.gen import R
from wg_async import wg_async, wg_await

def showOpenBundleMainView(bundleID):
    from open_bundle.gui.impl.lobby.states import OpenBundleState
    OpenBundleState.goTo(bundleID=bundleID)


def showIntro(bundleID):
    from open_bundle.gui.impl.lobby.intro_view import IntroWindow
    window = IntroWindow(bundleID)
    window.load()


@wg_async
def showOpenBundleConfirmDialog(bundleID, stepNumber, parent=None, callback=None):
    from gui.impl.dialogs import dialogs
    from open_bundle.gui.impl.lobby.confirmation_view import ConfirmationView
    result = yield wg_await(dialogs.showSingleDialogWithResultData(layoutID=R.views.open_bundle.mono.lobby.confirmation(), parent=parent, wrappedViewClass=ConfirmationView, bundleID=bundleID, stepNumber=stepNumber))
    if result.busy:
        callback((False, {}))
    else:
        isOK, data = result.result
        callback((isOK, data))
