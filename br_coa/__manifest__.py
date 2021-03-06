# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


{  # pylint: disable=C8101,C8103
    'name': 'Plano de Contas Brasil',
    'summary': """Plano de contas Brasileiro""",
    'description': """Plano de contas Brasileiro""",
    'version': '11.0.1.0.0',
    'category': 'Localization',
    'author': 'Udoo',
    'license': 'AGPL-3',
    'website': 'http://www.udoo.com.br',
    'depends': [
        'account', 'br_account'
    ],
    'data': [
        'data/br_chart_data.xml',
        'data/account.account.template.csv',
        'data/account_tax_template_data.xml',
        # TODO Achar uma forma de carregar o template
        # 'data/account_chart_template_data.yml',
    ],
    'active': True,
}
