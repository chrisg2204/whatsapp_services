# -*- coding: utf-8 -*-

from datetime import timedelta, date, datetime, time
from odoo import models, fields, api, exceptions, _

import logging

_logger = logging.getLogger(__name__)

class MyModule(models.Model):
    _name = 'my.module'