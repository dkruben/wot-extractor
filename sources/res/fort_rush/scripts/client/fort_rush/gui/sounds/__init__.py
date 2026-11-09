# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/sounds/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/sounds/__init__.py
from __future__ import absolute_import
import SoundGroups

def play2DSound(eventName):
    SoundGroups.g_instance.playSafeSound2D(eventName)


def get2DSound(eventName):
    return SoundGroups.g_instance.getSound2D(eventName)
