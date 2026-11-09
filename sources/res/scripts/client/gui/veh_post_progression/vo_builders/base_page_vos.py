# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/veh_post_progression/vo_builders/base_page_vos.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/veh_post_progression/vo_builders/base_page_vos.py
import typing
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles, getRoleTextWithIcon
from gui.shared.gui_items.Vehicle import getNationLessName, getIconResourceName
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.Vehicle import Vehicle

def getBaseButtonsVO(vehicle):
    iconName = getIconResourceName(getNationLessName(vehicle.name))
    return {'shopIconPath': (backport.image(R.images.gui.maps.shop.vehicles.c_360x270.dyn(iconName)())), 
       'compareBtnVisible': True, 
       'goToVehicleViewBtnVisible': True, 
       'isPremium': (vehicle.isPremium or vehicle.buyPrices.itemPrice.isActionPrice()), 
       'vehicleId': (vehicle.intCD)}


def getBaseDataVO(vehicle):
    return {'showDemountAllPairsBtn': False, 
       'showExpBlock': False, 
       'vehicleButton': {}, 'vehicleInfo': {}, 'nation': (vehicle.nationName)}


def getBaseTitleVO(vehicle):
    tankUserName = vehicle.userName
    return {'intCD': (vehicle.intCD), 
       'tankNameStr': (text_styles.grandTitle(tankUserName)), 
       'tankNameStrSmall': (text_styles.promoTitle(tankUserName)), 
       'statusStr': '', 
       'roleText': (getRoleTextWithIcon(vehicle.role, vehicle.roleLabel)), 
       'showInfoIcon': False}
