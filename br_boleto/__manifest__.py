# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{  # pylint: disable=C8101,C8103
    'name': 'Pagamentos via Boleto Bancário',
    'summary': """Permite gerar e realizar a integração bancária através de
        arquivo CNAB 240""",
    'description': """Permite gerar e realizar a integração bancária através de
        arquivo CNAB 240""",
    'version': '11.0.1.0.0',
    'category': 'account',
    'author': 'Udoo',
    'license': 'AGPL-3',
    'website': 'http://www.udoo.com.br',
    'depends': [
        'br_account_payment', 'br_data_account_product'
    ],
    'external_dependencies': {
        'python': [
            'pyboleto',
        ],
    },
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings.xml',
        'views/account_invoice.xml',
        'views/account_move_line.xml',
        'views/res_partner_bank.xml',
        'views/payment_order.xml',
        'views/payment_mode.xml',
        'views/account_journal.xml',
        'reports/report_print_button_view.xml',
        'sequence/payment_order_sequence.xml',
        'sequence/numero_documento_sequence.xml',
        'wizard/br_boleto_wizard.xml',
        'wizard/send_boleto_email.xml',
    ],
    'installable': True,
    'application': True,
}
