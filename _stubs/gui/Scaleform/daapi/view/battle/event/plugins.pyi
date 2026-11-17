# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/event/plugins.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.daapi.view.battle.shared.markers2d.vehicle_plugins import RespawnableVehicleMarkerPlugin as RespawnableVehicleMarkerPlugin
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as _EVENT_ID

class EventVehicleMarkerPlugin(RespawnableVehicleMarkerPlugin):
    def init(self, *args):
        ...
    def fini(self):
        ...
    def __onVehicleFeedbackReceived(self, eventID, vehicleID, value):
        ...
    def __showActionMassage(self, handle, massage, isAlly):
        ...
