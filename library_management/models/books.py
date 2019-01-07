# -*- coding: utf-8 -*-

from odoo import models, fields


class Books(models.Model):
    _name = 'library.books'

    name = fields.Char(string='书名')
    isbn = fields.Char(string='ISBN')
    type = fields.Selection(selection=[
                            ('HC', '精装本'),
                            ('SC', '平装本'), ], string='类型')
    purchase_date = fields.Date(string='采购日期')
    purchase_price = fields.Float(string='采购价格', digits=(6, 2))
    book_cover = fields.Binary(string='封面', attachment=True)
