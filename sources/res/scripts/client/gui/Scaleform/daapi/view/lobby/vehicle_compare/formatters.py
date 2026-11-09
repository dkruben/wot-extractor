# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_compare/formatters.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_compare/formatters.py
from __future__ import absolute_import
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE
from gui.game_control.veh_comparison_basket import isValidVehicleForComparing
from helpers import dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.game_control import IVehicleComparisonBasket

def packHeaderColumnData(columnID, btnWidth, btnHeight, label='', icon='', tooltip='', direction='descending', showSeparator=True, textAlign='center', enabled=False, verticalTextAlign='bottom'):
    return {'id': columnID, 
       'label': (_ms(label)), 
       'iconSource': icon, 
       'buttonWidth': btnWidth, 
       'toolTip': tooltip, 
       'defaultSortDirection': direction, 
       'buttonHeight': btnHeight, 
       'showSeparator': showSeparator, 
       'enabled': enabled, 
       'textAlign': textAlign, 
       'verticalTextAlign': verticalTextAlign}


def getTreeNodeCompareData(vehicle):
    comparisonBasket = dependency.instance(IVehicleComparisonBasket)
    return {'modeAvailable': (comparisonBasket.isEnabled()), 
       'cmpBasketFull': (not comparisonBasket.isReadyToAdd(vehicle))}


def resolveStateTooltip(comparisonBasket, vehicle, enabledTooltip, fullTooltip, invalidTooltip=VEH_COMPARE.VEHPREVIEW_COMPAREVEHICLEBTN_TOOLTIPS_CANNOTADDTOCOMPARE):
    if not comparisonBasket.isAvailable():
        state, tooltip = False, invalidTooltip
    elif comparisonBasket.isFull():
        state, tooltip = False, fullTooltip
    elif not isValidVehicleForComparing(vehicle):
        state, tooltip = False, invalidTooltip
    else:
        state, tooltip = True, enabledTooltip
    return (state, tooltip)
