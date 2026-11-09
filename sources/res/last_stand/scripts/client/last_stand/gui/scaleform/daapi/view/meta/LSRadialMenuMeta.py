# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/meta/LSRadialMenuMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/meta/LSRadialMenuMeta.py
from gui.Scaleform.daapi.view.battle.shared.radial_menu import RadialMenu

class LSRadialMenuMeta(RadialMenu):

    def as_setObeliskEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setObeliskEnabled(value)
