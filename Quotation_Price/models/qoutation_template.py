# -*- coding: utf-8 -*-
# Copyright (c) iSoft Solutions Limited

from odoo import fields, models

class QuotationTemplateCustom(models.Model):
    _inherit = "sale.order.template.line"
    _inherits = {"sale.order.line":"analytic_line_ids"}

    unit_price = fields.Float(string="Unit Price")
    analytic_line_ids = fields.one2many("sale.order.line" , string="Analytic lines")
