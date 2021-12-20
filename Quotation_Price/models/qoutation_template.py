# -*- coding: utf-8 -*-
# Copyright (c) iSoft Solutions Limited

from odoo import api, fields, models, _

class QuotationTemplateCustom(models.Model):
    _inherit = "sale.order.template.line"
    _name = "quotation.template.custom"

    unit_price = fields.Float(string="Unit Price")

class UnitPriceChange(models.Model):
    _inherit = "sale.order.line"
    quotation_template_custom_id = fields.Many2one("quotation.template.custom", string="Quotation Template Custom")
    price_unit = fields.Float(string="Unit Price")

    @api.onchange('quotation_template_custom_id')
    def onchange_quotation_template_custom_id(self):
        self.price_unit = self.quotation_template_custom_id.unit_price
