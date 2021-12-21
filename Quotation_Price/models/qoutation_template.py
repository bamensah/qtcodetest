# -*- coding: utf-8 -*-
# Copyright (c) iSoft Solutions Limited

from odoo import api, fields, models, _

class SaleOrderTemplateLine(models.Model):
    _inherit = "sale.order.template.line"

    unit_price = fields.Float(string='Unit Price')

class SaleOrderLine(models.Model):
    _inherit = "sale.order"

    @api.onchange('product_id')
    def SetUnitPrice(self):
        if self.product_id:
            self.name = self.product_id.display_name
            self.price_unit = self.product_id.unit_price
