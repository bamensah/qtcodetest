# -*- coding: utf-8 -*-
# Copyright (c) iSoft Solutions Limited

from odoo import fields, models

class QuotationTemplateCustom(models.Model):
    _inherit = "sale.order.template.line"

class UnitPriceCustom(models.Model):
    _inherits = {"sale.order.line":"price_unit"}

    price_unit = fields.Float("sale.order.line" , string="Unit Price")
