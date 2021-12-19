# -*- coding: utf-8 -*-
# Copyright (c) iSoft Solutions Limited

from odoo import fields, models

class SaleOrderTemplate(models.Model):
    _inherit = 'sale.order.template'
    _inherit = 'sale.order.template.line'

    description_head = fields.Char(string='Header')
