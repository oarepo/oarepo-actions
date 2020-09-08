# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# oarepo-actions is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""oarepo-actions."""

from __future__ import absolute_import, print_function

from .version import __version__
from .ext import Actions
__all__ = ('__version__', 'Actions',)
