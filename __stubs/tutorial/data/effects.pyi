# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/tutorial/data/effects.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from tutorial.data.has_id import HasTargetID as HasTargetID
EFFECT_TYPE_NAMES: dict

class EFFECT_TYPE(object):
    EFFECTS_GROUP: Any
    ACTIVATE: Any
    DEACTIVATE: Any
    GLOBAL_ACTIVATE: Any
    GLOBAL_DEACTIVATE: Any
    SHOW_HINT: Any
    CLOSE_HINT: Any
    SHOW_DIALOG: Any
    SHOW_WINDOW: Any
    REFUSE_TRAINING: Any
    RUN_TRIGGER: Any
    SET_ITEM_PROPS: Any
    FINISH_TRAINING: Any
    INVOKE_GUI_CMD: Any
    SET_GUI_ITEM_CRITERIA: Any
    SET_GUI_ITEM_VIEW_CRITERIA: Any
    SET_ACTION: Any
    REMOVE_ACTION: Any
    SET_VAR: Any
    CLEAR_SCENE: Any
    GO_SCENE: Any
    SELECT_VEHICLE_IN_HANGAR: Any
    LOAD_VIEW: Any
    CLOSE_VIEW: Any
    PLAY_ANIMATION: Any
    SET_ALLOWED_TO_FIGHT: Any
    PLAY_SOUND: Any

class HasTargetEffect(HasTargetID):
    __type: Any
    __conditions: Any
    def __init__(self, targetID, effectType, conditions=None):
        ...
    def __repr__(self):
        ...
    def getType(self):
        ...
    def getConditions(self):
        ...
    def clear(self):
        ...

class SimpleEffect(HasTargetEffect):
    def __init__(self, effectType, conditions=None, **kwargs):
        ...
    def __repr__(self):
        ...

class InvokeGuiCommand(HasTargetEffect):
    __argOverrides: Any
    def __init__(self, targetID, argOverrides, conditions=None):
        ...
    def getArgOverrides(self):
        ...

class EffectsGroup(SimpleEffect):
    __effects: Any
    def __init__(self, effects, conditions=None):
        ...
    def getEffects(self):
        ...

class SetGuiItemProperties(HasTargetEffect):
    __props: Any
    def __init__(self, targetID, props, conditions=None):
        ...
    def getProps(self):
        ...
    def clear(self):
        ...

class PlayAnimationEffect(HasTargetEffect):
    __animType: Any
    __waitForFinish: Any
    def __init__(self, targetID, animType, waitForFinish, conditions=None):
        ...
    def getAnimType(self):
        ...
    def needWaitForFinish(self):
        ...

class SetAllowedToFightEffect(SimpleEffect):
    __value: Any
    def __init__(self, value, conditions=None):
        ...
    def getValue(self):
        ...

class PlaySoundEffect(HasTargetEffect):
    __soundEvent: Any
    def __init__(self, soundID, soundEvent, conditions=None):
        ...
    def getSoundEvent(self):
        ...
