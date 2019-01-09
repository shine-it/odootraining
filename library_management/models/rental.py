# -*- coding: utf-8 -*-

from odoo import models, fields


class Rental(models.Model):
    _name = 'library.rent'
    _description = '图书借阅'

    code = fields.Char(string="编码")
    user_id = fields.Many2one(string="管理员", comodel_name="res.users")
    book_id = fields.Many2one(comodel_name='library.book', string='书籍')
    partner_id = fields.Many2one(comodel_name='res.partner', string='借阅者')
    start_date = fields.Datetime(string='起始时间')
    end_date = fields.Datetime(string='到期时间')
    state = fields.Selection(selection=[
                                ('draft', '草稿'),
                                ('rent', '已出借'),
                                ('exrent', '已延期'),
                                ('return', '已归还'),
                                ('cancel', '已取消')
                            ], string='状态')
