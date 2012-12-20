# Copyright 2012 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import textwrap
from six.moves import cStringIO
from awscli.newhelp import HelpParser


class BaseStyle(object):

    def __init__(self, doc, indent_width=4, **kwargs):
        self.doc = doc
        self.indent_width = indent_width
        self.kwargs = kwargs
        self.keep_data = True

    def spaces(self, indent):
        return ' ' * (indent * self.indent_width)

    def start_bold(self, attrs=None):
        return ''

    def end_bold(self):
        return ''

    def bold(self, s):
        return self.start_bold() + s + self.end_bold()

    def h2(self, s):
        return self.bold(s)

    def start_underline(self, attrs=None):
        return ''

    def end_underline(self):
        return ''

    def underline(self, s):
        return self.start_underline() + s + self.end_underline()

    def start_italics(self, attrs=None):
        return ''

    def end_italics(self):
        return ''

    def italics(self, s):
        return self.start_italics() + s + self.end_italics()

    def start_p(self, attrs=None):
        self.doc.add_paragraph()

    def end_p(self):
        pass

    def start_code(self, attrs=None):
        self.doc.do_translation = True
        self.start_bold(attrs)

    def end_code(self):
        self.doc.do_translation = False
        self.end_bold()

    def start_a(self, attrs=None):
        self.doc.do_translation = True
        self.start_underline()

    def end_a(self):
        self.doc.do_translation = False
        self.end_underline()

    def start_i(self, attrs=None):
        self.doc.do_translation = True
        self.start_italic()

    def end_i(self):
        self.doc.do_translation = False
        self.end_italic()

    def start_li(self, attrs):
        pass

    def end_li(self):
        pass

    def start_examples(self, attrs):
        self.doc.keep_data = False

    def end_examples(self):
        self.doc.keep_data = True


class CLIStyle(BaseStyle):

    def start_bold(self, attrs=None):
        if self.kwargs.get('do_ansi', False):
            return u'\033[1m'

    def end_bold(self):
        if self.kwargs.get('do_ansi', False):
            return u'\033[0m'

    def start_underline(self, attrs=None):
        if self.kwargs.get('do_ansi', False):
            return u'\033[4m'

    def end_underline(self):
        if self.kwargs.get('do_ansi', False):
            return u'\033[0m'

    def start_italics(self, attrs=None):
        if self.kwargs.get('do_ansi', False):
            return u'\033[3m'

    def end_italics(self):
        if self.kwargs.get('do_ansi', False):
            return u'\033[0m'

    def start_li(self, attrs=None):
        para = self.doc.add_paragraph()
        para.subsequent_indent = para.initial_indent + 1
        para.write('  * ')

    def end_li(self):
        pass

    def h2(self, s):
        para = self.doc.get_current_paragraph()
        para.lines_before = 1
        return self.bold(s)

    def end_p(self):
        para = self.doc.get_current_paragraph()
        para.lines_after = 2
