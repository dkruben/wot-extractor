# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/battle_results/reusable/ext_shared.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.battle_results.reusable.shared import VehicleSummarizeInfo as VehicleSummarizeInfo, VehicleDetailedInfo as VehicleDetailedInfo, no_key_error as no_key_error

class LSVehicleDetailedInfo(VehicleDetailedInfo):
    __slots__: tuple
    @classmethod
    # decorador original: @no_key_error
    def makeForVehicle(cls, vehicleID, vehicle, player, vehicleRecords, critsRecords=None):
        ...
    @property
    def prevBestMissionsCount(self):
        ...
    @property
    def phase(self):
        ...
    @property
    def phasesCount(self):
        ...
    @property
    def effectivenessPoints(self):
        ...
    @property
    def obeliskPoints(self):
        ...
    @property
    def totalPoints(self):
        ...
    @property
    def teamContribution(self):
        ...
    @property
    def teamFightPlace(self):
        ...
    @property
    def respawnsCount(self):
        ...
    @property
    def completedDifficultyMissions(self):
        ...

class LSVehicleSummarizeInfo(VehicleSummarizeInfo):
    @property
    def prevBestMissionsCount(self):
        ...
    @property
    def phase(self):
        ...
    @property
    def phasesCount(self):
        ...
    @property
    def effectivenessPoints(self):
        ...
    @property
    def obeliskPoints(self):
        ...
    @property
    def totalPoints(self):
        ...
    @property
    def teamContribution(self):
        ...
    @property
    def teamFightPlace(self):
        ...
    @property
    def respawnsCount(self):
        ...
    @property
    def completedDifficultyMissions(self):
        ...
