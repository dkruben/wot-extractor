# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/frag_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.daapi.view.meta.FragPanelMeta import FragPanelMeta as FragPanelMeta
from battle_royale.gui.battle_control.controllers.vehicles_count_ctrl import IVehicleCountListener as IVehicleCountListener
from gui.battle_control.avatar_getter import getArena as getArena
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from gui.impl import backport as backport
from gui.impl.gen import R as R

class FragPanel(IVehicleCountListener, FragPanelMeta):
    __slots__: tuple
    __ADDITIONAL_FRAG_TEMPLATE = '<font color="#333333">[&nbsp;<font color="#999999">{}</font>&nbsp;]</font>'
    def setFrags(self, frags, isPlayerVehicle):
        ...
    def setTotalCount(self, vehicles, teams):
        ...
