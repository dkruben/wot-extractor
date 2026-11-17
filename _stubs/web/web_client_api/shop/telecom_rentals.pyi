# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/shop/telecom_rentals.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from account_helpers.telecom_rentals import TelecomRentals as TelecomRentals
from gui import SystemMessages as SystemMessages
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.gui_items.Vehicle import getUserName as getUserName
from items.vehicles import getVehicleType as getVehicleType
from web.web_client_api import W2CSchema as W2CSchema, w2c as w2c, Field as Field
_logger: Any

class _TelecomRentalsRentVehicleInfoSchema(W2CSchema):
    vehCD: Any

class TelecomRentalsWebApiMixin(object):
    # decorador original: @w2c(...)
    def getTelecomRentalsInfo(self, cmd):
        ...
    # decorador original: @w2c(...)
    def telecomRentDelayed(self, cmd):
        ...
