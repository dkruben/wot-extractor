# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/dossier/achievements/abstract/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from future.utils import viewvalues as viewvalues
from helpers import dependency as dependency
from skeletons.gui.server_events import IEventsCache as IEventsCache
from .mixins import Deprecated as Deprecated
from .mixins import Quest as Quest
from .mixins import HasVehiclesList as _HasVehiclesList
from .mixins import NoProgressBar as NoProgressBar
from .class_progress import ClassProgressAchievement as ClassProgressAchievement
from .historical import HistoricalAchievement as HistoricalAchievement
from .nation_specific import NationSpecificAchievement as NationSpecificAchievement
from .rare import RareAchievement as RareAchievement
from .regular import RegularAchievement as RegularAchievement
from .series import SeriesAchievement as SeriesAchievement
from .regular_ext import RegularExtAchievement as RegularExtAchievement
from .simple_progress import SimpleProgressAchievement as SimpleProgressAchievement
from .stage import StageAchievement as StageAchievement
__all__: tuple

class DeprecatedAchievement(Deprecated, RegularAchievement):
    ...

class QuestAchievement(Quest, RegularAchievement):
    ...

class DeprecatedClassAchievement(Deprecated, NoProgressBar, ClassProgressAchievement):
    ...

def isRareAchievement(achievement):
    ...
def isSeriesAchievement(achievement):
    ...
def achievementHasVehiclesList(achievement):
    ...
def getCompletedPersonalMissionsCount(branch, classifiers):
    ...
