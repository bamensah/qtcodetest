# -*- coding: utf-8 -*-
# Copyright (c) iSoft Solutions Limited

from odoo import fields, models

class QuotationTemplateCustom(models.Model):
    _inherit = "sale.order.template.line"

    unit_price = fields.Float(string="Unit Price")
