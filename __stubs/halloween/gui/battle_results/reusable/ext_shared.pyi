# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/battle_results/reusable/ext_shared.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.battle_results.reusable.shared import VehicleSummarizeInfo as VehicleSummarizeInfo, VehicleDetailedInfo as VehicleDetailedInfo, no_key_error as no_key_error

class HalloweenVehicleDetailedInfo(VehicleDetailedInfo):
    __slots__: tuple
    @classmethod
    # decorador original: @no_key_error
    def makeForVehicle(cls, vehicleID, vehicle, player, vehicleRecords, critsRecords=None):
        ...
    @property
    def hwPhase(self):
        ...
    @property
    def hwPhasesCount(self):
        ...
    @property
    def effectivenessKeys(self):
        ...
    @property
    def bossKeys(self):
        ...
    @property
    def totalKeys(self):
        ...
    @property
    def hwTeamContribution(self):
        ...
    @property
    def hwTeamFightPlace(self):
        ...
    @property
    def hwBossFightDamage(self):
        ...
    @property
    def hwVehiclesRespawnCount(self):
        ...
    @property
    def hwHangarLoot(self):
        ...

class HalloweenVehicleSummarizeInfo(VehicleSummarizeInfo):
    @property
    def hwPhase(self):
        ...
    @property
    def hwPhasesCount(self):
        ...
    @property
    def effectivenessKeys(self):
        ...
    @property
    def bossKeys(self):
        ...
    @property
    def totalKeys(self):
        ...
    @property
    def hwTeamContribution(self):
        ...
    @property
    def hwTeamFightPlace(self):
        ...
    @property
    def hwBossFightDamage(self):
        ...
    @property
    def hwVehiclesRespawnCount(self):
        ...
    @property
    def hwHangarLoot(self):
        ...
