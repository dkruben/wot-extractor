# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/wgnc/xml/actions_parsers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgnc/xml/actions_parsers.py
import typing, resource_helper
from gui.wgnc import actions
from gui.wgnc.errors import ParseError
from gui.wgnc.wgnc_helpers import parseSize
from gui.wgnc.xml.shared_parsers import ParsersCollection, SectionParser
if typing.TYPE_CHECKING:
    import ResMgr

class _CallbackActionParser(SectionParser):

    def getTagName(self):
        return 'callback'

    def parse(self, section):
        return actions.Callback(self._readString('name', section), section.readBool('purge', True))


class _BrowseActionParser(SectionParser):

    def getTagName(self):
        return 'browse'

    def parse(self, section):
        name = self._readString('name', section)
        url = self._readString('href', section)
        target = section.readString('target', 'internal')
        if target == 'internal':
            size = parseSize(section.readString('size'))
            showRefresh = section.readBool('show_refresh')
            webClientHandler = section.readString('web_client_handler') if section.has_key('web_client_handler') else None
            isSolidBorder = section.readBool('is_solid_border')
            return actions.OpenInternalBrowser(name, url, size, showRefresh, webClientHandler, isSolidBorder)
        else:
            if target == 'external':
                return actions.OpenExternalBrowser(name, url)
            if target == 'promo':
                return actions.OpenPromoBrowser(name, url)
            if target == 'stronghold':
                return actions.OpenStrongholdBrowser(name, url)
            if target == 'ranked':
                return actions.OpenRankedBrowser(name, url)
            msg = ('The target "{}" of action "{}" is not valid.').format(target, self.getTagName())
            raise ParseError(msg)
            return


class _OpenWindowParser(SectionParser):

    def getTagName(self):
        return 'openwindow'

    def parse(self, section):
        return actions.OpenWindow(self._readString('name', section), self._readString('target', section))


class _CustomActionsParser(SectionParser):

    def getTagName(self):
        return 'custom_action'

    def parse(self, section):
        ctx, _ = resource_helper.getRoot('')
        return actions.CustomAction(action_name=self._readString('name', section), **self.__parse(ctx, section))

    def __parse(self, ctx, section):
        res = {}
        for c, ss in resource_helper.getIterator(ctx, section):
            val = resource_helper.readItem(c, ss, ss.name).value
            res[self.__getKeyName(ss)] = val if val else self.__parse(c, ss)

        if not res:
            res[self.__getKeyName(section)] = resource_helper.readItem(ctx, section, section.name).value
        if 'action_class' not in res.keys():
            res['action_class'] = resource_helper.readItem(ctx, section, section.name).value
        return res

    def __getKeyName(self, section):
        if section['name'] is not None:
            return section['name'].asString
        else:
            return section.name


class _ReplaceButtonsAction(SectionParser):

    def getTagName(self):
        return 'replace_buttons'

    def parse(self, section):
        text = section.asString
        if not text:
            raise ParseError(('The content of action "{0}" is not defined.').format(self.getTagName()))
        return actions.ReplaceButtons(self._readString('name', section), section.asString)


class _ActionsParser(ParsersCollection):

    def getTagName(self):
        return 'actions'

    def parse(self, section):
        items = []
        for item in super(_ActionsParser, self).parse(section):
            items.append(item)

        return actions.ActionsHolder(items)


class ActionsParser_v2(_ActionsParser):

    def __init__(self):
        super(ActionsParser_v2, self).__init__((
         _CallbackActionParser(),
         _BrowseActionParser(),
         _OpenWindowParser(),
         _ReplaceButtonsAction(),
         _CustomActionsParser()))
