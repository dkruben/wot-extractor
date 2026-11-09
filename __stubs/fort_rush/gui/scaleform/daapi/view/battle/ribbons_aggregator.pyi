# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/battle/ribbons_aggregator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from fort_rush.gui.fort_rush_gui_constants import FEEDBACK_EVENT_ID as FEI
from fort_rush.gui.scaleform.genConsts.FORT_RUSH_BATTLE_EFFICIENCY_TYPES import FORT_RUSH_BATTLE_EFFICIENCY_TYPES as FORT_RUSH_BATTLE_EFFICIENCY_TYPES
from fort_rush_common.battle_feedback import unpackPersonalScoreFeedback as unpackPersonalScoreFeedback
from fort_rush_common.fort_rush_constants import BATTLE_EVENT_TYPE as BATTLE_EVENT_TYPE
from gui.Scaleform.daapi.view.battle.shared.ribbons_aggregator import RibbonsAggregator as RibbonsAggregator, _BasePointsRibbon as _BasePointsRibbon, _RibbonSingleClassFactory as _RibbonSingleClassFactory
from gui.Scaleform.daapi.view.battle.shared.ribbons_panel import _baseRibbonFormatter as _baseRibbonFormatter
from gui.battle_control.controllers.feedback_events import _BATTLE_EVENT_TO_PLAYER_FEEDBACK_EVENT as _BATTLE_EVENT_TO_PLAYER_FEEDBACK_EVENT, _PLAYER_FEEDBACK_EXTRA_DATA_CONVERTERS as _PLAYER_FEEDBACK_EXTRA_DATA_CONVERTERS

class _FortRushBaseCaptureHealRibbon(_BasePointsRibbon):
    TYPE = FORT_RUSH_BATTLE_EFFICIENCY_TYPES.FORT_RUSH_BASE_CAPTURE_HEAL
    def getType(self):
        ...
    def getFormatter(self):
        ...

class _FortRushPersonalPointsRibbon(_BasePointsRibbon):
    def __init__(self, ribbonID, actionCtx):
        ...
    def getType(self):
        ...
    def getFormatter(self):
        ...

class _FortRushRibbonsAggregator(RibbonsAggregator):
    ...

def createRibbonsAggregator():
    ...
