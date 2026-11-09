# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/platoon/view/fun_platoon_members_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/lobby/platoon/view/fun_platoon_members_view.py
from __future__ import absolute_import
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin, FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.platoon.members_window_model import PrebattleTypes
from gui.impl.lobby.platoon.platoon_helpers import getPlatoonBonusState
from gui.impl.lobby.platoon.view.platoon_members_view import SquadMembersView
from gui.impl.lobby.platoon.view.subview.platoon_chat_subview import ChatSubview

class FunRandomMembersView(SquadMembersView, FunAssetPacksMixin, FunSubModesWatcher):
    _prebattleType = PrebattleTypes.FUNRANDOM

    @hasDesiredSubMode(defReturn='')
    def _getTitle(self):
        subModeName = backport.text(self.getDesiredSubMode().getLocalsResRoot().userName())
        return backport.text(R.strings.fun_random.platoonView.title(), subModeName=subModeName)

    def _setHeaderBg(self, fileName, model):
        model.header.setBackgroundImage(backport.image(self.getModeIconsResRoot().platoon.dyn(fileName)()))

    def _onFindPlayers(self):
        pass

    def _addSubviews(self):
        self._addSubviewToLayout(ChatSubview())

    def _addListeners(self):
        super(FunRandomMembersView, self)._addListeners()
        self.startSubSelectionListening(self.__onSubModeSelected)

    def _removeListeners(self):
        self.stopSubSelectionListening(self.__onSubModeSelected)
        super(FunRandomMembersView, self)._removeListeners()

    def _updateFindPlayersButton(self, *args):
        with self.viewModel.transaction() as model:
            model.setShouldShowFindPlayersButton(value=False)

    def __onSubModeSelected(self, *_):
        self.viewModel.setRawTitle(self._getTitle())
        self._setBonusInformation(getPlatoonBonusState(True))
