# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/achievements/achievements_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from dossiers2.custom.records import RECORD_DB_IDS as RECORD_DB_IDS, DB_ID_TO_RECORD as DB_ID_TO_RECORD
from dossiers2.ui.achievements import ACHIEVEMENT_TYPE as ACHIEVEMENT_TYPE
from gui.impl.gen.view_models.views.lobby.achievements.achievement_model import AchievementType as AchievementType, AchievementModel as AchievementModel, CounterType as CounterType
from gui.impl.gen.view_models.views.lobby.achievements.views.achievement_section_model import AchievementSectionModel as AchievementSectionModel
from gui.shared.gui_items.dossier.achievements.abstract import isRareAchievement as isRareAchievement
COUNTER_TYPE_MAP: dict
_ACHIEVEMENT_TYPE_MAP: dict

def fillAchievementSectionModel(section):
    ...
def fillAchievementModel(achievement):
    ...
def convertAchievementsToDbIds(achivements):
    ...
def convertDbIdsToAchievements(layout, dossier=None):
    ...
