# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/external_inventory_common/external_rent_entitlement.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/external_inventory_common/external_rent_entitlement.py
from __future__ import absolute_import
from items import vehicles
EXTERNAL_RENT_ENTITLEMENT_PREFIX = 'ext_rent'

def isExternalRentEntitlement(entitlementCode):
    return entitlementCode.startswith(EXTERNAL_RENT_ENTITLEMENT_PREFIX)


def parseEntitlement(entitlementCode):
    if not isExternalRentEntitlement(entitlementCode):
        return (False, None, 'Wrong prefix')
    else:
        tokens = entitlementCode.split(':')
        if len(tokens) < 3:
            return (False, None, 'Wrong amount of tokens')
        vehName = tokens[1] + ':' + tokens[2]
        if not vehicles.g_list.isVehicleExisting(vehName):
            return (False, None, 'Unknown vehicle')
        nationID, innationID = vehicles.g_list.getIDsByName(vehName)
        vehTypeCompDescr = vehicles.makeIntCompactDescrByID('vehicle', nationID, innationID)
        partnerCode = None
        if len(tokens) >= 4:
            partnerCode = tokens[3]
        data = {'vehTypeCompDescr': vehTypeCompDescr, 
           'partnerCode': partnerCode}
        return (
         True, data, '')
