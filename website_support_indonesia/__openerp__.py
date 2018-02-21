# -*- coding: utf-8 -*-
{
    'name': "Website Support Indonesia",

    'summary': """
        Quick Response Ticket for HR Division
    """,

    'description': """
        Quick Response Ticket for HR Division
    """,

    'author': "Palma Group",
    'website': "http://palmagroup.co.id",

    'category': 'Tools',
    'version': '0.1',

    'depends': ['base','website_support'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/inherit_website_support_ticket_categories_view.xml',
        'views/website_support_indonesia_view.xml',
        'views/website_support_ticket_templates.xml',
        'wizard/set_category_sla_wizard.xml',
        'views/mail_template_schedule_pic.xml',    
    ],
    
    'demo': [
        'demo/demo.xml',
    ],
}