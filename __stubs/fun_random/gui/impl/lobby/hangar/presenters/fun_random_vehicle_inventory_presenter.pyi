# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/presenters/fun_random_vehicle_inventory_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin, FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode as hasDesiredSubMode
from gui.impl.gen import R as R
from gui.impl.lobby.hangar.presenters.vehicle_inventory_presenter import VehicleInventoryPresenter as VehicleInventoryPresenter
from gui.impl.lobby.tooltips.carousel_vehicle_tooltip import getUnsuitable2queueTooltip as getUnsuitable2queueTooltip

class FunRandomVehicleInventoryPresenter(VehicleInventoryPresenter, FunAssetPacksMixin, FunSubModesWatcher):
    def createToolTip(self, event):
        ...
    # decorador original: @hasDesiredSubMode(...)
    def _autoSelectVehicle(self):
        ...
