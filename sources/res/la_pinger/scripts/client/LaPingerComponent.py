# wot-extractor: codigo DESCOMPILADO de sources/res/la_pinger/scripts/client/LaPingerComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: la_pinger/scripts/client/LaPingerComponent.py
from __future__ import absolute_import
import BigWorld

class LaPingerComponent(BigWorld.StaticScriptComponent):

    def __init__(self):
        pass

    def pingMeAndThenJustTouchMe(self, ip, port, dbID, iterations, timeout):
        BigWorld.pingMeAndThenJustTouchMe(ip, port, dbID, iterations, timeout)
