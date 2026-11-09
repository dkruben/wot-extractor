# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_systems/components/shot_damage_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
import Math as Math
import BigWorld as BigWorld
from items import vehicles as vehicles
from vehicle_systems.tankStructure import TankPartNames as TankPartNames
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent

class ShotDamageComponent(object):
    partName: Any
    compound: Any
    def __init__(self, partName, compound):
        ...

# decorador original: @registerComponent
class DamageStickerComponent(object):
    category = 'Render'
    editorTitle = 'Damage Sticker Component'
    domain = CGF.Domain.Client
    damageSticker: Any
    lodDistance: Any
    fadeoutTime: Any
    offset: Any
    stickerModel: Any
    def __init__(self):
        ...

class DamageStickerSystem(CGF.System):
    StickerActivated: Any
    StickerDeaactivated: Any
    Reactions: Any
    def update(self):
        ...
