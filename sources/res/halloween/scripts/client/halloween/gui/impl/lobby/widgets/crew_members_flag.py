# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/widgets/crew_members_flag.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/impl/lobby/widgets/crew_members_flag.py
from __future__ import absolute_import
from gui.impl.pub.view_component import ViewComponent
from halloween.gui.impl.gen.view_models.views.lobby.widgets.crew_members_flag_model import CrewMembersFlagModel
from halloween.gui.shared.event_dispatcher import showCrewSelectionWindow
from halloween.skeletons.halloween_twitch_con_controller import IHalloweenTwitchConController
from helpers import dependency

class CrewMembersFlag(ViewComponent[CrewMembersFlagModel]):
    _hwTwitchConCtrl = dependency.descriptor(IHalloweenTwitchConController)

    def __init__(self):
        super(CrewMembersFlag, self).__init__(model=CrewMembersFlagModel)

    @property
    def viewModel(self):
        return super(CrewMembersFlag, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(CrewMembersFlag, self)._onLoading()
        self.__update()

    def _getEvents(self):
        return [
         (
          self.viewModel.onClick, self.__onClick),
         (
          self._hwTwitchConCtrl.onTwitchConSettingsUpdated, self.__update)]

    def __onClick(self):
        showCrewSelectionWindow()

    def __update(self):
        with self.viewModel.transaction() as model:
            model.setIsHidden(not self._hwTwitchConCtrl.isPromoScreenEnabled())
