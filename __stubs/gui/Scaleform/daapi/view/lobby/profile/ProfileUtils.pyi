# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileUtils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.Scaleform.locale.PROFILE import PROFILE as PROFILE
from gui.battle_results.components import style as style
from gui.impl import backport as backport
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items.dossier.stats import _MaxVehicleStatsBlock as _MaxVehicleStatsBlock, _FalloutStatsBlock as _FalloutStatsBlock
from gui.shared.gui_items.dossier.stats import _VehiclesStatsBlock as _VehiclesStatsBlock
from helpers import dependency as dependency
from helpers import i18n as i18n
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
COMMON_SECTION_FIELDS: tuple
COMMON_SECTION_FALLOUT_FIELDS: tuple
AVERAGE_SECTION_FIELDS: tuple
AVERAGE_SECTION_FALLOUT_FIELDS: tuple
RECORD_SECTION_FIELDS: tuple
RECORD_SECTION_FALLOUT_FIELDS: tuple
STATISTICS_LAYOUT: tuple
FALLOUT_STATISTICS_LAYOUT: tuple
BATTLE_ROYALE_SECTION_FIELDS: tuple
BR_AVERAGE_SECTION_FIELDS: tuple
BR_RECORD_SECTION_FIELDS: tuple
BR_VEHICLE_RECORD_SECTION_FIELDS: tuple
BATTLE_ROYALE_STATISTICS_LAYOUT: tuple
BATTLE_ROYALE_VEHICLE_STATISTICS_LAYOUT: tuple

class _AbstractField(object):
    itemsCache: Any
    _label: Any
    _tooltip: Any
    def __init__(self, label, tooltip):
        ...
    def __call__(self, targetData, isCurrentUser):
        ...
    def isVisible(self, targetData, isCurrentUser):
        ...
    def _buildData(self, targetData, isCurrentUser):
        ...
    def _buildTooltipData(self, targetData, isCurrentUser):
        ...

class _OnlyAccountField(_AbstractField):
    def isVisible(self, targetData, isCurrentUser):
        ...

class _OnlyTechniqueField(_AbstractField):
    def isVisible(self, targetData, isCurrentUser):
        ...

class _BattlesCountField(_AbstractField):
    def _buildData(self, targetData, isCurrentUser):
        ...
    def _buildTooltipData(self, targetData, isCurrentUser):
        ...

class _WinsEfficiencyField(_AbstractField):
    def _buildData(self, targetData, isCurrentUser):
        ...

class _WinsField(_AbstractField):
    def _buildData(self, targetData, isCurrentUser):
        ...

class _SurvivalField(_AbstractField):
    def _buildData(self, targetData, isCurrentUser):
        ...

class _HitsField(_AbstractField):
    def _buildData(self, targetData, isCurrentUser):
        ...

class _DamageCoefficientField(_AbstractField):
    def __call__(self, targetData, isCurrentUser):
        ...
    def _buildData(self, targetData, isCurrentUser):
        ...
    def _buildTooltipData(self, targetData, isCurrentUser):
        ...

class _DestructionCoefficientField(_AbstractField):
    def __call__(self, targetData, isCurrentUser):
        ...
    def _buildData(self, targetData, isCurrentUser):
        ...
    def _buildTooltipData(self, targetData, isCurrentUser):
        ...

class _ArmorusingField(_AbstractField):
    def _buildData(self, targetData, isCurrentUser):
        ...
    def _buildTooltipData(self, targetData, isCurrentUser):
        ...

class _AvgDmgField(_AbstractField):
    def __call__(self, targetData, isCurrentUser):
        ...
    def _buildData(self, targetData, isCurrentUser):
        ...

class _AvgReceivedDmgField(_AbstractField):
    def _buildData(self, targetData, isCurrentUser):
        ...

class _AvgHealthRepairField(_AbstractField):
    def _buildData(self, targetData, isCurrentUser):
        ...

class _AvgEnemiesSpottedField(_AbstractField):
    def _buildData(self, targetData, isCurrentUser):
        ...

class _StunFieldMixin(object):
    lobbyContext: Any
    def isVisible(self, targetData, isCurrentUser):
        ...

class _StunNumberField(_StunFieldMixin, _OnlyTechniqueField):
    def _buildData(self, targetData, isCurrentUser):
        ...

class _AvgStunNumberField(_StunFieldMixin, _AbstractField):
    def _buildData(self, targetData, isCurrentUser):
        ...

class _AssistedStunDmgField(_StunFieldMixin, _OnlyTechniqueField):
    def __init__(self):
        ...
    def __call__(self, targetData, isCurrentUser):
        ...
    def _buildData(self, targetData, isCurrentUser):
        ...
    @staticmethod
    def _getSelfStrings():
        ...
    @staticmethod
    def _getOtherStrings():
        ...

class _AvgAssistedStunDmgField(_StunFieldMixin, _AbstractField):
    def __init__(self):
        ...
    def __call__(self, targetData, isCurrentUser):
        ...
    def _buildData(self, targetData, isCurrentUser):
        ...
    @staticmethod
    def _getSelfStrings():
        ...
    @staticmethod
    def _getOtherStrings():
        ...

class _AvgDestroyedField(_AbstractField):
    def __call__(self, targetData, isCurrentUser):
        ...
    def _buildData(self, targetData, isCurrentUser):
        ...

class _MaxXPField(_AbstractField):
    def __call__(self, targetData, isCurrentUser):
        ...
    def _buildData(self, targetData, isCurrentUser):
        ...
    def _buildTooltipData(self, targetData, isCurrentUser):
        ...

class _MaxDamageField(_AbstractField):
    _unavailableTooltip: Any
    def __init__(self, label, tooltip, unavailableTooltip):
        ...
    def __call__(self, targetData, isCurrentUser):
        ...
    def _buildData(self, targetData, isCurrentUser):
        ...
    def _buildTooltipData(self, targetData, isCurrentUser):
        ...

class _MaxDestroyedField(_AbstractField):
    def __call__(self, targetData, isCurrentUser):
        ...
    def _buildData(self, targetData, isCurrentUser):
        ...
    def _buildTooltipData(self, targetData, isCurrentUser):
        ...

class _CapturePointsField(_OnlyAccountField):
    def _buildData(self, targetData, isCurrentUser):
        ...

class _DroppedPointsField(_OnlyAccountField):
    def _buildData(self, targetData, isCurrentUser):
        ...

class _TotalVehiclesField(_OnlyAccountField):
    def _buildData(self, targetData, isCurrentUser):
        ...

class _BattleRoyaleBattlesCountField(_AbstractField):
    def _buildData(self, targetData, isCurrentUser):
        ...

class _BattleRoyaleWinsEfficiencyField(_AbstractField):
    def _buildData(self, targetData, isCurrentUser):
        ...

class _AveragePositionBR(_AbstractField):
    def _buildData(self, targetData, isCurrentUser):
        ...

class _AverageVehicleLevelBR(_AbstractField):
    def _buildData(self, targetData, isCurrentUser):
        ...

class _MaxBattleXPBR(_AbstractField):
    def _buildData(self, targetData, isCurrentUser):
        ...
    def _buildTooltipData(self, targetData, isCurrentUser):
        ...

class _MaxBattleDamageBR(_AbstractField):
    def _buildData(self, targetData, isCurrentUser):
        ...
    def _buildTooltipData(self, targetData, isCurrentUser):
        ...

class _MaxBattleFragsBR(_AbstractField):
    def _buildData(self, targetData, isCurrentUser):
        ...
    def _buildTooltipData(self, targetData, isCurrentUser):
        ...

class _MaxBattleXPVehicleBR(_AbstractField):
    def _buildData(self, targetData, isCurrentUser):
        ...

class _MaxBattleDamageVehicleBR(_AbstractField):
    def _buildData(self, targetData, isCurrentUser):
        ...

class _MaxBattleFragsVehicleBR(_AbstractField):
    def _buildData(self, targetData, isCurrentUser):
        ...

class HeaderItemsTypes(object):
    VALUE_PREFIX = 'value_'
    COMMON = 'common'
    RATIO = 'ratio'
    VALUES = 'values'

class ProfileUtils(object):
    UNAVAILABLE_VALUE = -1
    UNAVAILABLE_SYMBOL = '--'
    PERCENT_SYMBOL = '%'
    VIEW_TYPE_TABLES = 0
    VIEW_TYPE_CHARTS = 1
    VIEW_TYPE_TABLE = 2
    itemsCache: Any
    @classmethod
    def packProfileDossierInfo(cls, targetData, accountDossier):
        ...
    @staticmethod
    def packProfileCommonInfo(targetData):
        ...
    @staticmethod
    def getIconPath(icon):
        ...
    @staticmethod
    def formatFloatPercent(value):
        ...
    @staticmethod
    def getFormattedWinsEfficiency(targetData):
        ...
    @staticmethod
    def formatEfficiency(coeff2, valueReceiveFunction):
        ...
    @staticmethod
    def getEfficiencyPercent(dividend, delimiter, unavailableValue=...):
        ...
    @staticmethod
    def packLditItemData(text, description, tooltip, icon, tooltipData=None):
        ...
    @staticmethod
    def getValueOrUnavailable(targetValue):
        ...
    @staticmethod
    def getLabelDataObject(label, data):
        ...
    @staticmethod
    def getLabelViewTypeDataObject(label, data, viewType):
        ...
    @staticmethod
    def createToolTipData(bodyParamsList):
        ...
    @staticmethod
    def getTotalBattlesHeaderParam(targetData, description, tooltip):
        ...
    @classmethod
    def getVehicleRecordTooltipData(cls, getValueMethod):
        ...
    @staticmethod
    def getRecordTooltipDataByVehicle(vehicle):
        ...
    @staticmethod
    def getAvailableValueStr(value):
        ...
    @staticmethod
    def getAvgDamageBlockedValue(targetData):
        ...

class DetailedStatisticsUtils(object):
    @staticmethod
    def getDetailedDataObject(label, value, tooltip, tooltipData=None):
        ...
    @staticmethod
    def getStatistics(targetData, isCurrentUser, layout):
        ...

def _emptyField(targetData, isCurrentUser):
    ...
def _avgExpField(targetData, isCurrentUser):
    ...
def _avgAssignedDmgField(targetData, isCurrentUser):
    ...
def _avgDetectedField(targetData, isCurrentUser):
    ...
def _totalVehiclesField(targetData, isCurrentUser):
    ...
def _flagsDeliveredField(targetData, isCurrentUser):
    ...
def _flagsAbsorbedField(targetData, isCurrentUser):
    ...
def _maxWinPointsField(targetData, isCurrentUser):
    ...
def getProfileCommonInfo(userName, dossier):
    ...
