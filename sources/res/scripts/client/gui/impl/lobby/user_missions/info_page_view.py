# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/user_missions/info_page_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/user_missions/info_page_view.py
from __future__ import absolute_import
from config_schemas.umg_config import umgConfigSchema
from frameworks.wulf import ViewSettings
from gui.impl.gen.view_models.views.lobby.user_missions.info_page_model import InfoPageModel
from gui.impl.pub.view_component import ViewComponent
from gui.server_events.events_helpers import getRerollTimeout
from gui.shared.system_factory import collectDynamicUmgInfoPagePresenters

class InfoPageView(ViewComponent[InfoPageModel]):

    def __init__(self, settings, *args, **kwargs):
        super(InfoPageView, self).__init__(settings.layoutID, InfoPageModel, *args, **kwargs)

    @property
    def viewModel(self):
        return super(InfoPageView, self).getViewModel()

    def _getEvents(self):
        return (
         (
          self.viewModel.onClose, self._onViewClose),)

    def _getChildComponents(self):
        return collectDynamicUmgInfoPagePresenters()

    def _onLoading(self, *args, **kwargs):
        super(InfoPageView, self)._onLoading(*args, **kwargs)
        self.viewModel.setRerollInterval(getRerollTimeout())
        self.viewModel.setIsWeeklySectionAvailable(umgConfigSchema.getModel().enableAllWeekly)

    def _onViewClose(self):
        self.destroyWindow()
