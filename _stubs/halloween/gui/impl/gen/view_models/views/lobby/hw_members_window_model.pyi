# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/hw_members_window_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from halloween.gui.impl.gen.view_models.views.lobby.event_difficulty_model import EventDifficultyModel as EventDifficultyModel
from gui.impl.gen.view_models.views.lobby.platoon.members_window_model import MembersWindowModel as MembersWindowModel

class PrebattleTypes(Enum):
    HALLOWEEN = 'halloween'

class HwMembersWindowModel(MembersWindowModel):
    __slots__: tuple
    def __init__(self, properties=20, commands=3):
        ...
    @property
    def eventDifficulty(self):
        ...
    @staticmethod
    def getEventDifficultyType():
        ...
    def getSelectedDifficulty(self):
        ...
    def setSelectedDifficulty(self, value):
        ...
    def getSelectionDisabled(self):
        ...
    def setSelectionDisabled(self, value):
        ...
    def _initialize(self):
        ...
