# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/RareAchievementsCache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import re as re
from functools import partial as partial
from future.utils import lfilter as lfilter
import ResMgr as ResMgr
import Event as Event
from debug_utils import LOG_WARNING as LOG_WARNING, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION, LOG_DEBUG as LOG_DEBUG
from helpers import i18n as i18n, getClientLanguage as getClientLanguage
from account_helpers.rare_achievements import getRareAchievementImage as getRareAchievementImage, getRareAchievementImageUrl as getRareAchievementImageUrl, getRareAchievementImageBig as getRareAchievementImageBig, getRareAchievementText as getRareAchievementText
from skeletons.gui.shared.utils import IRaresCache as IRaresCache
URL_NAMES: dict

class IMAGE_TYPE(object):
    IT_67X71 = 1
    IT_180X180 = 2

class IMAGE_PATH(object):
    IT_67X71 = 'gui/maps/icons/achievement/'
    IT_180X180 = 'gui/maps/icons/achievement/big/'

class RaresCache(IRaresCache):
    RARE_ACHIEVEMENT_PREFIX = 'rare'
    RARE_ACHIEVEMENT_PATTERN: Any
    RARE_ACHIEVEMENT_ICON_PATTERN: Any
    __cache: Any
    __local: Any
    onTextReceived: Any
    onImageReceived: Any
    def __init__(self):
        ...
    def request(self, listOfIds):
        ...
    def __onTextReceived(self, rareID, text):
        ...
    def __onImageReceived(self, imgType, imgID, imageData):
        ...
    def isLocallyLoaded(self, achieveID):
        ...
    def getTitle(self, achieveID):
        ...
    def getDescription(self, achieveID):
        ...
    def getImageData(self, imgType, achieveID):
        ...
    def getHeroInfo(self, achieveID):
        ...
    def getConditions(self, achieveID):
        ...
    def getAchievementImageUrl(self, imgType, achieveID):
        ...
    @classmethod
    def __getRareAchievementID(cls, rareName):
        ...
