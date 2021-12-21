# -*- coding: utf-8 -*-
# Copyright (c) iSoft Solutions Limited

from odoo import api, fields, models, _

class SaleOrderTemplateLine(models.Model):
    _inherit = "sale.order.template.line"

    unit_price = fields.Float(string='Unit Price')

class SaleOrderLine(models.Model):
    _inherit = "sale.order"

    @api.onchange('sale_order_template_id')
    def onchange_sale_order_template_id(self):
        ret = super(SaleOrder, self).onchange_sale_order_template_id()
        if self.sale_order_template_id:
            template_price = self.sale_order_template_id.with_context(lang=self.product_id.unit_price)
            self.price_unit = template.unit_price
            return ret
