# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/visual_script_client/contexts/sound_notifications_context.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import BigWorld as BigWorld
from visual_script.misc import ASPECT as ASPECT
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE, arrayOf as arrayOf
from visual_script.context import VScriptContext as VScriptContext, vse_event_out as vse_event_out, vse_func_call as vse_func_call

class SoundNotificationsContext(VScriptContext):
    __soundNotifications: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def getSoundNotifications(self):
        ...
    # decorador original: @vse_event_out(...)
    def onPlayQueueEvent(self, eventName):
        ...
    # decorador original: @vse_event_out(...)
    def onAddQueueEvent(self, eventName):
        ...
    # decorador original: @vse_func_call(...)
    def playNextQueueEvent(self, queueNum):
        ...
    # decorador original: @vse_func_call(...)
    def replayLastQueueEvent(self, queueNum):
        ...
    # decorador original: @vse_func_call(...)
    def getFirstQueueEvent(self, queueNum):
        ...
    # decorador original: @vse_func_call(...)
    def clearQueue(self, queueNum):
        ...
    # decorador original: @vse_func_call(...)
    def getEventInfoBool(self, eventName, parameter):
        ...
    # decorador original: @vse_func_call(...)
    def getEventInfoInt(self, eventName, parameter):
        ...
    # decorador original: @vse_func_call(...)
    def getEventInfoFloat(self, eventName, parameter):
        ...
    # decorador original: @vse_func_call(...)
    def getEventInfoString(self, eventName, parameter):
        ...
    # decorador original: @vse_func_call(...)
    def getEventInfoStringArray(self, eventName, parameter):
        ...
    # decorador original: @vse_func_call(...)
    def getCircumstanceInfoBool(self, circIndex, parameter):
        ...
    # decorador original: @vse_func_call(...)
    def getCircumstanceInfoInt(self, circIndex, parameter):
        ...
    # decorador original: @vse_func_call(...)
    def getCircumstanceInfoString(self, circIndex, parameter):
        ...
    # decorador original: @vse_func_call(...)
    def getPlayingEventName(self, queueNum):
        ...
    # decorador original: @vse_func_call(...)
    def getPlayingEventVehicle(self, queueNum):
        ...
    # decorador original: @vse_func_call(...)
    def getPlayingEventBoundVehicle(self, queueNum):
        ...
    # decorador original: @vse_func_call(...)
    def getPlayingEventPosition(self, queueNum):
        ...
    # decorador original: @vse_func_call(...)
    def getPlayingEventIs2D(self, queueNum):
        ...
    # decorador original: @vse_func_call(...)
    def getCircumstanceIndex(self, circGroup, circName):
        ...
    # decorador original: @vse_func_call(...)
    def setEventCooldown(self, eventName, cooldown):
        ...
    # decorador original: @vse_func_call(...)
    def setEventPriority(self, eventName, priority, hold):
        ...
    # decorador original: @vse_func_call(...)
    def setCircumstanceWeight(self, circIndex, weight, hold):
        ...
    # decorador original: @vse_func_call(...)
    def setCircumstanceGroupWeight(self, groupName, weight, hold):
        ...
    # decorador original: @vse_func_call(...)
    def onNotificationBegins(self, eventName):
        ...
    # decorador original: @vse_func_call(...)
    def log(self, msg):
        ...
