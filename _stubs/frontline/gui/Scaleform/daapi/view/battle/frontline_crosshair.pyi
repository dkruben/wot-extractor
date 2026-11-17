# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_crosshair.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.daapi.view.battle.shared.crosshair import CrosshairPanelContainer as CrosshairPanelContainer
from gui.Scaleform.daapi.view.battle.shared.crosshair.plugins import AimDamagePlugin as AimDamagePlugin

class FrontlineAimDamagePlugin(AimDamagePlugin):
    def start(self):
        ...
    def stop(self):
        ...
    def __onDestructibleEntityFeedbackReceived(self, eventID, _, value):
        ...

class FrontlineCrosshairPanelContainer(CrosshairPanelContainer):
    def _getPlugins(self):
        ...
