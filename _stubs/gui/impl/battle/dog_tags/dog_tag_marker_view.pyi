# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/battle/dog_tags/dog_tag_marker_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.battle.dog_tags.dog_tag_marker_view_model import DogTagMarkerViewModel as DogTagMarkerViewModel
from gui.battle_control.dog_tag_composer import DogTagComposerInBattleGF as DogTagComposerInBattleGF
from dog_tags_common.player_dog_tag import DisplayableDogTag as DisplayableDogTag, PlayerDogTag as PlayerDogTag
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from helpers import dependency as dependency

class DogTagMarkerView(ViewImpl):
    __sessionProvider: Any
    __composer: Any
    __vehicleID: Any
    def __init__(self, viewKey):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self):
        ...
    def __update(self):
        ...
