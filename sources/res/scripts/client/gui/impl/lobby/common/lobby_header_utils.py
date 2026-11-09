# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/common/lobby_header_utils.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/common/lobby_header_utils.py
from __future__ import absolute_import
HEADER_BUTTONS_COUNTERS_CHANGED_EVENT = 'lobbyHeaderButtonsCountersChanged'
_EXT_FIGHT_BUTTON_TOOLTIP_GETTERS = []

def registerFightButtonTooltipGetter(getter):
    _EXT_FIGHT_BUTTON_TOOLTIP_GETTERS.append(getter)


def findExtensionTooltip(pValidation):
    for getter in _EXT_FIGHT_BUTTON_TOOLTIP_GETTERS:
        tooltip = getter(pValidation)
        if tooltip is not None:
            return tooltip

    return
