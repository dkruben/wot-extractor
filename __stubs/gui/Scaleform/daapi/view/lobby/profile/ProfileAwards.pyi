# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileAwards.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.meta.ProfileAwardsMeta import ProfileAwardsMeta as ProfileAwardsMeta
from gui.Scaleform.locale.PROFILE import PROFILE as PROFILE
from web_stubs import i18n as i18n
from gui.Scaleform.daapi.view.AchievementsUtils import AchievementsUtils as AchievementsUtils
from gui.shared.utils.RareAchievementsCache import IMAGE_TYPE as IMAGE_TYPE
from gui.shared.gui_items.dossier import dumpDossier as dumpDossier

class ProfileAwards(ProfileAwardsMeta):
    __achievementsFilter: Any
    def __init__(self, *args):
        ...
    def setFilter(self, data):
        ...
    @classmethod
    def _getTotalStatsBlock(cls, dossier):
        ...
    def _sendAccountData(self, targetData, accountDossier):
        ...
    def _populate(self):
        ...
    def _onRareImageReceived(self, imgType, rareID, imageData):
        ...
    def _dispose(self):
        ...
    @staticmethod
    def __packProviderItem(key):
        ...
