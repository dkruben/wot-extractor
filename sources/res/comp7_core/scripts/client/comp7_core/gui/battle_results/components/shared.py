# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_core/scripts/client/comp7_core/gui/battle_results/components/shared.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_core/scripts/client/comp7_core/gui/battle_results/components/shared.py
from __future__ import absolute_import
from account_helpers.AccountSettings import STATS_COMP7_SORTING
from gui.battle_results.components.shared import SortingBlock

class Comp7CoreSortingBlock(SortingBlock):
    __slots__ = ()

    def __init__(self, meta=None, field='', *path):
        super(Comp7CoreSortingBlock, self).__init__(STATS_COMP7_SORTING, meta, field, *path)
