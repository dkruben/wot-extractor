# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/live_ops_web_events/entry_point_tooltip_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/live_ops_web_events/entry_point_tooltip_view.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.live_ops_web_events.entry_point_tooltip_view_model import EntryPointTooltipViewModel
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.game_control import ILiveOpsWebEventsController
from gui.impl.gen.view_models.views.lobby.live_ops_web_events.entry_point_base import State

class EntryPointTooltipView(ViewImpl):
    __liveOpsWebEventsController = dependency.descriptor(ILiveOpsWebEventsController)
    __slots__ = ('__state', )

    def __init__(self, state):
        settings = ViewSettings(R.views.lobby.live_ops_web_events.EntryPointTooltip())
        settings.model = EntryPointTooltipViewModel()
        self.__state = state
        super(EntryPointTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(EntryPointTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        with self.viewModel.transaction() as tx:
            tx.setState(State(self.__state))
            tx.setEventStartDate(self.__liveOpsWebEventsController.eventStart)
            tx.setEventEndDate(self.__liveOpsWebEventsController.eventEnd)
        super(EntryPointTooltipView, self)._onLoading(*args, **kwargs)
