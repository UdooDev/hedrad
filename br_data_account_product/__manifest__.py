# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{  # pylint: disable=C8101,C8103
    'name': 'Odoo Brasil - Dados Account Product',
    'description': 'Brazilian Localisation Data Extension for Product',
    'license': 'AGPL-3',
    'author': 'Udoo',
    'website': 'http://www.udoo.com.br',
    'version': '11.0.1.0.0',
    'depends': [
        'br_data_account',
    ],
    'data': [
        'data/br_account_product.xml',
    ],
    'demo': [
    ],
    'post_init_hook': 'post_init',
    'category': 'Localisation',
    'auto_install': True,

}
