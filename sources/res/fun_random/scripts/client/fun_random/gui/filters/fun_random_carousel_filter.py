# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/filters/fun_random_carousel_filter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/filters/fun_random_carousel_filter.py
from __future__ import absolute_import
from account_helpers.AccountSettings import BATTLEPASS_CAROUSEL_FILTER_1, BATTLEPASS_CAROUSEL_FILTER_CLIENT_1, FUN_RANDOM_CAROUSEL_FILTER_1, FUN_RANDOM_CAROUSEL_FILTER_2, FUN_RANDOM_CAROUSEL_FILTER_3, FUN_RANDOM_CAROUSEL_FILTER_CLIENT_1
from gui.filters.battle_pass_carousel_filter import BattlePassCarouselFilter

class FunRandomCarouselFilter(BattlePassCarouselFilter):

    def __init__(self):
        super(FunRandomCarouselFilter, self).__init__()
        self._serverSections = (
         FUN_RANDOM_CAROUSEL_FILTER_1, FUN_RANDOM_CAROUSEL_FILTER_2, BATTLEPASS_CAROUSEL_FILTER_1,
         FUN_RANDOM_CAROUSEL_FILTER_3)
        self._clientSections = (
         FUN_RANDOM_CAROUSEL_FILTER_CLIENT_1, BATTLEPASS_CAROUSEL_FILTER_CLIENT_1)
        self._criteriesGroups = ()
