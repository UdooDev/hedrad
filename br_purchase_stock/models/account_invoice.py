# -*- coding: utf-8 -*-
# © 2016 Danimar Ribeiro, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    def comput_despesas(self, total_despesas, total_qty, line_qty):
    	eq_number = total_despesas/total_qty
    	return line_qty * eq_number

    def _prepare_invoice_line_from_po_line(self, line):
        res = super(AccountInvoice, self)._prepare_invoice_line_from_po_line(
            line)
        total_qty = sum(l.product_qty for l in line.order_id.order_line)
        total_despesas = line.order_id.total_outras_despesas
        res['valor_seguro'] = line.valor_seguro
        res['outras_despesas'] = res['outras_despesas'] = self.comput_despesas(total_despesas, total_qty, line.product_qty) if total_despesas > 0 else line.outras_despesas
        res['valor_frete'] = line.valor_frete
        return res
