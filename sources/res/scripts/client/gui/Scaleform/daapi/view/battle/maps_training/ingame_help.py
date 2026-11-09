# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/maps_training/ingame_help.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/maps_training/ingame_help.py
from __future__ import absolute_import
from gui import GUI_CTRL_MODE_FLAG
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.meta.MapsTrainingIngameHelpWindowMeta import MapsTrainingIngameHelpWindowMeta
from gui.Scaleform.managers.battle_input import BattleGUIKeyHandler
from gui.battle_control import avatar_getter
from gui.impl import backport
from gui.impl.gen import R
_HTML_TEMPLATE_PATH = 'html_templates:mapsTraining/loadingScreen'

class MapsTrainingIngameHelpWindow(MapsTrainingIngameHelpWindowMeta, BattleGUIKeyHandler):

    def onWindowClose(self):
        self.destroy()

    def onWindowMinimize(self):
        self.destroy()

    def handleEscKey(self, isDown):
        return isDown

    def _populate(self):
        super(MapsTrainingIngameHelpWindow, self)._populate()
        self.app.registerGuiKeyHandler(self)
        self.app.enterGuiControlMode(VIEW_ALIAS.INGAME_HELP, cursorVisible=True, enableAiming=False)
        avatar_getter.setForcedGuiControlMode(GUI_CTRL_MODE_FLAG.GUI_ENABLED, enableAiming=False)
        self.as_setDataS([self.__getPageConfig(pageNum + 1) for pageNum in range(4)])

    @staticmethod
    def __getPageConfig(pageNum):
        pageData = {'rendererLinkage': (('MapsTrainingHint{}PageBigUI').format(pageNum)), 
           'header1Text': (backport.text(R.strings.maps_training.loadingScreen.num(pageNum).title())), 
           'header1AutoSize': 'center', 
           'description1Text': (backport.text(R.strings.maps_training.loadingScreen.num(pageNum).description())), 
           'description1AutoSize': 'center', 
           'background': (backport.image(R.images.gui.maps.icons.mapsTraining.dyn(('tip_bg_0{}').format(pageNum))()))}
        return pageData

    def _dispose(self):
        self.app.leaveGuiControlMode(VIEW_ALIAS.INGAME_HELP)
        self.app.unregisterGuiKeyHandler(self)
        super(MapsTrainingIngameHelpWindow, self)._dispose()
