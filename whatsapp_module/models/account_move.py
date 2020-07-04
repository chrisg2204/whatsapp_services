# -*- coding: utf-8 -*-

from datetime import timedelta, date, datetime, time
from odoo import models, fields, api, exceptions, _

import logging

_logger = logging.getLogger(__name__)

class WhatsappModuleAccountMove(models.Model):

	_inherit = 'account.move'

	def action_post(self):

		if self.filtered(lambda x: x.journal_id.post_at == 'bank_rec').mapped('line_ids.payment_id').filtered(lambda x: x.state != 'reconciled'):
			raise UserError(_("A payment journal entry generated in a journal configured to post entries only when payments are reconciled with a bank statement cannot be manually posted. Those will be posted automatically after performing the bank reconciliation."))
		
		self._get_invoice_file()
		return self.post()


	def _get_invoice_file(self):

		file = self.env['ir.attachment'].search([
			('res_id', '=', self.id)
		])
		_logger.info('init dev \n \n \n')
		# solicitar credenciales de whatsapp
		# ejecutar solicitud http POST
		ws_message = self.env['whatsapp.message'].create({
			'file_type': 'factura',
			'module_name': file.res_model,
			'state': 'enviado',
			'attachment_rel_id': file.id

			})

		# _logger.info(file.name)
		_logger.info('\n \n \n end dev')
