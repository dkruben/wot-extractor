# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/auxiliary/tooltips/compensation_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/auxiliary/tooltips/compensation_tooltip.py
from __future__ import absolute_import
from gui.impl.gen.view_models.views.loot_box_compensation_tooltip_model import LootBoxCompensationTooltipModel
from gui.impl.gen.view_models.views.loot_box_compensation_tooltip_types import LootBoxCompensationTooltipTypes
from gui.impl.gen.view_models.views.loot_box_vehicle_compensation_tooltip_model import LootBoxVehicleCompensationTooltipModel
from gui.impl.pub import ViewImpl

class CompensationTooltipContent(ViewImpl):
    __slots__ = ()

    @property
    def viewModel(self):
        return super(CompensationTooltipContent, self).getViewModel()

    def _initialize(self, *args, **kwargs):
        with self.viewModel.transaction() as tx:
            tx.setIconBefore(kwargs.get('iconBefore', ''))
            tx.setLabelBefore(kwargs.get('labelBefore', ''))
            tx.setIconAfter(kwargs.get('iconAfter', ''))
            tx.setLabelAfter(kwargs.get('labelAfter', ''))
            tx.setBonusName(kwargs.get('bonusName', ''))
            tx.setCountBefore(kwargs.get('countBefore', 1))
            tx.setTooltipType(kwargs.get('tooltipType', LootBoxCompensationTooltipTypes.BASE))


class CrewSkinsCompensationTooltipContent(CompensationTooltipContent):
    __slots__ = ()

    def _initialize(self, *args, **kwargs):
        super(CrewSkinsCompensationTooltipContent, self)._initialize(*args, **kwargs)
        with self.viewModel.transaction() as tx:
            tx.setLabelBefore(kwargs.get('labelBefore', ''))


class VehicleCompensationTooltipContent(CompensationTooltipContent):
    __slots__ = ()

    @property
    def viewModel(self):
        return super(VehicleCompensationTooltipContent, self).getViewModel()

    def _initialize(self, *args, **kwargs):
        super(VehicleCompensationTooltipContent, self)._initialize(*args, **kwargs)
        with self.viewModel.transaction() as tx:
            tx.setVehicleName(kwargs.get('vehicleName', ''))
            tx.setVehicleType(kwargs.get('vehicleType', ''))
            tx.setIsElite(kwargs.get('isElite', True))
            tx.setVehicleLvl(kwargs.get('vehicleLvl', ''))
            tx.setTooltipType(LootBoxCompensationTooltipTypes.VEHICLE)
