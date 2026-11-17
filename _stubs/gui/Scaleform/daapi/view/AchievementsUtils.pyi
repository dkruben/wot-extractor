# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/AchievementsUtils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from dossiers2.ui.achievements import ACHIEVEMENT_SECTION as ACHIEVEMENT_SECTION, ACHIEVEMENT_TYPE as ACHIEVEMENT_TYPE
from dossiers2.custom.config import RECORD_CONFIGS as RECORD_CONFIGS
from gui.shared.gui_items.dossier.achievements.abstract import isRareAchievement as isRareAchievement
from gui.shared.gui_items.dossier.achievements import MarkOnGunAchievement as MarkOnGunAchievement
from gui.Scaleform.genConsts.ACHIEVEMENTS_ALIASES import ACHIEVEMENTS_ALIASES as ACHIEVEMENTS_ALIASES

class AchievementsUtils(object):
    @staticmethod
    def packAchievementList(target, dossierType, dossierCompactDescriptor, isDossierForCurrentUser, defaultShowProgress=True, defaultSeriesCounter=None):
        ...
    @staticmethod
    def packAchievement(achievement, dossierType, dossierCompDescr, isDossierForCurrentUser, defaultShowProgress=True, defaultSeriesCounter=None):
        ...
    @staticmethod
    def getCommonAchievementData(achievement, dossierType, dossierCompDescr, iconAlpha=1):
        ...
    @staticmethod
    def getBattleResultAchievementData(achievement, aType, customData, isUnique=False):
        ...
    @staticmethod
    def getCounterType(achievement, defaultSeriesCounter=None):
        ...
