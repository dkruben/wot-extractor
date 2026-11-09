# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/tooltips/customization_builders.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/customization_builders.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.lobby.customization.tooltips import ElementAwardTooltip
from gui.Scaleform.daapi.view.lobby.customization.tooltips import ElementIconTooltip
from gui.Scaleform.daapi.view.lobby.customization.tooltips import ElementPurchaseTooltip
from gui.Scaleform.daapi.view.lobby.customization.tooltips import ElementTooltip
from gui.Scaleform.daapi.view.lobby.customization.tooltips.element import NonHistoricTooltip, FantasticalTooltip, PopoverTooltip, ChainedTooltip
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts
from gui.shared.tooltips.builders import DataBuilder
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM, TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM_UI, ElementTooltip(contexts.TechCustomizationContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_NONHISTORIC_ITEM, TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM_UI, NonHistoricTooltip(contexts.TechCustomizationContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_FANTASTICAL_ITEM, TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM_UI, FantasticalTooltip(contexts.TechCustomizationContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_CHAINED_ITEM, TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM_UI, ChainedTooltip(contexts.TechCustomizationContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_POPOVER_ITEM, TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM_UI, PopoverTooltip(contexts.TechCustomizationContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM_ICON, TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM_UI, ElementIconTooltip(contexts.TechCustomizationContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM_AWARD, TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM_UI, ElementAwardTooltip(contexts.TechCustomizationContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM_PURCHASE, TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM_UI, ElementPurchaseTooltip(contexts.TechCustomizationContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.SHOP_CUSTOMIZATION_ITEM, TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM_UI, ElementTooltip(contexts.ShopCustomizationContext())))
