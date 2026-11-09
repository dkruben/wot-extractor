# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/gui_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/gui_constants.py
from __future__ import absolute_import
from constants_utils import ConstInjector
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.hangar.header_helpers import flag_constants

class QuestFlagTypes(flag_constants.QuestFlagTypes, ConstInjector):
    _const_type = str
    EPIC = 'epicQuests'


class ViewAlias(VIEW_ALIAS, ConstInjector):
    _const_type = str
