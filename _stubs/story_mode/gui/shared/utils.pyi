# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/shared/utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from future.utils import viewitems as viewitems
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.framework.entities.DisposableEntity import EntityState as EntityState
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA as POP_UP_CRITERIA
from gui.server_events.awards_formatters import AwardsPacker as AwardsPacker, AWARDS_SIZES as AWARDS_SIZES
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from story_mode.gui.story_mode_gui_constants import VIEW_ALIAS as VIEW_ALIAS
from story_mode.gui.shared.bonuses_formatters import StoryModeBonusesAwardsComposer as StoryModeBonusesAwardsComposer, getImgPath as getImgPath
from story_mode.gui.shared.packers.bonus import getSMFormattersMap as getSMFormattersMap
from story_mode.gui.impl.gen.view_models.views.lobby.reward_model import RewardModel as RewardModel
from story_mode_common.configs.story_mode_missions import missionsSchema as missionsSchema
from wg_async import wg_async as wg_async, AsyncEvent as AsyncEvent, wg_await as wg_await
from gui.Scaleform.framework.application import AppEntry as AppEntry

# decorador original: @wg_async
def waitForLobby():
    ...
def getRewardList(progressInfo, isBattlePassActive, forBattleResults=False):
    ...
def getTasksCount(progressInfo):
    ...
def formatAndFillRewards(rewards, rewardsModel, idGenerator, bonusCache, maxBonusesInView):
    ...
