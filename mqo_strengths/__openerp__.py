# -*- coding: utf-8 -*-
{
    'name': "MQO Strengths",

    'summary': """Manage strengths""",

    'description': """
        MQO module for managing strengths:
    """,

    'author': "Your Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'survey'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'templates/templates.xml',
        # 'views/survey.xml',
        #'views/session_workflow.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}