# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/meta/BossHPBarMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/scaleform/daapi/view/meta/BossHPBarMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BossHPBarMeta(BaseDAAPIComponent):

    def as_setVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(value)

    def as_setLockedS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setLocked(value)

    def as_setMaxLivesS(self, value, difficulty, info):
        if self._isDAAPIInited():
            return self.flashObject.as_setMaxLives(value, difficulty, info)

    def as_setLivesS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setLives(value)

    def as_setBossHPS(self, label, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_setBossHP(label, progress)

    def as_setShieldsS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setShields(value)
