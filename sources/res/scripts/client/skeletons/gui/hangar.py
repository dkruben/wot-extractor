# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/skeletons/gui/hangar.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/hangar.py
from __future__ import absolute_import
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gui.prb_control.items import FunctionalState

class ICarouselEventEntry(object):

    @staticmethod
    def getIsActive(state):
        raise NotImplementedError
