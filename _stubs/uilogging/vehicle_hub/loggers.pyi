# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/vehicle_hub/loggers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from uilogging.base.logger import MetricsLogger as MetricsLogger, createPartnerID as createPartnerID
from uilogging.vehicle_hub.constants import LogActions as LogActions, Features as Features, Tabs as Tabs, TIME_LIMIT as TIME_LIMIT
from uilogging.vehicle_hub.constants import LogItems as LogItems

class ArmorTabLogger(MetricsLogger):
    __slots__: tuple
    _vehicleCD: Any
    _partnerID: Any
    def __init__(self, vehCD):
        ...
    @property
    def vehicleCD(self):
        ...
    @property
    def partnerID(self):
        ...
    def logOpen(self):
        ...
    def logClose(self):
        ...
    def tooltipOpened(self):
        ...
    def armorTooltipClosed(self):
        ...
    def _tooltipClosed(self, item):
        ...
