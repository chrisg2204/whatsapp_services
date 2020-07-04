# -*- coding: utf-8 -*-

from datetime import timedelta, date, datetime, time
from odoo import models, fields, api, exceptions, _

import logging

_logger = logging.getLogger(__name__)

class WhatsappMessage(models.Model):
	_description = "Whatsapp Message"
	_name = 'whatsapp.message'
	_inherit = ['mail.thread.cc', 'mail.activity.mixin', 'utm.mixin']

	num_des = fields.Char(string="Número receptor")
	num_from = fields.Char(string='Número emisor')
	state = fields.Char(string='Estado')
	file_type = fields.Char(string='Tipo de archivo')
	module_name = fields.Char(string='Módulo de destino')
	attachment_rel_id = fields.Many2one('ir.attachment', 'Archivo')
	
	create_date = fields.Datetime('Fecha y hora', default=fields.Datetime.now)