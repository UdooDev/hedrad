# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{  # pylint: disable=C8101,C8103
    'name': 'Brazilian Localization Purchase',
    'description': 'Brazilian Localization for Purchase',
    'category': 'purchase',
    'license': 'AGPL-3',
    'author': 'Udoo',
    'website': 'http://www.udoo.com.br',
    'version': '11.0.1.0.0',
    'depends': [
        'purchase', 'br_account',
    ],
    'data': [
        'views/purchase_view.xml',
        'views/account_invoice.xml',
        'views/product.xml',
    ],
    'installable': True,
    'auto_install': True
}