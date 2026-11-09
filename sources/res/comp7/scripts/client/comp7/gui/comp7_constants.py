# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/comp7_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/comp7_constants.py
from __future__ import absolute_import
from comp7.gui.Scaleform.genConsts.COMP7_HANGAR_ALIASES import COMP7_HANGAR_ALIASES
from constants_utils import ConstInjector
from gui.prb_control import settings
from messenger import m_constants
COMP7_HANGAR_ALIAS = COMP7_HANGAR_ALIASES.COMP7_LOBBY_HANGAR
COMP7_ENTRY_POINT_ALIAS = 'Comp7EntryPoint'
INFO_PAGE_WCI = 'infoPageWci'
INFO_PAGE_OLS = 'infoPageOls'

class FUNCTIONAL_FLAG(settings.FUNCTIONAL_FLAG, ConstInjector):
    COMP7 = 536870912


class PREBATTLE_ACTION_NAME(settings.PREBATTLE_ACTION_NAME, ConstInjector):
    _const_type = str
    COMP7 = 'comp7'
    COMP7_SQUAD = 'comp7Squad'


class SELECTOR_BATTLE_TYPES(settings.SELECTOR_BATTLE_TYPES, ConstInjector):
    _const_type = str
    COMP7 = 'comp7'


class REQUEST_TYPE(settings.REQUEST_TYPE, ConstInjector):
    pass


class SCH_CLIENT_MSG_TYPE(m_constants.SCH_CLIENT_MSG_TYPE, ConstInjector):
    pass
