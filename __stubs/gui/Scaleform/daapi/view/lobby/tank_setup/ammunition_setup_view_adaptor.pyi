# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/tank_setup/ammunition_setup_view_adaptor.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor as InjectComponentAdaptor
from gui.impl.lobby.tank_setup.ammunition_setup.hangar import HangarAmmunitionSetupView as HangarAmmunitionSetupView
from gui.shared.system_factory import collectAmmunitionSetupView as collectAmmunitionSetupView
from helpers import dependency as dependency
from skeletons.gui.game_control import IHangarGuiController as IHangarGuiController

class AmmunitionSetupViewAdaptor(InjectComponentAdaptor):
    __hangarGuiCtrl: Any
    __ctx: Any
    def __init__(self, ctx):
        ...
    def _makeInjectView(self):
        ...
