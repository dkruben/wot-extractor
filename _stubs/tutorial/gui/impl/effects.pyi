# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/tutorial/gui/impl/effects.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import logging as logging
from gui.Scaleform.genConsts.TUTORIAL_EFFECT_TYPES import TUTORIAL_EFFECT_TYPES as TUTORIAL_EFFECT_TYPES
from gui.impl.gen.view_models.common.tutorial.visible_effect_model import VisibleEffectModel as VisibleEffectModel
from gui.impl.gen.view_models.common.tutorial.enabled_effect_model import EnabledEffectModel as EnabledEffectModel
from gui.impl.gen.view_models.common.tutorial.effect_model import EffectModel as EffectModel
_logger: Any

class IEffectsFactory(object):
    def createEffect(self, effectType):
        ...
    def updateEffect(self, effect, effectData):
        ...

class Factory(IEffectsFactory):
    __slots__: tuple
    __effectsMap: Any
    __updatersMap: Any
    def __init__(self):
        ...
    def createEffect(self, effectType):
        ...
    def updateEffect(self, effect, effectData):
        ...
    @staticmethod
    def __updateVisibleEffect(effect, effectData):
        ...
    @staticmethod
    def __updateEnabledEffect(effect, effectData):
        ...

def getFactory():
    ...
