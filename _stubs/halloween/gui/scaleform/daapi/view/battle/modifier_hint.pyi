# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/modifier_hint.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl import backport as backport
from halloween.gui.scaleform.daapi.view.battle.battle_hint import BattleHint as BattleHint
from halloween.gui.scaleform.daapi.view.meta.BattleHintModifierMeta import BattleHintModifierMeta as BattleHintModifierMeta
from gui.impl.gen import R as R
from halloween.gui.sounds import playSound as playSound
from halloween.gui.sounds.sound_constants import PhaseModifierSounds as PhaseModifierSounds

class HWPhaseModifierHint(BattleHint, BattleHintModifierMeta):
    ICONS_PATH = R.images.halloween.gui.maps.icons.battleHints
    BATTLE_HINT = R.strings.halloween_battle.battleHint
    def _showHint(self, model, params):
        ...
