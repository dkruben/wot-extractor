# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/abilities/corroding_shot_indicator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
import BigWorld as BigWorld
from helpers import dependency as dependency
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView as IAbstractPeriodView
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from constants import EQUIPMENT_STAGES as EQUIPMENT_STAGES
from gui.Scaleform.daapi.view.meta.CorrodingShotIndicatorMeta import CorrodingShotIndicatorMeta as CorrodingShotIndicatorMeta
from battle_royale.gui.constants import BattleRoyaleEquipments as BattleRoyaleEquipments
from Event import EventsSubscriber as EventsSubscriber

class CorrodingShotIndicator(CorrodingShotIndicatorMeta, IAbstractPeriodView):
    __sessionProvider: Any
    __isEnabled: Any
    _es: Any
    def __init__(self):
        ...
    def _destroy(self):
        ...
    def __onEquipmentComponentUpdated(self, equipmentName, vehicleID, abilityInfo):
        ...
    def __onVehicleChanged(self, _):
        ...
    def __onCrosshairPositionChanged(self, *args):
        ...
    def __enable(self):
        ...
    def __disable(self):
        ...
    def __onCameraChanged(self, cameraName, currentVehicleId=None):
        ...
