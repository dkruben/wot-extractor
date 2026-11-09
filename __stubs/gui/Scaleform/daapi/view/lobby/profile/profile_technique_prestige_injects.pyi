# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/profile/profile_technique_prestige_injects.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor as InjectComponentAdaptor
from gui.impl.lobby.prestige.prestige_profile_technique_views import PrestigeProfileTechniqueView as PrestigeProfileTechniqueView, PrestigeProfileTechniqueEmblemView as PrestigeProfileTechniqueEmblemView
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener

class CommonPrestigeInject(InjectComponentAdaptor, IGlobalListener):
    def setDatabaseID(self, value):
        ...
    def setSelectedVehicleIntCD(self, value):
        ...
    def _makeInjectView(self):
        ...

class ProfileTechniquePrestigeInject(CommonPrestigeInject):
    def _makeInjectView(self):
        ...

class ProfileTechniquePrestigeEmblemInject(CommonPrestigeInject):
    def _makeInjectView(self):
        ...
