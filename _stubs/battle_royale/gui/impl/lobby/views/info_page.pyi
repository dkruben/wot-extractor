# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/info_page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.moves import itertools as itertools
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.Scaleform.genConsts.BATTLEROYALE_ALIASES import BATTLEROYALE_ALIASES as BATTLEROYALE_ALIASES
from gui.impl.gen import R as R
from battle_royale.gui.impl.gen.view_models.views.lobby.views.info_page_model import InfoPageModel as InfoPageModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.game_mode_model import GameModeModel as GameModeModel
from battle_royale.gui.impl.lobby.br_helpers.respawn_ability import RespawnAbility as RespawnAbility
from battle_royale.gui.impl.lobby.br_helpers.utils import setEventInfo as setEventInfo
from gui.impl.gen.view_models.views.lobby.battle_pass.game_mode_rows_model import GameModeRowsModel as GameModeRowsModel
from gui.impl.gen.view_models.views.lobby.battle_pass.game_mode_cell_model import GameModeCellModel as GameModeCellModel
from gui.impl import backport as backport
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from battle_royale.gui.shared.tooltips.helper import fillProgressionPointsTableModel as fillProgressionPointsTableModel
from helpers import dependency as dependency
from helpers.time_utils import ONE_MINUTE as ONE_MINUTE
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
_rBattleRoyale = R.strings.battle_royale_infopage.battleTypes

class InfoPage(ViewImpl):
    __battleRoyaleCtrl: Any
    __battlePassCtrl: Any
    __slots__: tuple
    _isModeSelector: Any
    def __init__(self, layoutID, isModeSelector):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __updateModel(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onClose(self):
        ...
    def _onOpenVideo(self):
        ...
    def __fillSeasonDateModel(self, viewModel):
        ...
    @staticmethod
    def __fillPlatoonTooltipData(viewModel):
        ...
    def __createBattlePassTable(self):
        ...
    @staticmethod
    def __createCellName(points, previousLevel):
        ...
    @staticmethod
    def __createEmptyCell():
        ...
    @staticmethod
    def __createTableHeader(viewModel):
        ...

class InfoPageWindow(LobbyWindow):
    LAYOUT_ID: Any
    def __init__(self, isModeSelector):
        ...
