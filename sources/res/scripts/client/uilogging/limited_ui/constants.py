# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/uilogging/limited_ui/constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/limited_ui/constants.py
from __future__ import absolute_import
from enum import Enum
FEATURE = 'limited_ui'

class LimitedUILogItem(Enum):
    DISABLE_LIMITED_UI_BUTTON = 'disable_limited_ui_button'


class LimitedUILogScreenParent(Enum):
    SETTINGS_WINDOW = 'settings_window'


class LimitedUILogActions(Enum):
    CLICK = 'click'
