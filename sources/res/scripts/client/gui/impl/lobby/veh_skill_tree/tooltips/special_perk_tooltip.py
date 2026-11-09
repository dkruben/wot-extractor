# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/veh_skill_tree/tooltips/special_perk_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/veh_skill_tree/tooltips/special_perk_tooltip.py
from frameworks.wulf import ViewSettings
from helpers import dependency
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.veh_skill_tree.tooltips.special_perk_tooltip_model import SpecialPerkTooltipModel
from gui.impl.lobby.veh_skill_tree.tooltips.base_perk_tooltip import BasePerkTooltipView
from gui.veh_post_progression.models.progression import PostProgressionAvailability
from skeletons.gui.shared import IItemsCache
_LOCKED_VEHICLE_MAP = [
 PostProgressionAvailability.VEH_NOT_IN_INVENTORY,
 PostProgressionAvailability.VEH_IN_BATTLE,
 PostProgressionAvailability.VEH_IN_QUEUE,
 PostProgressionAvailability.VEH_IN_FORMATION,
 PostProgressionAvailability.VEH_IS_BROKEN]

class SpecialPerkTooltipView(BasePerkTooltipView):
    __itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.mono.vehicle_hub.tooltips.perk_tooltip())
        settings.model = SpecialPerkTooltipModel()
        settings.args = args
        settings.kwargs = kwargs
        super(SpecialPerkTooltipView, self).__init__(settings, *args, **kwargs)

    @property
    def viewModel(self):
        return self.getViewModel()

    def _onLoading(self, vehCD, step, stepStatus, *args, **kwargs):
        super(SpecialPerkTooltipView, self)._onLoading(vehCD, step, stepStatus, *args, **kwargs)
        vehicle = self.__itemsCache.items.getItemByCD(vehCD)
        _, reason = vehicle.postProgressionAvailability()
        lockedVehicle = reason in _LOCKED_VEHICLE_MAP
        self.viewModel.setLockedVehicle(lockedVehicle)
