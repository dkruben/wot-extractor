# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/personal_file/context.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.impl.lobby.crew.container_vews.common.base_personal_case_context import BasePersonalCaseContext as BasePersonalCaseContext
from gui.impl.lobby.crew.crew_helpers.skill_helpers import getTmanNewSkillCount as getTmanNewSkillCount
from gui.shared.gui_items.Tankman import SKILL_EFFICIENCY_UNTRAINED as SKILL_EFFICIENCY_UNTRAINED
from typing import Tuple as Tuple

class PersonalFileViewContext(BasePersonalCaseContext):
    __slots__: tuple
    _availableSkillsCount: Any
    _lastSkillLevel: Any
    _skillAnimationsSkipped: Any
    def __init__(self, tankmanID):
        ...
    @property
    def availableSkillsCount(self):
        ...
    @property
    def lastSkillLevel(self):
        ...
    @property
    def skillAnimationsSkipped(self):
        ...
    @property
    def hasIncreaseDiscount(self):
        ...
    @property
    def hasDropSkillDiscount(self):
        ...
    @property
    def resetDisabled(self):
        ...
    def update(self, tankmanID=None, skillAnimationsSkipped=False):
        ...
    def getInstalledBooster(self):
        ...
    def _calcSkillsCountAndLevel(self):
        ...
