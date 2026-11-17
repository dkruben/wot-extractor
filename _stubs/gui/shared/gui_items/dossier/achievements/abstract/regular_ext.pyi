# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/dossier/achievements/abstract/regular_ext.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items.dossier.achievements.abstract.regular import RegularAchievement as RegularAchievement
from helpers import i18n as i18n

class RegularExtAchievement(RegularAchievement):
    __slots__: tuple
    USER_DESCR_TEMPLATE = '%(title)s\n<font size="3">&nbsp;</font>\n%(standard)s\n%(ext)s'
    USER_DESCR_WEB_TEMPLATE = '%(title)s\n%(standard)s\n%(ext)s'
    def getUserDescription(self):
        ...
    def getUserWebDescription(self):
        ...
    def _getTranslatedText(self, translationRef):
        ...
    def _getExtDescription(self):
        ...
    def _getStandardDescription(self):
        ...
    def _getStandardValues(self):
        ...
    def _getExtValues(self):
        ...
    def _getConditionText(self):
        ...
