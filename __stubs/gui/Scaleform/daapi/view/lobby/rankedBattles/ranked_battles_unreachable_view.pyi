# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/rankedBattles/ranked_battles_unreachable_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.ranked_battles.ranked_helpers.sound_manager import RANKED_SUBVIEW_SOUND_SPACE as RANKED_SUBVIEW_SOUND_SPACE
from gui.ranked_battles.ranked_builders.unreachable_vos import getUnreachableVO as getUnreachableVO
from gui.Scaleform.daapi import LobbySubView as LobbySubView
from gui.Scaleform.daapi.view.meta.RankedBattlesUnreachableViewMeta import RankedBattlesUnreachableViewMeta as RankedBattlesUnreachableViewMeta
from gui.shared.utils.scheduled_notifications import PeriodicNotifier as PeriodicNotifier
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController

class RankedBattlesUnreachableView(LobbySubView, RankedBattlesUnreachableViewMeta):
    __rankedController: Any
    _COMMON_SOUND_SPACE = RANKED_SUBVIEW_SOUND_SPACE
    __background_alpha__ = 0.5
    __currentSeason: Any
    __periodicNotifier: Any
    def __init__(self, **kwargs):
        ...
    def onEscapePress(self):
        ...
    def onCloseBtnClick(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __close(self):
        ...
    def __checkDestroy(self):
        ...
    def __timeTillCurrentSeasonEnd(self):
        ...
    def __update(self):
        ...
    def __updateData(self):
        ...
