# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/progressive_reward/progressive_award_sounds.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import WWISE as WWISE
from shared_utils import CONST_CONTAINER as CONST_CONTAINER

class ProgressiveRewardSoundEvents(CONST_CONTAINER):
    PROGRESSIVE_REWARD_VIEW_GROUP = 'STATE_overlay_hangar_general'
    PROGRESSIVE_REWARD_VIEW_ENTER = 'STATE_overlay_hangar_general_on'
    PROGRESSIVE_REWARD_VIEW_EXIT = 'STATE_overlay_hangar_general_off'
    PROGRESSIVE_REWARD_AWARD_GROUP = 'STATE_overlay_hangar_general'
    PROGRESSIVE_REWARD_AWARD_ENTER = 'STATE_overlay_hangar_general_on'
    PROGRESSIVE_REWARD_AWARD_EXIT = 'STATE_overlay_hangar_general_off'

def setSoundState(groupName, stateName, eventName=None):
    ...
def playSound(eventName):
    ...
