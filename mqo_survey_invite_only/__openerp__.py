# -*- coding: utf-8 -*-
{
    'name': "MQO Survey Invite Only",

    'summary': """Make surveys invite only""",

    'description': """
        MQO module to make surveys invite only:
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
        'views/survey.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}