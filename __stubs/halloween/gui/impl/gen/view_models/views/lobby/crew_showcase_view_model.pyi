# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/crew_showcase_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from halloween.gui.impl.gen.view_models.views.lobby.crew_member_view_model import CrewMemberViewModel as CrewMemberViewModel

class CrewShowcaseViewModel(ViewModel):
    __slots__: tuple
    onClose: Any
    onClaim: Any
    onShop: Any
    onPlaySound: Any
    def __init__(self, properties=3, commands=4):
        ...
    def getCrewMembers(self):
        ...
    def setCrewMembers(self, value):
        ...
    @staticmethod
    def getCrewMembersType():
        ...
    def getSkills(self):
        ...
    def setSkills(self, value):
        ...
    @staticmethod
    def getSkillsType():
        ...
    def getGroupVoiceover(self):
        ...
    def setGroupVoiceover(self, value):
        ...
    def _initialize(self):
        ...
