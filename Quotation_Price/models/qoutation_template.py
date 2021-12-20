# -*- coding: utf-8 -*-
# Copyright (c) iSoft Solutions Limited

from odoo import fields, models, api

class QuotationTemplateCustom(models.Model):
    _inherit = "sale.order.template.line"

    unit_price = fields.Float(string="Unit Price")

class UnitPriceChange(models.Model):
    _inherit = "sale.order.line"

    @api.onchange('price_unit')
    def onchange_price_unit(self):

        res = super(QuotationTemplateCustom,self).onchange_price_unit()

        for rec in self:
            self.price_unit = rec.unit_price
        return res
