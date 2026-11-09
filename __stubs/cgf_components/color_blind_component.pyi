# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/color_blind_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import CGF as CGF
import GenericComponents as GenericComponents
from account_helpers.settings_core.settings_constants import GRAPHICS as GRAPHICS
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore

# decorador original: @registerComponent
class ChangeModelOnColorBlindComponent(object):
    group = 'Render'
    editorTitle = 'Change Model When Color Blind      [DEPRECATED]'
    domain = CGF.Domain.Client
    colorBlindModelPath: Any
    normalModel: Any
    def __init__(self):
        ...

class ChangeModelOnColorBlindComponentSystem(CGF.System):
    _settingsCore: Any
    ChangeModelActivated: Any
    ChangeModelDeactivated: Any
    ModelAccess: Any
    ChangeModelAccess: Any
    Reactions: Any
    _gameObjects: Any
    def __init__(self, *args):
        ...
    def update(self):
        ...
    def onAdded(self, gameObject, component, modelAccess):
        ...
    def onRemoved(self, gameObject):
        ...
    def _clientColorSettingsChanged(self, diff):
        ...

def setModel(gameObject, isColorBlind, queue, dynamicModelPath, colorBlindComponent=None):
    ...
