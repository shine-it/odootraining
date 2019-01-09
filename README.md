# Odoo 技术培训

## Scaffolding

生成模块基本结构
```bash
cd odoo #进入Odoo根目录
./odoo-bin scaffold library_management ~/odootraining 
```
## 创建模型（基础字段）

创建`library.books`对象及其相关字段

- `name = fields.Char(string='书名')`
- `isbn = fields.Char(string='ISBN')`
- `type = fields.Selection（string='类型', ..)`
- `purchase_date = fields.Date(string='采购日期')`
- `purchase_price = fields.Float(string='采购价格')`
- `book_cover = fields.Binary(string='封面')`

## 创建模型 (关联字段)

创建`library.rent`对象及其相关字段:

- `code = fields.Char(string="编码")`
- `user_id = fields.Many2one(string="管理员", comodel_name="res.users")`
- `book_id = fields.Many2one(comodel_name='library.book', string='书籍')`
- `partner_id = fields.Many2one(comodel_name='res.partner', string='借阅者')`
- `start_date = fields.Datetime(string='起始时间')`
- `end_date = fields.Datetime(string='到期时间')`
- `state = fields.Selection(string='状态', ..)`

对`library.books`对象增加字段：

- `rental_ids = fields.One2many(comodel_name='library.rent', inverse_name='book_id', string='借阅记录')`
