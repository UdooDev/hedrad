# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{  # pylint: disable=C8101,C8103
    'name': 'Integração Nota Belo Horizonte',
    'description': """Efetua a integração com a prefeitura de Belo Horizonte""",
    'summary': """Efetua a integração com a prefeitura de Belo Horizonte""",
    'version': '11.0.1.0.0',
    'category': "Accounting & Finance",
    'author': 'Udoo',
    'license': 'AGPL-3',
    'website': 'http://www.udoo.com.br',
    'depends': [
        'br_nfse',
    ],
    'data': [
        'views/br_account_service.xml',
        'views/res_company.xml',
        'reports/danfpse.xml',
    ],
    'application': True,
}
