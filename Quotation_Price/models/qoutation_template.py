# -*- coding: utf-8 -*-
# Copyright (c) iSoft Solutions Limited

from odoo import api, fields, models, _

class QuotationTemplateCustom(models.Model):
    _inherit = ['sale.order.template.line','sale.order.line']

    price_unit = fields.Float("sale.order.line", string="Unit Price")
    
