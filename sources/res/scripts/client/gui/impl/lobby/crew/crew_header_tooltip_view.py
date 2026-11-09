# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/crew_header_tooltip_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/crew_header_tooltip_view.py
import typing
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.crew_header_tooltip_view_model import CrewHeaderTooltipViewModel
from gui.impl.gen.view_models.views.lobby.crew.idle_crew_bonus import IdleCrewBonusEnum
from gui.impl.pub import ViewImpl
from gui.game_control.wot_plus.utils import getPassiveCrewXPPerMinuteFromAllTiers
from helpers import dependency
from skeletons.gui.game_control import IWotPlusController
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from gui.shared.gui_items import Vehicle
_MINUTES_MULTIPLICATOR = 5

class CrewHeaderTooltipView(ViewImpl):
    __slots__ = ()
    _wotPlusCtrl = dependency.descriptor(IWotPlusController)
    _itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(layoutID=R.views.lobby.crew.CrewHeaderTooltipView(), model=CrewHeaderTooltipViewModel())
        settings.args = args
        settings.kwargs = kwargs
        super(CrewHeaderTooltipView, self).__init__(settings, *args, **kwargs)

    @property
    def viewModel(self):
        return super(CrewHeaderTooltipView, self).getViewModel()

    def _onLoading(self, idleCrewBonus):
        with self.viewModel.transaction() as tx:
            passiveCrewXP = int(getPassiveCrewXPPerMinuteFromAllTiers() * _MINUTES_MULTIPLICATOR)
            tx.setBonusXpPerFiveMinutes(passiveCrewXP)
            tx.setIdleCrewBonus(idleCrewBonus)
            vehicle = self._itemsCache.items.getVehicle(self._wotPlusCtrl.getVehicleIDWithIdleXP())
            if vehicle:
                tx.setVehicleName(vehicle.userName)
                tx.setVehicleType(vehicle.typeUserName)
                tx.setVehicleLvl(str(vehicle.level))
