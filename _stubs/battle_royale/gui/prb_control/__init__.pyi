# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/prb_control/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from battle_royale.gui.impl.lobby.views.event_banner import BattleRoyaleEventBanner as BattleRoyaleEventBanner, isBattleRoyaleEntryPointAvailable as isBattleRoyaleEntryPointAvailable
from battle_royale.gui.impl.lobby.views.mode_selector.items.battle_royale_mode_selector_item import BattleRoyaleModeSelectorItem as BattleRoyaleModeSelectorItem
from battle_royale.gui.impl.lobby.views.st_patrick_banner import StPatrickEventBanner as StPatrickEventBanner, isStPatrickEntryPointAvailable as isStPatrickEntryPointAvailable
from battle_royale.gui.prb_control.entities.regular.pre_queue import entity as br_entity
from battle_royale.gui.prb_control.entities.regular.squad.entity import BattleRoyaleSquadEntryPoint as BattleRoyaleSquadEntryPoint, BattleRoyaleSquadEntity as BattleRoyaleSquadEntity
from battle_royale.gui.prb_control.entities.tournament.legacy.entity import BattleRoyaleTournamentEntryPoint as BattleRoyaleTournamentEntryPoint
from battle_royale.gui.prb_control.entities.tournament.pre_queue import entity as br_tournament
from battle_royale.gui.prb_control.storages.battle_royale_storage import BattleRoyaleStorage as BattleRoyaleStorage
from constants import QUEUE_TYPE as QUEUE_TYPE, PREBATTLE_TYPE as PREBATTLE_TYPE
from gui.Scaleform.daapi.view.common.battle_royale.br_helpers import currentHangarIsBattleRoyale as currentHangarIsBattleRoyale
from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer as EventBannersContainer
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from gui.prb_control.storages import makeQueueName as makeQueueName
from gui.shared.system_factory import registerQueueEntity as registerQueueEntity, registerEntryPoint as registerEntryPoint, registerUnitEntryPoint as registerUnitEntryPoint, registerUnitEntryPointByType as registerUnitEntryPointByType, registerUnitEntity as registerUnitEntity, registerLegacyEntryPointByType as registerLegacyEntryPointByType, registerPrbStorage as registerPrbStorage, registerCustomizationHangarDecorator as registerCustomizationHangarDecorator, registerBannerEntryPointValidator as registerBannerEntryPointValidator, registerModeSelectorItem as registerModeSelectorItem, registerBattleButtonManualControl as registerBattleButtonManualControl
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleTournamentController as IBattleRoyaleTournamentController

# decorador original: @dependency.replace_none_kwargs(...)
def battleButtonTournamentReady(prbEntity, ctrl=None):
    ...
def registerBRPrebattles():
    ...
