# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/points_of_interest/registrars.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import CGF as CGF
from cgf_script.registration import registerModule as registerModule
from points_of_interest.managers import PoiStateCreateSystem as PoiStateCreateSystem, PoiStateUpdateSystem as PoiStateUpdateSystem, PoiViewStateSystem as PoiViewStateSystem, PoiSoundSystem as PoiSoundSystem
_UPDATE_PERIOD = 0.2

# decorador original: @registerModule
class PointsOfInterestModule(object):
    name = 'POI Module'
    desc = 'Stuff for points of interest'
    group = 'Battle'
    systems: list
    components: list
