# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/blueprints/BlueprintTypes.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/blueprints/BlueprintTypes.py
from __future__ import absolute_import
from wotdecorators import singleton

@singleton
class BlueprintTypes(object):
    NONE = 0
    VEHICLE = 1
    NATIONAL = 2
    INTELLIGENCE_DATA = 3
    UNIVERSAL = (
     NATIONAL, INTELLIGENCE_DATA)
    ALL = (NATIONAL, VEHICLE, INTELLIGENCE_DATA)
