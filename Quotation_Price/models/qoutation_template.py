# -*- coding: utf-8 -*-
# Copyright (c) iSoft Solutions Limited

from odoo import fields, models

class QuotationTemplateCustom(models.Model):
    _inherit = "sale.order.template.line"
    _inherit = "sale.order.line"

    price_unit = fields.Float(string="Unit Price")
    analytic_line_ids = (string="Analytic lines")
