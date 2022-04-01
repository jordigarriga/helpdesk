# -*- coding: utf-8 -*-
{
    'name': 'HelpDesk',
    'summary': 'Module to support teams',
    'version': '13.0.1.0.0',
    'category': 'Customer Relationship Management',
    'website': '',
    'author': 'Jordi G.S <jordigarrigaseres1@gmail.com>',
    'license': 'AGPL-3',
    'data': [
        'security/helpdesk_security.xml',
        'security/ir.model.access.csv',
        'views/helpdesk_ticket_views.xml',
        'views/helpdesk_team_views.xml',
        'views/helpdesk_ticket_stage_views.xml',
        'views/helpdesk_menu_views.xml',
    ],
    'depends': [
        'base'
    ],
    'application': True,
    'installable': True,
}

