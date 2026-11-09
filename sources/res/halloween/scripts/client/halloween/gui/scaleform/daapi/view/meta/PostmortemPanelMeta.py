# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/meta/PostmortemPanelMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/scaleform/daapi/view/meta/PostmortemPanelMeta.py
from gui.Scaleform.daapi.view.battle.shared.postmortem_panel import PostmortemPanel

class PostmortemPanelMeta(PostmortemPanel):

    def as_setHintTitleS(self, value, isShadow=True):
        if self._isDAAPIInited():
            return self.flashObject.as_setHintTitle(value, isShadow)

    def as_setHintDescrS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setHintDescr(value)

    def as_showRespawnIconS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showRespawnIcon(value)

    def as_setCanExitS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCanExit(value)

    def as_showSpectatorPanelS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showSpectatorPanel(value)
