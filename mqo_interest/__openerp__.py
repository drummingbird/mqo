# -*- coding: utf-8 -*-
{
    'name': "MQO Interest",

    'summary': """Manage interest""",

    'description': """
        MQO module for managing interest:
    """,

    'author': "Your Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mqo_program', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/interest.xml',
        'views/program.xml',
        'templates/templates.xml',
        #'views/session_workflow.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}