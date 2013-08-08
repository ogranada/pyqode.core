#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# PCEF - Python/Qt Code Editing Framework
# Copyright 2013, Colin Duquesnoy <colin.duquesnoy@gmail.com>
#
# This software is released under the LGPLv3 license.
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
"""
This package contains the core modes (language independant)
"""
from pcef.core.modes.caret_line_highlight import CaretLineHighlighterMode
from pcef.core.modes.checker import CheckerMode, CheckerMessage
from pcef.core.modes.checker import MSG_STATUS_ERROR
from pcef.core.modes.checker import MSG_STATUS_INFO
from pcef.core.modes.checker import MSG_STATUS_WARNING
from pcef.core.modes.checker import CHECK_TRIGGER_TXT_CHANGED
from pcef.core.modes.checker import CHECK_TRIGGER_TXT_SAVED
from pcef.core.modes.code_completion import CodeCompletionMode
from pcef.core.modes.code_completion import CompletionProvider
from pcef.core.modes.code_completion import Completion
from pcef.core.modes.code_completion import DocumentWordCompletionProvider
from pcef.core.modes.filewatcher import FileWatcherMode
from pcef.core.modes.matcher import SymbolMatcherMode
from pcef.core.modes.right_margin import RightMarginMode
from pcef.core.modes.zoom import ZoomMode
from pcef.core.modes.pygments_syntax_highlighter import PygmentsSyntaxHighlighter
from pcef.core.modes.pygments_syntax_highlighter import PYGMENTS_STYLES
from pcef.core.modes.indenter import AutoIndentMode


__all__ = ["CaretLineHighlighterMode", "CheckerMode", "CheckerMessage",
           "MSG_STATUS_ERROR", "MSG_STATUS_WARNING", "MSG_STATUS_INFO",
           "CHECK_TRIGGER_TXT_SAVED", "CHECK_TRIGGER_TXT_CHANGED",
           "CodeCompletionMode", "CompletionProvider", "Completion",
           "DocumentWordCompletionProvider", "FileWatcherMode",
           "SymbolMatcherMode",
           "RightMarginMode", "ZoomMode", "PygmentsSyntaxHighlighter",
           "PYGMENTS_STYLES", "AutoIndentMode"]
