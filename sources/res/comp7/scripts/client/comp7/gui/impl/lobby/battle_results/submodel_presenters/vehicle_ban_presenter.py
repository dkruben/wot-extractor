# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/battle_results/submodel_presenters/vehicle_ban_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/lobby/battle_results/submodel_presenters/vehicle_ban_presenter.py
from __future__ import absolute_import
import typing
from comp7.gui.impl.gen.view_models.views.lobby.battle_results.comp7_bans_model import Comp7BansModel
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel
from helpers import dependency
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from gui.battle_results.stats_ctrl import BattleResults
    from frameworks.wulf import ViewModel

class Comp7VehicleBanSubPresenter(BattleResultsSubPresenter):
    __itemsCache = dependency.descriptor(IItemsCache)

    @classmethod
    def getViewModelType(cls):
        return Comp7BansModel

    def packBattleResults(self, battleResults):
        with self.getViewModel().transaction() as vm:
            bannedVehicles = battleResults.reusable.common.bannedVehicles
            vm.setIsEnabled(bool(bannedVehicles))
            playerTeam = battleResults.reusable.personal.avatar.team
            for teamID, banVehicleInfo in bannedVehicles.items():
                bannedVehicleCD = banVehicleInfo['vehicleCD']
                bannedVehicle = self.__itemsCache.items.getItemByCD(bannedVehicleCD) if bannedVehicleCD else None
                isRandomlySelected = banVehicleInfo['isRandomlySelected']
                totalVotes = banVehicleInfo['totalVotes']
                if teamID == playerTeam:
                    if bannedVehicle is not None:
                        fillVehicleModel(vm.bannedByAlliesVehicle, bannedVehicle)
                    vm.setIsAlliesRandomlySelected(isRandomlySelected)
                    vm.setAlliesVotes(totalVotes)
                elif bannedVehicle is not None:
                    fillVehicleModel(vm.bannedByEnemiesVehicle, bannedVehicle)
                vm.setIsEnemyRandomlySelected(isRandomlySelected)
                vm.setEnemyVotes(totalVotes)

        return
