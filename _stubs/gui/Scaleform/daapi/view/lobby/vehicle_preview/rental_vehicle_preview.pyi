# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/rental_vehicle_preview.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from gui.Scaleform.daapi.view.lobby.vehicle_preview.vehicle_preview import VehiclePreview as VehiclePreview
from gui.Scaleform.daapi.view.meta.VehiclePreviewBottomPanelWotPlusMeta import VehiclePreviewBottomPanelWotPlusMeta as VehiclePreviewBottomPanelWotPlusMeta
from gui.Scaleform.genConsts.VEHPREVIEW_CONSTANTS import VEHPREVIEW_CONSTANTS as VEHPREVIEW_CONSTANTS
from gui.impl import backport as backport
from gui.impl.gen import R as R
import wg_async as future_async
from gui.Scaleform.daapi.view.lobby.event_boards.formaters import formatDate as formatDate
from gui.shared.event_dispatcher import showTelecomRentDialog as showTelecomRentDialog
from gui.shared.gui_items.Vehicle import getIconResourceName as getIconResourceName, getNationLessName as getNationLessName
from gui.shop import showRentProductOverlay as showRentProductOverlay

class RentalVehiclePreview(VehiclePreview):
    def setBottomPanel(self):
        ...

class VehiclePreviewBottomPanelRental(VehiclePreviewBottomPanelWotPlusMeta):
    __buyParams: Any
    def _populate(self):
        ...
    def onRentClick(self):
        ...
    def setOffers(self, offers):
        ...
    # decorador original: @future_async.wg_async
    def __purchaseSubRent(self):
        ...
