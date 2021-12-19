# -*- coding: utf-8 -*-
# Copyright (c) iSoft Solutions Limited

from odoo import fields, models

class QuotationTemplateCustom(models.Model):
    _inherit = 'sale.order.template.line'

    price_unit = fields.Float('sale.order', string='Unit Price')
