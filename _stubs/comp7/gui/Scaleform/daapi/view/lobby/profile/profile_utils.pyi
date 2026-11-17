# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/profile/profile_utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.daapi.view.lobby.profile import ProfileUtils as commonProfileUtils
from gui.Scaleform.daapi.view.lobby.profile.ProfileUtils import ProfileUtils as ProfileUtils, DetailedStatisticsUtils as DetailedStatisticsUtils
from gui.Scaleform.locale.PROFILE import PROFILE as PROFILE
from gui.impl import backport as backport
COMMON_SECTION_COMP7_FIELDS: tuple
COMMON_SECTION_COMP7_VEHICLE_FIELDS: tuple
AVERAGE_SECTION_COMP7_FIELDS: tuple
AVERAGE_SECTION_COMP7_VEHICLE_FIELDS: tuple
RECORD_SECTION_COMP7_FIELDS: tuple
RECORD_SECTION_COMP7_VEHICLE_FIELDS: tuple
COMP7_STATISTICS_LAYOUT: tuple
COMP7_VEHICLE_STATISTICS_LAYOUT: tuple

class _AvgPrestigePointsField(commonProfileUtils._AbstractField):
    def _buildData(self, targetData, isCurrentUser):
        ...

class _AvgPoiCapturedField(commonProfileUtils._AbstractField):
    def _buildData(self, targetData, isCurrentUser):
        ...

class _AvgRoleSkillUsedField(commonProfileUtils._AbstractField):
    def _buildData(self, targetData, isCurrentUser):
        ...

class _AvgAssistedStunDmgComp7Field(commonProfileUtils._AvgAssistedStunDmgField):
    @staticmethod
    def _getSelfStrings():
        ...
    @staticmethod
    def _getOtherStrings():
        ...

class _MaxPrestigePointsField(commonProfileUtils._AbstractField):
    def __call__(self, targetData, isCurrentUser):
        ...
    def _buildData(self, targetData, isCurrentUser):
        ...
    def _buildTooltipData(self, targetData, isCurrentUser):
        ...
    def __getVehicle(self, targetData):
        ...

class _MaxWinSeriesField(commonProfileUtils._AbstractField):
    def _buildData(self, targetData, isCurrentUser):
        ...

class _MaxEquipmentDamageDealtField(commonProfileUtils._AbstractField):
    def __call__(self, targetData, isCurrentUser):
        ...
    def _buildData(self, targetData, isCurrentUser):
        ...
    def _buildTooltipData(self, targetData, isCurrentUser):
        ...
    def __getVehicle(self, targetData):
        ...

class _MaxHealthRepairField(commonProfileUtils._AbstractField):
    def __call__(self, targetData, isCurrentUser):
        ...
    def _buildData(self, targetData, isCurrentUser):
        ...
    def _buildTooltipData(self, targetData, isCurrentUser):
        ...
    def __getVehicle(self, targetData):
        ...

class _PoiCapturedField(commonProfileUtils._OnlyAccountField):
    def _buildData(self, targetData, isCurrentUser):
        ...

def _avgAssignedDmgComp7Field(targetData, isCurrentUser):
    ...
