# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/gui_items/dossier/achievements/abstract/regular_ext.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/abstract/regular_ext.py
from __future__ import absolute_import
from gui.shared.formatters import text_styles
from gui.shared.gui_items.dossier.achievements.abstract.regular import RegularAchievement
from helpers import i18n

class RegularExtAchievement(RegularAchievement):
    __slots__ = ()
    USER_DESCR_TEMPLATE = '%(title)s\n<font size="3">&nbsp;</font>\n%(standard)s\n%(ext)s'
    USER_DESCR_WEB_TEMPLATE = '%(title)s\n%(standard)s\n%(ext)s'

    def getUserDescription(self):
        return RegularExtAchievement.USER_DESCR_TEMPLATE % {'title': (text_styles.main(self._getTranslatedText('#achievements:%s_descr'))), 
           'standard': (text_styles.main(self._getStandardDescription())), 
           'ext': (text_styles.main(self._getExtDescription()))}

    def getUserWebDescription(self):
        return RegularExtAchievement.USER_DESCR_WEB_TEMPLATE % {'title': (i18n.makeString('#achievements:%s_descr' % self._getActualName())), 
           'standard': (i18n.makeString('#achievements:%s_standard_descr' % self._getActualName(), condition=str(self._getStandardValues()) + self._getConditionText())), 
           'ext': (i18n.makeString('#achievements:%s_ext_descr' % self._getActualName(), condition=str(self._getExtValues()) + self._getConditionText()))}

    def _getTranslatedText(self, translationRef):
        return text_styles.main(i18n.makeString(translationRef % self._getActualName()))

    def _getExtDescription(self):
        return self._getTranslatedText('#achievements:%s_ext_descr') % {'condition': (text_styles.creditsSmall(str(self._getExtValues()) + self._getConditionText()))}

    def _getStandardDescription(self):
        return self._getTranslatedText('#achievements:%s_standard_descr') % {'condition': (text_styles.creditsSmall(str(self._getStandardValues()) + self._getConditionText()))}

    def _getStandardValues(self):
        pass

    def _getExtValues(self):
        pass

    def _getConditionText(self):
        condTextKey = '#achievements:%s_condition_text' % self._getActualName()
        if i18n.doesTextExist(condTextKey):
            return i18n.makeString(condTextKey)
        return ''
