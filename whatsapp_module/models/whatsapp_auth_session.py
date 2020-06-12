# -*- coding: utf-8 -*-

from datetime import timedelta, date, datetime, time
from odoo import models, fields, api, exceptions, _

import logging

_logger = logging.getLogger(__name__)

class WhatsappAuthSession(models.Model):
	_description = "Whatsapp Auth Session"
	_name = 'whatsapp.auth.session'
	_inherit = ['mail.thread.cc', 'mail.activity.mixin', 'utm.mixin']

	token = fields.Char()
	refresh_token = fields.Char()
	client_id = fields.Char()
	secret_id = fields.Char()
	num = fields.Char()
	create_date = fields.Datetime('Fecha y hora', default=fields.Datetime.now)

	def get_filtered_record(self):
		raise exceptions.Warning('Ejecutar acción para refrescar el token de whatsapp')
