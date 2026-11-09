# wot-extractor: codigo DESCOMPILADO de sources/res/advent_calendar/scripts/client/advent_calendar/gui/impl/lobby/feature/tooltips/advent_calendar_simple_tooltip_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: advent_calendar/scripts/client/advent_calendar/gui/impl/lobby/feature/tooltips/advent_calendar_simple_tooltip_view.py
from __future__ import absolute_import
import json
from advent_calendar.gui.impl.gen.view_models.views.lobby.tooltips.simple_tooltip_model import SimpleTooltipModel
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl

class AdventCalendarSimpleTooltip(ViewImpl[SimpleTooltipModel]):

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.advent_calendar.mono.lobby.tooltips.advent_calendar_simple_tooltip(), model=SimpleTooltipModel(), args=args, kwargs=kwargs)
        super(AdventCalendarSimpleTooltip, self).__init__(settings)

    def _onLoading(self, payload):
        with self.getViewModel().transaction() as vm:
            vm.setPayload(payload)


def createAdventCalendarSimpleTooltip(header, body):
    return AdventCalendarSimpleTooltip(json.dumps({'header': header, 'body': body}))
