# -*- coding: utf-8 -*-
# Copyright (c) iSoft Solutions Limited

from odoo import api, fields, models, _

class QuotationTemplateCustom(models.Model):
    _inherit = ['sale.order.template.line','sale.order.line']

    unit_price = fields.Float(string="Unit Price")
    price_unit = fields.Float(string="Unit Price")

    @api.onchange('price_change')
    def onchange_price_change(self):
        self.price_unit = self.unit_price
