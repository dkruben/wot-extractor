# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/battle_matters_entry_point.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/battle_matters_entry_point.py
from __future__ import absolute_import
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.impl.lobby.battle_matters.battle_matters_entry_point_view import BattleMattersEntryPointView
from shared_utils import nextTick

class BattleMattersEntryPoint(InjectComponentAdaptor):

    @nextTick
    def _createInjectView(self, *args):
        super(BattleMattersEntryPoint, self)._createInjectView(*args)

    def _makeInjectView(self):
        return BattleMattersEntryPointView()
