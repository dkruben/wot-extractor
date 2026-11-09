# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/pub/service_window.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/pub/service_window.py
from __future__ import absolute_import
from frameworks.wulf import WindowFlags
from gui.impl.pub.window_impl import WindowImpl
from gui.impl.pub.window_view import WindowView

class ServiceWindow(WindowImpl):
    __slots__ = ()

    def __init__(self, content=None, parent=None, areaID=0):
        super(ServiceWindow, self).__init__(wndFlags=WindowFlags.SERVICE_WINDOW, decorator=WindowView(), content=content, parent=parent, areaID=areaID)
