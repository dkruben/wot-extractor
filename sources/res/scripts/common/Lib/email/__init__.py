# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/email/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/email/__init__.py
__version__ = '4.0.3'
__all__ = [
 'base64MIME', 
 'Charset', 
 'Encoders', 
 'Errors', 
 'Generator', 
 'Header', 
 'Iterators', 
 'Message', 
 'MIMEAudio', 
 'MIMEBase', 
 'MIMEImage', 
 'MIMEMessage', 
 'MIMEMultipart', 
 'MIMENonMultipart', 
 'MIMEText', 
 'Parser', 
 'quopriMIME', 
 'Utils', 
 'message_from_string', 
 'message_from_file', 
 'base64mime', 
 'charset', 
 'encoders', 
 'errors', 
 'generator', 
 'header', 
 'iterators', 
 'message', 
 'mime', 
 'parser', 
 'quoprimime', 
 'utils']

def message_from_string(s, *args, **kws):
    from email.parser import Parser
    return Parser(*args, **kws).parsestr(s)


def message_from_file(fp, *args, **kws):
    from email.parser import Parser
    return Parser(*args, **kws).parse(fp)


import sys

class LazyImporter(object):

    def __init__(self, module_name):
        self.__name__ = 'email.' + module_name

    def __getattr__(self, name):
        __import__(self.__name__)
        mod = sys.modules[self.__name__]
        self.__dict__.update(mod.__dict__)
        return getattr(mod, name)


_LOWERNAMES = [
 'Charset', 
 'Encoders', 
 'Errors', 
 'FeedParser', 
 'Generator', 
 'Header', 
 'Iterators', 
 'Message', 
 'Parser', 
 'Utils', 
 'base64MIME', 
 'quopriMIME']
_MIMENAMES = [
 'Audio', 
 'Base', 
 'Image', 
 'Message', 
 'Multipart', 
 'NonMultipart', 
 'Text']
for _name in _LOWERNAMES:
    importer = LazyImporter(_name.lower())
    sys.modules['email.' + _name] = importer
    setattr(sys.modules['email'], _name, importer)

import email.mime
for _name in _MIMENAMES:
    importer = LazyImporter('mime.' + _name.lower())
    sys.modules['email.MIME' + _name] = importer
    setattr(sys.modules['email'], 'MIME' + _name, importer)
    setattr(sys.modules['email.mime'], _name, importer)
