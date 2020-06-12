# -*- coding: utf-8 -*-
{
    'name': "whatsapp_module",
    'summary': """Módulo administrativo whatsapp business""",
    'description': """Módulo para gestionar credenciales del servicio interno whatsapp business""",
    'author': "cgimenez@spearhead.global",
    'website': "https://www.spearhead.global/",
    'category': 'Module',
    'version': '0.0.1',
    'depends': ['base', 'base_rest_whatsapp'],
    'data': [
        'security/ir.model.access.csv',
        'views/whatsapp_message.xml',
        'views/whatsapp_auth_session_view.xml',
        'views/whatsapp_opts_view.xml',
        'views/menu_view.xml',
        'views/res_config_settings_view.xml',
    ]
}
