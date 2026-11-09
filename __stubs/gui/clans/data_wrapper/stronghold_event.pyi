# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/clans/data_wrapper/stronghold_event.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from gui.clans.data_wrapper.utils import FieldsCheckerMixin as FieldsCheckerMixin, fmtUnavailableValue as fmtUnavailableValue
from shared_utils import makeTupleByDict as makeTupleByDict
_StrongholdEventClanInfoData: Any
_StrongholdEventConfig: Any
_StrongholdEventSettingsData: Any

class StrongholdEventClanInfoData(_StrongholdEventClanInfoData, FieldsCheckerMixin):
    # decorador original: @fmtUnavailableValue(...)
    def getPrimeTimeStart(self):
        ...
    # decorador original: @fmtUnavailableValue(...)
    def getPrimeTimeEnd(self):
        ...

class StrongholdEventConfig(_StrongholdEventConfig, FieldsCheckerMixin):
    # decorador original: @fmtUnavailableValue(...)
    def getVisibleStartDate(self):
        ...
    # decorador original: @fmtUnavailableValue(...)
    def getVisibleEndDate(self):
        ...
    # decorador original: @fmtUnavailableValue(...)
    def getStartDate(self):
        ...
    # decorador original: @fmtUnavailableValue(...)
    def getEndDate(self):
        ...
    # decorador original: @fmtUnavailableValue(...)
    def getUnfreezeVehicleRoles(self):
        ...

class StrongholdEventSettingsData(_StrongholdEventSettingsData, FieldsCheckerMixin):
    # decorador original: @fmtUnavailableValue(...)
    def getEventConfig(self):
        ...
    def getStartDate(self):
        ...
    def getEndDate(self):
        ...
