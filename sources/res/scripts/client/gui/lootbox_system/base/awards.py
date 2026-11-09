# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/lootbox_system/base/awards.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/lootbox_system/base/awards.py
from __future__ import absolute_import
import logging
from future.utils import viewitems, viewvalues
from gui.shared.money import Currency, Money, ZERO_MONEY
from helpers import dependency
from messenger.formatters.service_channel_helpers import getCustomizationItem
from skeletons.gui.shared import IItemsCache
_logger = logging.getLogger(__name__)

def preformatRewardsInfo(rewards):
    vehiclesList = rewards.get('vehicles', [])
    customizationsList = rewards.get('customizations', [])
    compValue = _getCompensationValue(vehiclesList)
    _addLockedStyleForVehicle(customizationsList, vehiclesList)
    for currency in Currency.ALL:
        if compValue.get(currency, 0) > 0:
            currencyValue = rewards.pop(currency, None)
            if currencyValue is not None:
                newCurrencyValue = currencyValue - compValue.get(currency, 0)
                if newCurrencyValue:
                    rewards[currency] = newCurrencyValue

    return


@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def addCompensation(rewards, itemsCache=None):
    vehiclesList = rewards.get('vehicles', [])
    for vehicleDict in vehiclesList:
        for vehIntCD, vehData in viewitems(vehicleDict):
            if 'compensatedNumber' in vehData:
                _logger.error('Trying to add compensation with compensation already present: %s', vehiclesList)
                return
            if 'customCompensation' not in vehData:
                _logger.warning('Compensation amount not defined for vehicle: %s', vehData)
                continue
            vehicleItem = itemsCache.items.getItemByCD(vehIntCD)
            if vehicleItem is not None and vehicleItem.inventoryCount > 0:
                vehData['compensatedNumber'] = 1

    return


@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def _addLockedStyleForVehicle(customizations, vehicles, itemsCache=None):
    if customizations and vehicles:
        for customization in customizations:
            customizationType = customization['custType']
            if customizationType == 'style':
                customizationID = customization['id']
                style = getCustomizationItem(customizationID, customizationType)
                if style is not None and style.isLockedOnVehicle:
                    vehCD = customization.get('vehTypeCompDescr')
                    for vehicleDict in vehicles:
                        cd = next(iter(vehicleDict))
                        if vehCD == cd or vehCD is None and style.mayInstall(itemsCache.items.getItemByCD(cd)):
                            vehicleDict[cd].update({'customization': {'styleId': customizationID}})
                            break

    return


def _getCompensationValue(vehicles):
    compensation = ZERO_MONEY
    for vehicleDict in vehicles:
        for vehData in viewvalues(vehicleDict):
            if 'rentCompensation' in vehData:
                compensation += Money.makeFromMoneyTuple(vehData['rentCompensation'])
            if 'customCompensation' in vehData and 'compensatedNumber' in vehData:
                compensation += Money.makeFromMoneyTuple(vehData['customCompensation']) * vehData['compensatedNumber']

    return compensation
