# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/common/player_satisfaction_rating/player_satisfaction_sound.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from enum import Enum as Enum
import SoundGroups as SoundGroups
from constants import PlayerSatisfactionRating as PlayerSatisfactionRating
_logger: Any
_RATING_TO_SOUND_MAP: dict

class SoundEvents(Enum):
    BETTER = 'post_battle_voting_better'
    USUAL = 'post_battle_voting_usual'
    WORSE = 'post_battle_voting_worse'

def playSoundForRating(rating):
    ...
