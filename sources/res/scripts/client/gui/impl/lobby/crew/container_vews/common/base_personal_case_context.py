# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/common/base_personal_case_context.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/container_vews/common/base_personal_case_context.py
import typing
from gui.impl.lobby.container_views.base.context import TankmanContext
from gui.shared.gui_items.gui_item_economics import ItemPrice
from gui.shared.money import Currency, Money
from helpers import dependency
from items.tankmen import getSpecialVoiceTag
from skeletons.gui.game_control import ISpecialSoundCtrl
if typing.TYPE_CHECKING:
    from typing import Optional, Dict, Any

class BasePersonalCaseContext(TankmanContext):
    __slots__ = ('_retrainPrice', '_voiceoverParams')
    _specialSounds = dependency.descriptor(ISpecialSoundCtrl)

    def __init__(self, tankmanID, *args, **kwargs):
        self._tankmanCurrentVehicle = None
        self._tankmanNativeVehicle = None
        self._retrainPrice = None
        self._voiceoverParams = None
        super(BasePersonalCaseContext, self).__init__(tankmanID)
        return

    @property
    def tankmanCurrentVehicle(self):
        return self._tankmanCurrentVehicle

    @property
    def tankmanNativeVehicle(self):
        return self._tankmanNativeVehicle

    @property
    def retrainPrice(self):
        return self._retrainPrice

    @property
    def voiceoverParams(self):
        return self._voiceoverParams

    def update(self, tankmanID):
        super(BasePersonalCaseContext, self).update(tankmanID)
        self._tankmanCurrentVehicle = self.itemsCache.items.getVehicle(self._tankman.vehicleInvID)
        self._tankmanNativeVehicle = self.itemsCache.items.getItemByCD(self._tankman.vehicleNativeDescr.type.compactDescr)
        self._retrainPrice = self._getRetrainPrice()
        self._voiceoverParams = self._getUniqueVoiceoverParams()

    def _getRetrainPrice(self):
        shop = self.itemsCache.items.shop
        tankmanCost = shop.tankmanCost
        defTankmanCost = shop.defaults.tankmanCost
        credit = tankmanCost[1][Currency.CREDITS]
        defCredit = defTankmanCost[1][Currency.CREDITS]
        gold = tankmanCost[2][Currency.GOLD]
        defGold = defTankmanCost[2][Currency.GOLD]
        creditAction = credit != defCredit
        goldAction = gold != defGold
        return ItemPrice(price=Money(credits=credit if creditAction else None, gold=gold if goldAction else None), defPrice=Money(credits=defCredit if creditAction else None, gold=defGold if goldAction else None))

    def _getUniqueVoiceoverParams(self):
        specialVoiceTag = getSpecialVoiceTag(self.tankman, self._specialSounds)
        return self._specialSounds.getVoiceoverByTankmanTagOrVehicle(specialVoiceTag)
