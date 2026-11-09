# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/ribbons_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from future.utils import viewvalues as viewvalues
from account_helpers.settings_core.settings_constants import BATTLE_EVENTS as BATTLE_EVENTS
from last_stand.gui.scaleform.daapi.view.battle import ribbons_aggregator as ribbons_aggregator
from gui.Scaleform.daapi.view.battle.shared.ribbons_aggregator import DAMAGE_SOURCE as DAMAGE_SOURCE
from gui.Scaleform.daapi.view.battle.shared.ribbons_panel import BattleRibbonsPanel as BattleRibbonsPanel
from last_stand.gui.scaleform.genConsts.LS_BATTLE_EFFICIENCY_TYPES import LS_BATTLE_EFFICIENCY_TYPES as LS_BATTLE_EFFICIENCY_TYPES
from last_stand.gui.ls_vehicle_role_helper import getVehicleRole as getVehicleRole
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
_DELAYED_RIBBONS_UPDATE_PERIOD = 0.1

class LSBattleRibbonsPanel(BattleRibbonsPanel):
    _ribbonsAggregator: Any
    _ribbonsUserSettings: Any
    _callbackDelayer: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    @property
    def aggregator(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _onPostMortemSwitched(self, noRespawnPossible, respawnAvailable):
        ...
    def _onRespawnBaseMoving(self):
        ...
    def _shouldShowRibbon(self, ribbon):
        ...
    def _getRibbonsConfig(self):
        ...
    def _getRibbonFormatter(self, ribbon):
        ...
    def _onSettingsChanged(self, diff):
        ...
    def _canBeShown(self, ribbon):
        ...
    def _delayedRibbonsUpdate(self):
        ...
    def __setUserSettings(self, settingName, value):
        ...
