# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/helpers/DevHotkeysController.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/DevHotkeysController.py
from __future__ import absolute_import
import os, subprocess, Keys

def handleKeyEvent(event):
    if event.isShiftDown() and event.isCtrlDown() and event.isAltDown() and event.isKeyDown() and not event.isRepeatedEvent():
        if event.key == Keys.KEY_P:
            subprocess.Popen([os.getcwd() + './../tools/PixelsHunter/PixelsHunter.exe', str(os.getpid())])
            __runSizeManager()
        elif event.key == Keys.KEY_S:
            __runSizeManager()


def __runSizeManager():
    from development.as_tools.change_window_size_manager import g_change_manager as m
    m.start()
