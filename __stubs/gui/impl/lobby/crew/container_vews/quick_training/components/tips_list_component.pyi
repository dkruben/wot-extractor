# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/quick_training/components/tips_list_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
import SoundGroups as SoundGroups
from gui.impl.gen.view_models.views.lobby.crew.common.info_tip_model import TipType as TipType
from gui.impl.lobby.container_views.base.components import ComponentBase as ComponentBase
from gui.impl.lobby.crew.crew_sounds import SOUNDS as SOUNDS
from gui.impl.lobby.crew.utils import TRAINING_TIPS as TRAINING_TIPS, getTip as getTip
from gui.impl.gen.view_models.views.lobby.crew.quick_training.quick_training_view_model import QuickTrainingViewModel as QuickTrainingViewModel
from gui.impl.gen.view_models.views.lobby.crew.quick_training.tips_list_component_model import TipsListComponentModel as TipsListComponentModel

class TipsListComponent(ComponentBase):
    def _getViewModel(self, vm):
        ...
    def _fillViewModel(self, vm):
        ...
    def __fillErrorTips(self, tips, playSound):
        ...
