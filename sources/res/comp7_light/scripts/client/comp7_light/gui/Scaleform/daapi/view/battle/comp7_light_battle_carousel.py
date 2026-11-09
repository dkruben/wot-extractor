# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/Scaleform/daapi/view/battle/comp7_light_battle_carousel.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/Scaleform/daapi/view/battle/comp7_light_battle_carousel.py
from __future__ import absolute_import
from account_helpers.AccountSettings import COMP7_LIGHT_CAROUSEL_FILTER_1, COMP7_LIGHT_CAROUSEL_FILTER_2
from account_helpers.AccountSettings import COMP7_LIGHT_CAROUSEL_FILTER_CLIENT_1
from comp7_core.gui.Scaleform.daapi.view.battle.battle_carousel import PrebattleTankCarousel

class Comp7LightPrebattleTankCarousel(PrebattleTankCarousel):
    _FILTER_SERVER_SECTIONS = (
     COMP7_LIGHT_CAROUSEL_FILTER_1, COMP7_LIGHT_CAROUSEL_FILTER_2)
    _FILTER_CLIENT_SECTIONS = (COMP7_LIGHT_CAROUSEL_FILTER_CLIENT_1,)
