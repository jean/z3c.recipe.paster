##############################################################################
#
# Copyright (c) 2008 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Tests

$Id:$
"""

import re
import unittest
from zope.testing import doctest
from zope.testing import renormalizing

import zc.buildout.testing


def setUp(test):
    zc.buildout.testing.buildoutSetUp(test)
    zc.buildout.testing.install_develop('z3c.recipe.paster', test)
    zc.buildout.testing.install('Paste', test)
    zc.buildout.testing.install('PasteDeploy', test)
    zc.buildout.testing.install('PasteScript', test)
    zc.buildout.testing.install('RestrictedPython', test)
    zc.buildout.testing.install('ZConfig', test)
    zc.buildout.testing.install('ZODB3', test)
    zc.buildout.testing.install('pytz', test)
    zc.buildout.testing.install('zc.recipe.egg', test)
    zc.buildout.testing.install('zc.recipe.filestorage', test)
    zc.buildout.testing.install('zdaemon', test)
    zc.buildout.testing.install('zodbcode', test)
    zc.buildout.testing.install('zope.annotation', test)
    zc.buildout.testing.install('zope.app.applicationcontrol', test)
    zc.buildout.testing.install('zope.app.appsetup', test)
    zc.buildout.testing.install('zope.app.authentication', test)
    zc.buildout.testing.install('zope.app.basicskin', test)
    zc.buildout.testing.install('zope.app.broken', test)
    zc.buildout.testing.install('zope.app.component', test)
    zc.buildout.testing.install('zope.app.container', test)
    zc.buildout.testing.install('zope.app.content', test)
    zc.buildout.testing.install('zope.app.debug', test)
    zc.buildout.testing.install('zope.app.dependable', test)
    zc.buildout.testing.install('zope.app.error', test)
    zc.buildout.testing.install('zope.app.exception', test)
    zc.buildout.testing.install('zope.app.folder', test)
    zc.buildout.testing.install('zope.app.form', test)
    zc.buildout.testing.install('zope.app.generations', test)
    zc.buildout.testing.install('zope.app.http', test)
    zc.buildout.testing.install('zope.app.i18n', test)
    zc.buildout.testing.install('zope.app.interface', test)
    zc.buildout.testing.install('zope.app.locales', test)
    zc.buildout.testing.install('zope.app.pagetemplate', test)
    zc.buildout.testing.install('zope.app.principalannotation', test)
    zc.buildout.testing.install('zope.app.publication', test)
    zc.buildout.testing.install('zope.app.publisher', test)
    zc.buildout.testing.install('zope.app.renderer', test)
    zc.buildout.testing.install('zope.app.rotterdam', test)
    zc.buildout.testing.install('zope.app.schema', test)
    zc.buildout.testing.install('zope.app.security', test)
    zc.buildout.testing.install('zope.app.session', test)
    zc.buildout.testing.install('zope.app.testing', test)
    zc.buildout.testing.install('zope.app.wsgi', test)
    zc.buildout.testing.install('zope.app.zapi', test)
    zc.buildout.testing.install('zope.app.zcmlfiles', test)
    zc.buildout.testing.install('zope.app.zopeappgenerations', test)
    zc.buildout.testing.install('zope.cachedescriptors', test)
    zc.buildout.testing.install('zope.component', test)
    zc.buildout.testing.install('zope.configuration', test)
    zc.buildout.testing.install('zope.contenttype', test)
    zc.buildout.testing.install('zope.copypastemove', test)
    zc.buildout.testing.install('zope.datetime', test)
    zc.buildout.testing.install('zope.deferredimport', test)
    zc.buildout.testing.install('zope.deprecation', test)
    zc.buildout.testing.install('zope.dottedname', test)
    zc.buildout.testing.install('zope.dublincore', test)
    zc.buildout.testing.install('zope.error', test)
    zc.buildout.testing.install('zope.event', test)
    zc.buildout.testing.install('zope.exceptions', test)
    zc.buildout.testing.install('zope.filerepresentation', test)
    zc.buildout.testing.install('zope.formlib', test)
    zc.buildout.testing.install('zope.hookable', test)
    zc.buildout.testing.install('zope.i18n', test)
    zc.buildout.testing.install('zope.i18nmessageid', test)
    zc.buildout.testing.install('zope.interface', test)
    zc.buildout.testing.install('zope.lifecycleevent', test)
    zc.buildout.testing.install('zope.location', test)
    zc.buildout.testing.install('zope.minmax', test)
    zc.buildout.testing.install('zope.modulealias', test)
    zc.buildout.testing.install('zope.pagetemplate', test)
    zc.buildout.testing.install('zope.proxy', test)
    zc.buildout.testing.install('zope.publisher', test)
    zc.buildout.testing.install('zope.schema', test)
    zc.buildout.testing.install('zope.security', test)
    zc.buildout.testing.install('zope.session', test)
    zc.buildout.testing.install('zope.size', test)
    zc.buildout.testing.install('zope.structuredtext', test)
    zc.buildout.testing.install('zope.tal', test)
    zc.buildout.testing.install('zope.tales', test)
    zc.buildout.testing.install('zope.testing', test)
    zc.buildout.testing.install('zope.thread', test)
    zc.buildout.testing.install('zope.traversing', test)
    # The BIG dependency mess in zope is really a pain


checker = renormalizing.RENormalizing([
    zc.buildout.testing.normalize_path,
    (re.compile(
    "Couldn't find index page for '[a-zA-Z0-9.]+' "
    "\(maybe misspelled\?\)"
    "\n"
    ), ''),
    (re.compile("""['"][^\n"']+z3c.recipe.paster[^\n"']*['"],"""),
     "'/z3c.recipe.paster',"),
    (re.compile('#![^\n]+\n'), ''),
    (re.compile('-\S+-py\d[.]\d(-\S+)?.egg'),
     '-pyN.N.egg',
    ),
    ])


def test_suite():
    return unittest.TestSuite(
        doctest.DocFileSuite('README.txt',
            setUp=setUp, tearDown=zc.buildout.testing.buildoutTearDown,
            optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS,
            checker=checker),
        )


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')