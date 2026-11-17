# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/lobby/header/helpers/controls_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin
from fun_random.gui.Scaleform.daapi.view.lobby.header.helpers.fight_btn_tooltips import getFunRandomFightBtnTooltipData as getFunRandomFightBtnTooltipData
from gui.impl.gen import R as R
from gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import DefaultLobbyHeaderHelper as DefaultLobbyHeaderHelper

class FunRandomLobbyHeaderHelper(DefaultLobbyHeaderHelper, FunAssetPacksMixin):
    __slots__: tuple
    @classmethod
    def _getDisabledFightTooltipData(cls, prbValidation, isInSquad):
        ...
    @classmethod
    def _getOutSquadTooltipData(cls, _):
        ...
