# -*- coding: utf-8 -*-
{
    'name': "Eric's Real Estate app",

    'summary': """
        This is a practice module. Via Odoo documentation.""",

    'description': """
        This is a practice module that will be used to simulate a real estate type application.
    """,

    'author': "Eric Callaway",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/estate_property.xml',
        'views/estate_menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}