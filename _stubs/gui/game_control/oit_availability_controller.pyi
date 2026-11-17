# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/oit_availability_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import BigWorld as BigWorld
from PlayerEvents import g_playerEvents as g_playerEvents
from config_schemas.oit_availability import oitAvailabilitySchema as oitAvailabilitySchema
from skeletons.gui.game_control import IOitAvailabilityController as IOitAvailabilityController

class OitAvailabilityController(IOitAvailabilityController):
    def init(self):
        ...
    def fini(self):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def isOitEnabledForPreset(self, qualityLevel):
        ...
    def _onConfigModelUpdated(self, gpKey):
        ...
    def _pushToEngine(self):
        ...
