# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/sounds/sound_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from shared_utils import CONST_CONTAINER as CONST_CONTAINER
PLAYING_SOUND_CHECK_PERIOD = 1.0
IS_ADVANCED_LOGGING = False

class EnabledStatus(object):
    ENABLED_DEFAULT = 0
    ENABLED_BY_USER = 1
    DISABLED = 2
    @classmethod
    def isEnabled(cls, status):
        ...

class SoundSystems(CONST_CONTAINER):
    UNKNOWN = 0
    WWISE = 1
    @classmethod
    def getUserName(cls, sysID):
        ...

class SoundFilters(CONST_CONTAINER):
    EMPTY = 1
    FILTERED_HANGAR = 2
    FORT_FILTER = 3
    HANGAR_OVERLAY = 5
    MARATHON_FILTER = 6
    HANGAR_PLACE_TASKS_DAILY = 7
    HANGAR_PLACE_TASKS_MISSIONS = 8
    HANGAR_PLACE_TASKS_EVENTS = 10
    HANGAR_PLACE_TASKS_BATTLE_MATTERS = 11

class SPEAKERS_CONFIG(object):
    AUTO_DETECTION = 0
    SPEAKER_SETUP_2_0 = 2
    SPEAKER_SETUP_5_1 = 5
    SPEAKER_SETUP_7_1 = 7
    RANGE: tuple
