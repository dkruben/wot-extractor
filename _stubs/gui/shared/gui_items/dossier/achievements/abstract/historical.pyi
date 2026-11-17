# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/dossier/achievements/abstract/historical.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.shared.gui_items.dossier.achievements.abstract.regular import RegularAchievement as RegularAchievement
from gui.shared.gui_items.dossier.achievements.abstract.mixins import HasVehiclesList as HasVehiclesList, Deprecated as Deprecated

class HistoricalAchievement(Deprecated, HasVehiclesList, RegularAchievement):
    _LIST_NAME = 'vehiclesTakePart'
    def _getVehiclesDescrsList(self):
        ...
