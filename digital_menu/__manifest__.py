# See LICENSE file for full copyright and licensing details.

{
    'name': 'Upload Digital Menu With Odoo',
    'version': '12.0.1.0.0',
    'license': 'LGPL-3',
    'category': 'Extra Tools',
    'author': 'Serpent Consulting Services Pvt. Ltd.',
    'website': 'https://www.serpentcs.com',
    'depends' : ['website','portal'],
    'data': [
        'security/ir.model.access.csv',
        'views/upload_menu.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'price': 129,
    'currency': 'EUR'
}
