# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/customization/constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/customization/constants.py
from __future__ import absolute_import
from gui.impl.gen import R

class CustomizationModes(object):
    CUSTOM = 1
    STYLE_2D = 2
    STYLE_3D = 3
    STYLE_2D_EDITABLE = 4
    ALL = (
     CUSTOM, STYLE_2D, STYLE_3D, STYLE_2D_EDITABLE)
    BASE = (CUSTOM, STYLE_2D, STYLE_3D)
    BASE_STYLES = (STYLE_2D, STYLE_3D)
    STYLES = BASE_STYLES + (STYLE_2D_EDITABLE,)


class CustomizationModeSource(object):
    UNDEFINED = -1
    BOTTOM_PANEL = 1
    CAROUSEL = 2
    CONTEXT_MENU = 3
    PROPERTIES_SHEET = 4
    NOTIFICATION = 5
    REWARD_WINDOW = 6


C11N_VIEW_IDS_THAT_SUSPEND_HIGHLIGHTER = frozenset((
 R.views.lobby.personal_exchange_rates.GoldExchangeView(),
 R.views.lobby.personal_exchange_rates.ExperienceExchangeView()))
