# -*- coding: utf-8 -*-
# Copyright (c) iSoft Solutions Limited

from odoo import fields, models

class QuotationTemplateCustom(models.Model):
    _name = "quotation.template.custom"
    _inherit = ['sale.order.template.line','sale.order.line']
    _description = "Quotation Template Custom"

    testone = fields.Float(string="Unit Price")
    testtwo = (string="Analytic lines")
