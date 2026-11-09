# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/battle_matters/battle_matters_exchange_rewards.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/battle_matters/battle_matters_exchange_rewards.py
from __future__ import absolute_import
from functools import partial
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.battle_matters.battle_matters_exchange_rewards_model import BattleMattersExchangeRewardsModel
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogBaseView
from gui.impl.pub.dialog_window import DialogButtons

class BattleMattersExchangeRewards(FullScreenDialogBaseView):
    __slots__ = ()

    def __init__(self, vehicleName, vehicleUserName):
        settings = ViewSettings(R.views.lobby.battle_matters.BattleMattersExchangeRewards())
        settings.model = BattleMattersExchangeRewardsModel()
        settings.args = (vehicleName, vehicleUserName)
        super(BattleMattersExchangeRewards, self).__init__(settings)

    @property
    def viewModel(self):
        return super(BattleMattersExchangeRewards, self).getViewModel()

    def _onLoading(self, vehicleName, vehicleUserName):
        super(BattleMattersExchangeRewards, self)._onLoading()
        with self.viewModel.transaction() as tx:
            tx.setVehicleName(vehicleName)
            tx.setVehicleUserName(vehicleUserName)

    def _getEvents(self):
        return (
         (
          self.viewModel.onConfirm, partial(self._setResult, DialogButtons.SUBMIT)),
         (
          self.viewModel.onClose, partial(self._setResult, DialogButtons.CANCEL)))
