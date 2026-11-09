# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/impl/lobby/newbie_banner_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/impl/lobby/newbie_banner_tooltip.py
from __future__ import absolute_import
from frameworks.wulf import ViewModel
from frameworks.wulf.view.view import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from story_mode.uilogging.story_mode.loggers import NewbieEntryPointTooltipLogger

class NewbieBannerTooltip(ViewImpl):

    def __init__(self):
        super(NewbieBannerTooltip, self).__init__(ViewSettings(R.views.story_mode.mono.lobby.tooltips.newbie_banner_tooltip(), model=ViewModel()))
        self._uiLogger = NewbieEntryPointTooltipLogger()
        self._uiLogger.start()

    def _finalize(self):
        self._uiLogger.stop()
        super(NewbieBannerTooltip, self)._finalize()
