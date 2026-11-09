# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/attack_artillery_fort_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from EntitySync import EntityGOSync as EntityGOSync
from cgf_components.color_components import ColorComponent as ColorComponent
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from constants import IS_CGF_DUMP as IS_CGF_DUMP, IS_CLIENT as IS_CLIENT
from helpers import dependency as dependency
from helpers.gui_utils import hexARGBToRGBAFloatColor as hexARGBToRGBAFloatColor
from account_helpers.settings_core.settings_constants import GRAPHICS as GRAPHICS

class ISettingsCore(object):
    ...

# decorador original: @registerComponent
class ArtilleryFortColorComponent(object):
    group = 'Abilities'
    editorTitle = 'Artillery Fort Color'
    domain = CGF.Domain.ClientEditor
    colorComponent: Any
    entityGO: Any
    def __init__(self):
        ...

class AttackArtilleryFortColorSystem(CGF.System):
    __settingsCore: Any
    FortColorActivated: Any
    FortColorDeactivated: Any
    FortColorIterate: Any
    EntitySyncAccess: Any
    ColorAccess: Any
    Reactions: Any
    def onMappingLoaded(self):
        ...
    def onMappingUnloaded(self):
        ...
    def update(self):
        ...
    def handleColorComponentAdded(self, gameObject, fortColor, entitySyncAccess, colorAccess):
        ...
    def colorSettingsChanged(self, diff):
        ...
    def changeColor(self, fortColor, entitySyncAccess, colorAccess):
        ...
