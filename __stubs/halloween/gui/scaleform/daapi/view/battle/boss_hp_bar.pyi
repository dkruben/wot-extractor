# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/boss_hp_bar.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BattleReplay as BattleReplay
import BigWorld as BigWorld
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.battle_control import avatar_getter as avatar_getter
from gui.impl import backport as backport
from gui.impl.gen import R as R
from halloween.gui.scaleform.daapi.view.battle.anomalies_watcher_mixin import AnomaliesWatcherMixin as AnomaliesWatcherMixin
from halloween_common.halloween_constants import ARENA_BONUS_TYPE_TO_LEVEL as ARENA_BONUS_TYPE_TO_LEVEL
from halloween.gui.scaleform.daapi.view.meta.BossHPBarMeta import BossHPBarMeta as BossHPBarMeta
from HWArenaInfoBossHealthBarComponent import getArenaInfoBossHealthBarComponent as getArenaInfoBossHealthBarComponent

class HWBossHPBar(AnomaliesWatcherMixin, BossHPBarMeta):
    BOSS_FIGHT_TITLE_TML = 'boss{difficulty}'
    needToShow: Any
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __onActivated(self):
        ...
    def __showBossHPBar(self, needToShow):
        ...
    def __onBossHealthChanged(self, newHealth, prevHealth, bossVehicleID, attackerID, attackReasonID):
        ...
    def __updateBossHPBar(self, lives, health, maxHealth):
        ...
    def __onMinionsCountChanged(self, amount):
        ...
    def __onBossHPBarVisibilityChanged(self, isVisible):
        ...
    def __onRoundFinished(self, winnerTeam, *args):
        ...
