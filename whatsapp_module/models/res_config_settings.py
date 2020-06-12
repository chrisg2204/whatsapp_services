# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):

	_inherit = 'res.config.settings'

	client_id = fields.Char()
	secret_id = fields.Char()
