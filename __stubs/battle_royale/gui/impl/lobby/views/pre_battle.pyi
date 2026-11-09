# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/pre_battle.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
import BigWorld as BigWorld
import ArenaType as ArenaType
from BattleRoyaleTournament import MAX_PLAYERS_IN_SQUAD as MAX_PLAYERS_IN_SQUAD
from battle_royale.gui.impl.gen.view_models.views.lobby.views.pre_battle_view_model import PreBattleViewModel as PreBattleViewModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.team_model import TeamModel as TeamModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.user_extended_model import UserExtendedModel as UserExtendedModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.user_model import UserModel as UserModel
from gui.Scaleform.Waiting import Waiting as Waiting
from helpers import dependency as dependency
from wg_async import wg_async as wg_async, wg_await as wg_await
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
from frameworks.wulf import ViewSettings as ViewSettings, Array as Array, WindowFlags as WindowFlags
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.dialogs.builders import WarningDialogBuilder as WarningDialogBuilder
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.impl.dialogs import dialogs as dialogs
from gui.impl.gen.view_models.ui_kit.gf_drop_down_item import GfDropDownItem as GfDropDownItem
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from gui.prb_control import prbEntityProperty as prbEntityProperty
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController, IBattleRoyaleTournamentController as IBattleRoyaleTournamentController
from skeletons.gui.shared import IItemsCache as IItemsCache

class BattleRoyalePreBattleWindow(WindowImpl):
    def __init__(self, layer, **kwargs):
        ...

class PreBattleView(ViewImpl):
    __battleRoyaleController: Any
    __battleRoyaleTournamentController: Any
    __itemsCache: Any
    __isObserver: Any
    __canStartBattle: Any
    __isSolo: Any
    __countOfReady: Any
    __maps: Any
    def __init__(self, layoutID):
        ...
    # decorador original: @prbEntityProperty
    def prbEntity(self):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def __onClose(self):
        ...
    def __onBattleClick(self, args=None):
        ...
    # decorador original: @wg_async
    def __showConfirmation(self, mapId):
        ...
    def __getMaps(self):
        ...
    def __initModel(self):
        ...
    def __updateParticipants(self):
        ...
    def __convertToPlayers(self, participants):
        ...
    def __setCurrentTeam(self, model, players):
        ...
    def __userClearData(self, user):
        ...
    def __initMaps(self):
        ...
    def __allPlayersIsReady(self):
        ...
