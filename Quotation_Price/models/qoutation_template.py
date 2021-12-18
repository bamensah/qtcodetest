# -*- coding: utf-8 -*-
# Copyright (c) iSoft Solutions Limited

from odoo import fields, models

class SaleOrderTemplate(models.Model):
    _inherits = 'sale.order.template.line'

    description_head = fields.Char(string='Header')
