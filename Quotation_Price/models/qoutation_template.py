# -*- coding: utf-8 -*-
# Copyright (c) iSoft Solutions Limited

from odoo import fields, models

class UnitPriceCustom(models.Model):
    _name = "unit.price.custom"
    _inherits = {"sale.order.line":"price_unit"}

class QuotationTemplateCustom(models.Model):
    _inherit = "sale.order.template.line"
    _inherit = "unit.price.custom"

    price_unit = fields.Float(string="Unit Price")
