# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/battle_results/reusable/fort_rush_shared.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.battle_results.reusable.shared import VehicleSummarizeInfo as VehicleSummarizeInfo, VehicleDetailedInfo as VehicleDetailedInfo, no_key_error as no_key_error

class FortRushVehicleDetailedInfo(VehicleDetailedInfo):
    __slots__: tuple
    @classmethod
    # decorador original: @no_key_error
    def makeForVehicle(cls, vehicleID, vehicle, player, vehicleRecords, critsRecords=None):
        ...
    @property
    def fortRushScore(self):
        ...

class FortRushVehicleSummarizeInfo(VehicleSummarizeInfo):
    @property
    def fortRushScore(self):
        ...
