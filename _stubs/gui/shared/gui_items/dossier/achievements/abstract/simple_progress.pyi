# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/dossier/achievements/abstract/simple_progress.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.shared.gui_items.dossier.achievements.abstract.regular import RegularAchievement as RegularAchievement
from dossiers2.custom.config import RECORD_CONFIGS as RECORD_CONFIGS

class SimpleProgressAchievement(RegularAchievement):
    __slots__: tuple
    _progressValue: Any
    def __init__(self, name, block, dossier, value=None):
        ...
    def getProgressValue(self):
        ...
    def isInNear(self):
        ...
    def hasProgress(self):
        ...
    def _readLevelUpValue(self, dossier):
        ...
    def _readLevelUpTotalValue(self, dossier):
        ...
    def _readProgressValue(self, dossier):
        ...
