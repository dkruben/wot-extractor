# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/battle_results/reusable/common.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/battle_results/reusable/common.py
from __future__ import absolute_import
from gui.battle_results.reusable.common import CommonInfo

class Comp7CommonInfo(CommonInfo):
    __slots__ = ('__bannedVehicles', )

    def __init__(self, *args, **kwargs):
        super(Comp7CommonInfo, self).__init__(*args, **kwargs)
        self.__bannedVehicles = kwargs.get('comp7BannedVehicles', {})

    @property
    def bannedVehicles(self):
        return self.__bannedVehicles
