# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/ribbons_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Event as Event
from account_helpers.settings_core.settings_constants import BATTLE_EVENTS as BATTLE_EVENTS
from halloween.gui.scaleform.daapi.view.battle import ribbons_aggregator as ribbons_aggregator
from gui.Scaleform.daapi.view.battle.shared.ribbons_aggregator import DAMAGE_SOURCE as DAMAGE_SOURCE
from gui.Scaleform.daapi.view.battle.shared.ribbons_panel import BattleRibbonsPanel as BattleRibbonsPanel
from halloween.gui.scaleform.genConsts.HW_BATTLE_EFFICIENCY_TYPES import HW_BATTLE_EFFICIENCY_TYPES as HW_BATTLE_EFFICIENCY_TYPES
from halloween.gui.hw_vehicle_role_helper import getVehicleRole as getVehicleRole
from gui.impl import backport as backport
from gui.impl.gen import R as R

class HWBattleRibbonsPanel(BattleRibbonsPanel):
    onRibbonHidden: Any
    _ribbonsAggregator: Any
    _ribbonsUserSettings: Any
    _delayedRibbons: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    @property
    def aggregator(self):
        ...
    def onHide(self, ribbonId):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _onPostMortemSwitched(self, noRespawnPossible, respawnAvailable):
        ...
    def _onRespawnBaseMoving(self):
        ...
    def _getRibbonsConfig(self):
        ...
    def _getRibbonFormatter(self, ribbon):
        ...
    def _onSettingsChanged(self, diff):
        ...
    def __setUserSettings(self, settingName, value):
        ...
