# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/pub/main_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/pub/main_view.py
from __future__ import absolute_import
from frameworks.wulf import ViewFlags, ViewSettings, ViewModel
from gui.impl.pub import ViewImpl

class MainView(ViewImpl):
    __slots__ = ()

    def __init__(self, entryID):
        super(MainView, self).__init__(ViewSettings(entryID, ViewFlags.MAIN_VIEW, ViewModel()))
