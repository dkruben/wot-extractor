# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/battle/page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import logging as logging
from fort_rush.gui.battle_control.controllers.respawn_ctrl import ISpawnListener as ISpawnListener
from fort_rush.gui.scaleform.daapi.view.battle.crosshair.container import FortRushCrosshairPanelContainer as FortRushCrosshairPanelContainer
from fort_rush.gui.shared.events import RespawnCtrlEvent as RespawnCtrlEvent
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES as BATTLE_VIEW_ALIASES
from gui.Scaleform.daapi.view.battle.shared.indicators import createDamageIndicator as createDamageIndicator
from gui.Scaleform.daapi.view.battle.shared import finish_sound_player as finish_sound_player, drone_music_player as drone_music_player
from gui.Scaleform.daapi.view.battle.shared.start_countdown_sound_player import StartCountdownSoundPlayer as StartCountdownSoundPlayer
from gui.Scaleform.daapi.view.battle.classic.page import DynamicAliases as ClassicDynamicAliases
from gui.Scaleform.daapi.view.battle.shared.indicators import createPredictionIndicator as createPredictionIndicator
from gui.Scaleform.daapi.view.battle.shared.page import ComponentsConfig as ComponentsConfig
from fort_rush.gui.fort_rush_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import ARENA_PERIOD as ARENA_PERIOD
from fort_rush.gui.impl.battle import showFortRushHud as showFortRushHud
from fort_rush.gui.scaleform.daapi.view.battle.markers2d.manager import FortRushMarkersManager as FortRushMarkersManager
from fort_rush.gui.scaleform.genConsts.FORT_RUSH_BATTLE_VIEW_ALIASES import FORT_RUSH_BATTLE_VIEW_ALIASES as FORT_RUSH_BATTLE_VIEW_ALIASES
from fort_rush.gui.scaleform.daapi.view.meta.FortRushBattlePageMeta import FortRushBattlePageMeta as FortRushBattlePageMeta
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from fort_rush.gui.scaleform.daapi.view.battle.battle_hints import FortRushBattleHintComponent as FortRushBattleHintComponent
from gui.battle_control.controllers.battle_hints.queues import BattleHintQueueParams as BattleHintQueueParams
from fort_rush.gui.scaleform.daapi.view.battle.battle_hints import FortRushBattleHintsQueue as FortRushBattleHintsQueue, FortRushBattleHint as FortRushBattleHint
_logger: Any
_CONFIG: Any
_EXTENDED_CONFIG: Any
EXT_CONFIG: Any
_EXTERNAL_COMPONENTS: tuple

class _ComponentsConfig(ComponentsConfig):
    def __init__(self):
        ...

class DynamicAliases(CONST_CONTAINER):
    FORT_RUSH_BATTLE_HINT = 'fortRushBattleHint'

class FortRushBattlePage(FortRushBattlePageMeta, ISpawnListener):
    __savedVisibleComponents: Any
    def __init__(self, components=None, external=..., fullStatsAlias=..., **kwargs):
        ...
    def _populate(self):
        ...
    def _onBattleLoadingFinish(self):
        ...
    def _startBattleSession(self):
        ...
    def _stopBattleSession(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def __onArenaPeriodChange(self, period, *_):
        ...
    def __onRoundFinished(self, *_):
        ...
    def __setVisibilityInitBattlePeriod(self):
        ...
    def _dispose(self):
        ...
    def showSpawnPoints(self):
        ...
    def closeSpawnPoints(self):
        ...
    def __toggleExternalComponentsVisibility(self, externalComponents, isVisible):
        ...
