# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/messages/player_messages.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.daapi.view.battle.shared.messages import player_messages as player_messages
from items import vehicles as vehicles

class LSPlayerMessages(player_messages.PlayerMessages):
    _SKIP_MESSAGES: tuple
    def showMessage(self, key, args=None, extra=None, postfix=''):
        ...
    def _onCombatEquipmentUsed(self, shooterID, eqID):
        ...
    def __replaceVehicleName(self, argName, vehId, args):
        ...
    @staticmethod
    def _getPostfixFromEquipment(equipment):
        ...
