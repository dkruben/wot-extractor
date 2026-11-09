# wot-extractor: codigo DESCOMPILADO de sources/res/open_bundle/scripts/client/open_bundle/gui/impl/lobby/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: open_bundle/scripts/client/open_bundle/gui/impl/lobby/__init__.py
from __future__ import absolute_import
from gui.shared.system_factory import registerBannerEntryPointValidator
from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer
from open_bundle.gui.constants import OPEN_BUNDLE_ENTRY_POINT_NAME
from open_bundle.gui.impl.lobby.event_banner import isOpenBundleEntryPointAvailable, OpenBundleEventBanner

def getStateMachineRegistrators():
    from open_bundle.gui.impl.lobby.states import registerStates, registerTransitions
    return (
     registerStates, registerTransitions)


def getViewSettings():
    return ()


def getBusinessHandlers():
    return ()


def getContextMenuHandlers():
    return ()


def registerEventBanners():
    ebc = EventBannersContainer()
    ebc.registerEventBanner(OpenBundleEventBanner)
    registerBannerEntryPointValidator(OPEN_BUNDLE_ENTRY_POINT_NAME, isOpenBundleEntryPointAvailable)
