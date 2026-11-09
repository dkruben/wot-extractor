# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/postmortem_info_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.battle.postmortem_panel.postmortem_panel_view import PostmortemPanelView as PostmortemPanelView
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor as InjectComponentAdaptor
from gui.shared.system_factory import collectPostmortemInfoView as collectPostmortemInfoView
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class PostmortemInfoPanel(InjectComponentAdaptor):
    __sessionProvider: Any
    __view: Any
    def _makeInjectView(self, *args):
        ...
