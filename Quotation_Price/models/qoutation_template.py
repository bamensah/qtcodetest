# -*- coding: utf-8 -*-
# Copyright (c) iSoft Solutions Limited

from odoo import fields, models

class QuotationTemplateCustom(models.Model):
    _inherit = "sale.order.template.line"

    unit_price = fields.Float(string="Unit Price")

class UnitPriceChange(models.Model):
    _inherit = "sale.order.line"

    @api.model
    @api.onchange('price_unit')
    def _onchange_price(self):
        res = super(QuotationTemplateCustom, self)._onchange_price()

        for rec in self:
            rec.price_unit = self.unit_price
        return res
