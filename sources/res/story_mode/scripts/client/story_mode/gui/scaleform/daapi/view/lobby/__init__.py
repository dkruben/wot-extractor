# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/lobby/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/lobby/__init__.py
from __future__ import absolute_import
from frameworks.wulf import WindowLayer
from gui.Scaleform.framework import ScopeTemplates, ViewSettings, getSwfExtensionUrl
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.app_loader import settings as app_settings
from gui.shared import EVENT_BUS_SCOPE
from story_mode.gui.impl.lobby.battle_result_view import BattleResultsWindow
from story_mode.gui.impl.lobby.web_view import StoryModeWebViewTransparent
from story_mode.gui.story_mode_gui_constants import VIEW_ALIAS

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from story_mode.gui.scaleform.daapi.view.lobby.outro_video import OutroVideo
    return (
     ViewSettings(VIEW_ALIAS.STORY_MODE_WEB_VIEW_TRANSPARENT, StoryModeWebViewTransparent, 'browserScreen.swf', WindowLayer.FULLSCREEN_WINDOW, VIEW_ALIAS.STORY_MODE_WEB_VIEW_TRANSPARENT, ScopeTemplates.LOBBY_SUB_SCOPE),
     ViewSettings(VIEW_ALIAS.STORY_MODE_OUTRO_VIDEO_WINDOW, OutroVideo, getSwfExtensionUrl('story_mode', 'IntroVideo.swf'), WindowLayer.TOP_WINDOW, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(VIEW_ALIAS.STORY_MODE_BATTLE_RESULTS, BattleResultsWindow, '', WindowLayer.TOP_WINDOW, None, ScopeTemplates.DEFAULT_SCOPE))


def getBusinessHandlers():
    return (
     StoryModePackageBusinessHandler(),)


class StoryModePackageBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = (
         (
          VIEW_ALIAS.STORY_MODE_WEB_VIEW_TRANSPARENT, self.loadViewByCtxEvent),
         (
          VIEW_ALIAS.STORY_MODE_OUTRO_VIDEO_WINDOW, self.loadViewByCtxEvent),
         (
          VIEW_ALIAS.STORY_MODE_BATTLE_RESULTS, self.loadView))
        super(StoryModePackageBusinessHandler, self).__init__(listeners, app_settings.APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)
