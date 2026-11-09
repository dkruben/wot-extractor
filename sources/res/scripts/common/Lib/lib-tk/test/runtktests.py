# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/lib-tk/test/runtktests.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib-tk/test/runtktests.py
import os, sys, unittest, importlib, test.test_support
this_dir_path = os.path.abspath(os.path.dirname(__file__))

def is_package(path):
    for name in os.listdir(path):
        if name in ('__init__.py', '__init__.pyc', '__init.pyo'):
            return True

    return False


def get_tests_modules(basepath=this_dir_path, gui=True, packages=None):
    py_ext = '.py'
    for dirpath, dirnames, filenames in os.walk(basepath):
        for dirname in list(dirnames):
            if dirname[0] == '.':
                dirnames.remove(dirname)

        if is_package(dirpath) and filenames:
            pkg_name = dirpath[len(basepath) + len(os.sep):].replace('/', '.')
            if packages and pkg_name not in packages:
                continue
            filenames = filter((lambda x: x.startswith('test_') and x.endswith(py_ext)), filenames)
            for name in filenames:
                try:
                    yield importlib.import_module('.%s' % name[:-len(py_ext)], pkg_name)
                except test.test_support.ResourceDenied:
                    if gui:
                        raise


def get_tests(text=True, gui=True, packages=None):
    attrs = []
    if text:
        attrs.append('tests_nogui')
    if gui:
        attrs.append('tests_gui')
    for module in get_tests_modules(gui=gui, packages=packages):
        for attr in attrs:
            for test in getattr(module, attr, ()):
                yield test


if __name__ == '__main__':
    test.test_support.run_unittest(*get_tests())
