# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/missions/missions_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/impl/lobby/missions/missions_helpers.py
from __future__ import absolute_import
from gui.impl.lobby.missions.missions_helpers import DefaultMissionsGuiHelper

class Comp7LightMissionsGuiHelper(DefaultMissionsGuiHelper):

    @classmethod
    def isDailyMissionsSupported(cls):
        return True

    @classmethod
    def isPM3MissionsSupported(cls):
        return False
