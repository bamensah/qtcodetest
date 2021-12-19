# -*- coding: utf-8 -*-
# Copyright (c) iSoft Solutions Limited

from odoo import fields, models

class QuotationTemplateCustom(models.Model):
    _inherit = "sale.order.template.line"
    _inherit = "sale.order.line"
    _description = "Quotation Template Custom"

    testone = fields.Float(string="Unit Price")
    testtwo = (string="Analytic lines")
