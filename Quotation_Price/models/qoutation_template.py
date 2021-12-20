# -*- coding: utf-8 -*-
# Copyright (c) iSoft Solutions Limited

from odoo import api, fields, models, _

class SaleOrderTemplateLine(models.Model):
    _inherit = "sale.order.template.line"

    unit_price = fields.Float('Unit Price' , store=True)

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    price_unit = fields.Float('Unit Price', related='product_id.unit_price', store=True)
