# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/hangar_cameras/hangar_space_listener.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/hangar_cameras/hangar_space_listener.py
from helpers import dependency
from skeletons.gui.shared.utils import IHangarSpace

class HangarSpaceListener(object):
    hangarSpace = dependency.descriptor(IHangarSpace)

    def __init__(self):
        self.hangarSpace.onSpaceCreate += self._activate
        self.hangarSpace.onSpaceDestroy += self._deactivate

    def destroy(self):
        self.hangarSpace.onSpaceCreate -= self._activate
        self.hangarSpace.onSpaceDestroy -= self._deactivate

    def _activate(self):
        pass

    def _deactivate(self, inited):
        pass
