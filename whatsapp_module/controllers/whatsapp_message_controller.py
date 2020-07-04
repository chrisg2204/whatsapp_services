# -*- coding: utf-8 -*-
# 
from odoo import http
from odoo.http import Controller, route, request, Response
from datetime import datetime

import json
import yaml
import logging

_logger = logging.getLogger(__name__)

class WhatsappMessageController(http.Controller):
	
	@http.route('/action', auth='public')
	def index(self, **kw):
		return "Hello, world"


	@http.route('/action/in', auth='public', methods=['POST'], type='json' ,cors='*')
	def message_in(self, **kw):
		"""
			Método para controlar los mensajes entrantes a BotMaker
		"""
		_logger.info('\n run message_in \n')

		data = request.httprequest.data
		body_json = yaml.load(data)
		_logger.info(body_json)

		headers = {'Content-Type': 'application/json'}
		body = { 'results': { 'code':200, 'message':'OK' } }

		return Response(json.dumps(body), headers=headers)


	@http.route('/action/out', auth='public', methods=['POST'], type='json' ,cors='*')
	def message_out(self, **kw):
		"""
			Método para controlar los mensajes salientes de BotMaker
		"""
		_logger.info('\n run message_out \n')

		data = request.httprequest.data
		body_json = yaml.load(data)
		_logger.info(body_json)

		headers = {'Content-Type': 'application/json'}
		body = { 'results': { 'code':200, 'message':'OK' } }

		return Response(json.dumps(body), headers=headers)
