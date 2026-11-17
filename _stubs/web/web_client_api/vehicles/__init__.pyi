# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/vehicles/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import long as long
import nations as nations
from gui.shared.gui_items.processors.vehicle import SetEnhancementProcessor as SetEnhancementProcessor, DismountEnhancementProcessor as DismountEnhancementProcessor
from gui.shared.items_parameters import params as params
from helpers import dependency as dependency
from items import vehicles as vehicles
from skeletons.gui.shared import IItemsCache as IItemsCache
from web.web_client_api import w2c as w2c, w2capi as w2capi, Field as Field, W2CSchema as W2CSchema
from web.web_client_api.shop import ItemsWebApiMixin as ItemsWebApiMixin

class _VehicleInfoSchema(W2CSchema):
    vehicle_id: Any

class _VehicleEnhancementEquipSchema(W2CSchema):
    vehicle_int_cd: Any
    slot: Any
    enhancement_id: Any

class _VehicleEnhancementDismountSchema(W2CSchema):
    vehicle_int_cd: Any
    slot: Any

# decorador original: @w2capi(...)
class VehiclesWebApi(W2CSchema, ItemsWebApiMixin):
    itemsCache: Any
    # decorador original: @w2c(...)
    def vehicleInfo(self, cmd):
        ...
    # decorador original: @w2c(...)
    def setVehicleEnhancement(self, cmd):
        ...
    # decorador original: @w2c(...)
    def dismountVehicleEnhancement(self, cmd):
        ...
    # decorador original: @w2c(...)
    def vehicleParams(self, cmd):
        ...
    @staticmethod
    def __getAvgDamageShells(vehDescr):
        ...
    @staticmethod
    def __getPiercingPowerShells(vehDescr):
        ...
