from odoo import api, fields, models, tools

class ProdCat(models.Model):
    #This class describes a product category, which is related with suppliers by many2many relationship:

    _name = 'prod.cat'
    _description = 'Product Categories'
    _rec_name = "category"
    category = fields.Char(string='Category', required=True, unique = True)
