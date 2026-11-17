# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/cgf/cgf_module.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import CGF as CGF
from CapturePointComponent import CapturePointMarkerAnchor as CapturePointMarkerAnchor
from cgf_script.registration import registerModule as registerModule, bonusCapsPredicate as bonusCapsPredicate
from fort_rush.cgf.capture_point import CapturePointMarkerAnchorGizmoSystem as CapturePointMarkerAnchorGizmoSystem, CapturePointSystem as CapturePointSystem
from fort_rush.cgf.damage_resistance import FortRushDamageResistanceSystem as FortRushDamageResistanceSystem
from fort_rush_common.fort_rush_constants import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from VehicleExpirableComponent import VehicleExpirableComponent as VehicleExpirableComponent

# decorador original: @registerModule
class FortRushClientModule(object):
    name = 'Fort Rush Client Module'
    desc = 'Fort Rush systems that works on client'
    group = 'Fort Rush'
    systems: list
    components: list
