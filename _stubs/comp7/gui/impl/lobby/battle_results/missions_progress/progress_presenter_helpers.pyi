# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/battle_results/missions_progress/progress_presenter_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from comp7.gui.impl.lobby.battle_results.missions_progress.comp7_weekly_missions_progress import Comp7WeeklyMissionsProgressPresenter as Comp7WeeklyMissionsProgressPresenter
from comp7.gui.impl.lobby.battle_results.missions_progress.progress_filters import comp7WeeklyQuestsProgressFilter as comp7WeeklyQuestsProgressFilter, comp7CustomizationQuestsProgressFilter as comp7CustomizationQuestsProgressFilter, comp7CommonBattleQuestsProgressFilter as comp7CommonBattleQuestsProgressFilter, comp7VehicleProgressFilter as comp7VehicleProgressFilter
from comp7.gui.impl.lobby.battle_results.missions_progress.comp7_customization_progress import Comp7CustomizationProgressPresenter as Comp7CustomizationProgressPresenter
from gui.impl.lobby.battle_results.missions_progress.new_module_vehicle_progress import NewModuleVehicleProgressPresenter as NewModuleVehicleProgressPresenter
from gui.shared.system_factory import collectProgressionPresenters as collectProgressionPresenters
from helpers import dependency as dependency
from skeletons.gui.server_events import IEventsCache as IEventsCache
from gui.impl.lobby.battle_results.missions_progress.common_battle_quests_progress import CommonBattleQuestsProgressPresenter as CommonBattleQuestsProgressPresenter

# decorador original: @dependency.replace_none_kwargs(...)
def getComp7ProgressionCategoriesPresenters(eventsCache=None):
    ...
