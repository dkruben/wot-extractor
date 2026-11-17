# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/mapbox/carousel_data_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui import GUI_NATIONS_ORDER_INDEX as GUI_NATIONS_ORDER_INDEX
from gui.Scaleform.daapi.view.lobby.hangar.carousels.battle_pass.carousel_data_provider import BattlePassCarouselDataProvider as BattlePassCarouselDataProvider
from gui.Scaleform.daapi.view.lobby.hangar.carousels.carousel_helpers import getUnsuitable2queueTooltip as getUnsuitable2queueTooltip
from gui.impl.gen import R as R
from gui.prb_control.entities.mapbox.pre_queue.actions_validator import MapboxVehicleValidator as MapboxVehicleValidator
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle, VEHICLE_TYPES_ORDER_INDICES as VEHICLE_TYPES_ORDER_INDICES

class MapboxCarouselDataProvider(BattlePassCarouselDataProvider):
    @classmethod
    def _vehicleComparisonKey(cls, vehicle):
        ...
    def _buildVehicle(self, vehicle):
        ...
