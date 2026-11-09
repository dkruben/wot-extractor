# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/tutorial/gui/impl/gui_impl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import logging as logging
from collections import defaultdict as defaultdict
from Event import Event as Event, EventManager as EventManager
from gui.Scaleform.genConsts.TUTORIAL_EFFECT_TYPES import TUTORIAL_EFFECT_TYPES as TUTORIAL_EFFECT_TYPES
from gui.Scaleform.genConsts.TUTORIAL_TRIGGER_TYPES import TUTORIAL_TRIGGER_TYPES as TUTORIAL_TRIGGER_TYPES
from gui.impl.gen.view_models.common.tutorial.component_description_model import ComponentDescriptionModel as ComponentDescriptionModel
from gui.impl.gen.view_models.common.tutorial.criterion_model import CriterionModel as CriterionModel
from gui.impl.gen.view_models.common.tutorial.triggers_model import TriggersModel as TriggersModel
from gui.impl.gen.view_models.common.tutorial.view_criterion_model import ViewCriterionModel as ViewCriterionModel
from gui.impl.gen.view_models.common.tutorial.view_description_model import ViewDescriptionModel as ViewDescriptionModel
from gui.impl.gen.view_models.common.tutorial.tutorial_model import TutorialModel as TutorialModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.utils.data import findIndexes as findIndexes, findItems as findItems
from helpers import dependency as dependency
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from tutorial.gui import GuiType as GuiType, IGuiImpl as IGuiImpl
from soft_exception import SoftException as SoftException
from tutorial.gui.impl import effects as effects_impl
from gui.impl.gen.view_models.ui_kit.list_model import ListModel as ListModel
from gui.impl.gen.view_models.common.tutorial.descriptions_model import DescriptionsModel as DescriptionsModel
from gui.impl.gen.view_models.common.tutorial.effect_model import EffectModel as EffectModel
from skeletons.tutorial import ComponentID as ComponentID
from tutorial.gui import ComponentDescr as ComponentDescr
_logger: Any

class WulfGuiImpl(IGuiImpl):
    _SUPPORTED_TRIGGERS: Any
    _FORCE_PROXIED_TRIGGERS: Any
    _PROXIED_TRIGGERS: Any
    _SUPPORTED_EFFECTS: Any
    __effectsFactory: Any
    __proxy: Any
    __model: Any
    __eventMgr: Any
    onComponentFound: Any
    onComponentDisposed: Any
    onTriggerActivated: Any
    onEffectCompleted: Any
    onInit: Any
    def __init__(self, proxy):
        ...
    def showEffect(self, componentID, viewID, effectType, effectData, effectBuilder=''):
        ...
    def hideEffect(self, componentID, viewID, effectType, effectBuilder=''):
        ...
    def setDescriptions(self, descriptions):
        ...
    def setSystemEnabled(self, enabled):
        ...
    def setCriteria(self, name, value):
        ...
    def setViewCriteria(self, componentID, viewUniqueName):
        ...
    def setTriggers(self, componentID, triggers):
        ...
    def supportedViewTypes(self):
        ...
    def isInited(self):
        ...
    def fini(self):
        ...
    def clear(self):
        ...
    def __onComponentFound(self, args):
        ...
    def __onComponentDisposed(self, args):
        ...
    # decorador original: @args2params(...)
    def __onEffectCompleted(self, componentId, viewId, effectType, effectBuilder):
        ...
    # decorador original: @args2params(...)
    def __onTriggerActivated(self, componentId, triggerType, state):
        ...
