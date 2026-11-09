# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/header_helpers/base_flags.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/header_helpers/base_flags.py
from __future__ import absolute_import
import typing
from typing import Dict, List, Optional, Union
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.Vehicle import Vehicle

class IQuestsFlag(object):

    @classmethod
    def isFlagSuitable(cls, questType):
        raise NotImplementedError

    @classmethod
    def formatQuests(cls, vehicle, params):
        raise NotImplementedError

    @classmethod
    def showQuestsInfo(cls, questType, questID):
        raise NotImplementedError
