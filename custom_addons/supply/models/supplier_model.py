# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools

class Supplier(models.Model):
    #This class describes a supplier, which is related with products (product categories) by many2many relationship:
    #Each supplier may supply several products
    #company, website, product_ids are required fields while notes are optional

    _name = "supplier"
    _description = "Supplier Contact Data"
    _rec_name = "company"

    company = fields.Char(string='Company', required=True, unique = True)
    website = fields.Char(string='Website', required = True)
    product_ids = fields.Many2many('prod.cat', string='Products', required = True)
    notes = fields.Text(string='Notes')





