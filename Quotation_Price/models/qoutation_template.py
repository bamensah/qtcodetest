# -*- coding: utf-8 -*-
# Copyright (c) iSoft Solutions Limited

from odoo import fields, models

class GetUnitPrice(models.Model):
    _name = 'custom.unit.price'
    _inherits = {'sale.order':'price_unit'}

class QuotationTemplateCustom(models.Model):
    _inherit = 'custom.unit.price'
    _inherit = 'sale.order.template.line'
    unit_price = fields.Float(string='Unit Price')
