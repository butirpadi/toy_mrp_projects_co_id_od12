# -*- coding: utf-8 -*-
{
    'name': "Custom MRP Toy Factory",

    'summary': """
        Custom modul untuk Toy Factory, project on projects.co.id""",

    'description': """
        Custom modul untuk Toy Factory, project on projects.co.id
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'mr',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'purchase', 'mrp', 'field_ukuran_product', 'field_additional_sale_order'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_company_view.xml',
        'views/product_template.xml',
        'views/mrp_production_view.xml',
        'views/mrp_bom_view.xml',
        'reports/manufacturing_order_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True
}