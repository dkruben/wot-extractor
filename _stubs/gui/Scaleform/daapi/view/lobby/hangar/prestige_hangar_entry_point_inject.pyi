# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/prestige_hangar_entry_point_inject.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor as InjectComponentAdaptor
from gui.impl.lobby.prestige.prestige_hangar_entry_point_view import PrestigeHangarEntryPointView as PrestigeHangarEntryPointView
from gui.Scaleform.daapi.view.meta.PrestigeProgressInjectMeta import PrestigeProgressInjectMeta as PrestigeProgressInjectMeta
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from shared_utils import nextTick as nextTick

class PrestigeHangarEntryPointInject(InjectComponentAdaptor, PrestigeProgressInjectMeta, IGlobalListener):
    # decorador original: @nextTick
    def _createInjectView(self, *args):
        ...
    def _makeInjectView(self):
        ...
