# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/FLReplayController.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/FLReplayController.py
from __future__ import absolute_import
import BattleReplay

class FLReplayController(object):

    def __init__(self):
        pass

    @staticmethod
    def setDataCallback(eventName, callback):
        if BattleReplay.g_replayCtrl.isPlaying:
            BattleReplay.g_replayCtrl.setDataCallback(eventName, callback)

    @staticmethod
    def delDataCallback(eventName, callback):
        if BattleReplay.g_replayCtrl.isPlaying:
            BattleReplay.g_replayCtrl.delDataCallback(eventName, callback)

    @staticmethod
    def serializeCallbackData(eventName, data):
        BattleReplay.g_replayCtrl.serializeCallbackData(eventName, data)
