# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/ranked/carousel_data_provider.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/ranked/carousel_data_provider.py
from __future__ import absolute_import
from gui import GUI_NATIONS_ORDER_INDEX
from gui.Scaleform.daapi.view.lobby.hangar.carousels.battle_pass.carousel_data_provider import BattlePassCarouselDataProvider
from gui.Scaleform.daapi.view.lobby.hangar.carousels.carousel_helpers import getUnsuitable2queueTooltip
from gui.impl.gen import R
from gui.shared.gui_items.Vehicle import Vehicle, VEHICLE_TYPES_ORDER_INDICES
from helpers import dependency
from skeletons.gui.game_control import IRankedBattlesController

class RankedCarouselDataProvider(BattlePassCarouselDataProvider):
    __rankedController = dependency.descriptor(IRankedBattlesController)

    @classmethod
    def _vehicleComparisonKey(cls, vehicle):
        return (
         not cls._isSuitableForQueue(vehicle),
         not vehicle.isInInventory,
         not vehicle.isEvent,
         not vehicle.isOnlyForBattleRoyaleBattles,
         not vehicle.isFavorite,
         not cls.__rankedController.hasVehicleRankedBonus(vehicle.intCD),
         GUI_NATIONS_ORDER_INDEX[vehicle.nationName],
         VEHICLE_TYPES_ORDER_INDICES[vehicle.type],
         vehicle.level,
         tuple(vehicle.buyPrices.itemPrice.price.iterallitems(byWeight=True)),
         vehicle.userName)

    def _buildVehicle(self, vehicle):
        result = super(RankedCarouselDataProvider, self)._buildVehicle(vehicle)
        result['hasRankedBonus'] = self.__rankedController.hasVehicleRankedBonus(vehicle.intCD)
        state, _ = vehicle.getState()
        suitResult = self.__rankedController.isSuitableVehicle(vehicle)
        resShortCut = R.strings.ranked_battles.rankedBattlesCarousel.lockedTooltip
        if suitResult is not None:
            if state == Vehicle.VEHICLE_STATE.UNSUITABLE_TO_QUEUE:
                result['lockedTooltip'] = getUnsuitable2queueTooltip(suitResult, resShortCut)
            result['clickEnabled'] = True
            result['hasRankedBonus'] = False
        return result

    @staticmethod
    def _isSuitableForQueue(vehicle):
        return True
