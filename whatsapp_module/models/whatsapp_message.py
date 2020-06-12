# -*- coding: utf-8 -*-

from datetime import timedelta, date, datetime, time
from odoo import models, fields, api, exceptions, _

import logging

_logger = logging.getLogger(__name__)

class WhatsappMessage(models.Model):
	_description = "Whatsapp Message"
	_name = 'whatsapp.message'
	_inherit = ['mail.thread.cc', 'mail.activity.mixin', 'utm.mixin']

	num_des = fields.Char()
	num_from = fields.Char()
	create_date = fields.Datetime('Fecha y hora', default=fields.Datetime.now)
	state = fields.Char()
	fname = fields.Char()
	attachment = fields.Binary()