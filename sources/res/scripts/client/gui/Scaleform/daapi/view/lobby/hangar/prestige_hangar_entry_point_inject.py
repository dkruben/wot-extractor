# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/prestige_hangar_entry_point_inject.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/prestige_hangar_entry_point_inject.py
from __future__ import absolute_import
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.impl.lobby.prestige.prestige_hangar_entry_point_view import PrestigeHangarEntryPointView
from gui.Scaleform.daapi.view.meta.PrestigeProgressInjectMeta import PrestigeProgressInjectMeta
from gui.prb_control.entities.listener import IGlobalListener
from shared_utils import nextTick

class PrestigeHangarEntryPointInject(InjectComponentAdaptor, PrestigeProgressInjectMeta, IGlobalListener):

    @nextTick
    def _createInjectView(self, *args):
        super(PrestigeHangarEntryPointInject, self)._createInjectView(*args)

    def _makeInjectView(self):
        return PrestigeHangarEntryPointView()
