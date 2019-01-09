# -*- coding: utf-8 -*-
{
    'name': "library_management",

    'summary': """
        简单的图书馆管理系统用于Shine IT 的Odoo模块开发教学
        """,

    'description': """
        通过开发一个完整的图书馆管理系统来学习Odoo开发的基本技能
    """,

    'author': "Shine IT",
    'website': "http://www.openerp.cn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Training',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
