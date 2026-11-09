# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/live_ops_web_events/entry_point_tooltip_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/live_ops_web_events/entry_point_tooltip_view_model.py
from gui.impl.gen.view_models.views.lobby.live_ops_web_events.entry_point_base import EntryPointBase

class EntryPointTooltipViewModel(EntryPointBase):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(EntryPointTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getEventStartDate(self):
        return self._getNumber(2)

    def setEventStartDate(self, value):
        self._setNumber(2, value)

    def getEventEndDate(self):
        return self._getNumber(3)

    def setEventEndDate(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(EntryPointTooltipViewModel, self)._initialize()
        self._addNumberProperty('eventStartDate', 0)
        self._addNumberProperty('eventEndDate', 0)
