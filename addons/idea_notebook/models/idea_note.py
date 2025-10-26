from odoo import models, fields

class IdeaNote(models.Model):
    _name = 'idea.note' 
    _description = 'Sổ tay ý tưởng'
    
    name = fields.Char(string='Tiêu đề', required=True)
    description = fields.Text(string='Mô tả chi tiết')
    
    category = fields.Selection([
        ('personal', 'Cá nhân'),
        ('work', 'Công việc'),
        ('project', 'Dự án')
    ], string='Phân loại', default='personal')
    
    is_important = fields.Boolean(string='Quang trọng ?')