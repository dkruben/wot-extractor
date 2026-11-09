# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/presenters/battle_royale_event_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/presenters/battle_royale_event_presenter.py
from __future__ import absolute_import
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_royale_event_model import BattleRoyaleEventModel
from battle_royale.gui.impl.lobby.br_helpers.utils import setEventInfo
from gui.impl.pub.view_component import ViewComponent
from gui.prb_control.entities.listener import IGlobalListener
from helpers import dependency
from skeletons.gui.game_control import IBattleRoyaleController
from skeletons.gui.lobby_context import ILobbyContext

class BattleRoyaleEventPresenter(ViewComponent[BattleRoyaleEventModel], IGlobalListener):
    __battleRoyaleController = dependency.descriptor(IBattleRoyaleController)
    __lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self):
        super(BattleRoyaleEventPresenter, self).__init__(model=BattleRoyaleEventModel)

    @property
    def viewModel(self):
        return super(BattleRoyaleEventPresenter, self).getViewModel()

    def onPrbEntitySwitched(self):
        self.__update()

    def _onLoading(self, *args, **kwargs):
        super(BattleRoyaleEventPresenter, self)._onLoading(*args, **kwargs)
        self.startGlobalListening()
        self.__update()

    def _finalize(self):
        self.stopGlobalListening()
        return super(BattleRoyaleEventPresenter, self)._finalize()

    def __update(self, *_):
        with self.viewModel.transaction() as model:
            setEventInfo(model)
