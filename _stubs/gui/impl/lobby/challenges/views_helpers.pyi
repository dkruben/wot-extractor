# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/challenges/views_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
import constants as constants
from challenges_common import CHALLENGE_MIN_VEHICLE_LEVEL as CHALLENGE_MIN_VEHICLE_LEVEL
from gui.shared.missions.packers.events import ChallengeMissionUIDataPacker as ChallengeMissionUIDataPacker
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.challenges import IChallengesController as IChallengesController
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.challenge_missions.challenge_quest_model import ChallengeState as ChallengeState, ChallengeQuestModel as ChallengeQuestModel
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA as REQ_CRITERIA

# decorador original: @dependency.replace_none_kwargs(...)
def updateChallengeModel(challengeItem, tooltipData, challenges=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getSuitableVehicles(itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getChallengeState(challenge, progress, challenges=None):
    ...
def parseChallengeQuestId(questID):
    ...
