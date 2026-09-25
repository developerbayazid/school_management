from odoo import fields, models, api


class StudentInformation(models.Model):
    _name = "student.information"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Student Record"
    
    
    name = fields.Char(string="Name", required=True, tracking=True)
    roll_number = fields.Char(string="Roll Number", required=True, tracking=True)
    phone_number = fields.Char(string="Phone Number", required=True, tracking=True)
    email = fields.Char(string="Email", tracking=True)
    father_name = fields.Char(string="Father Name", required=True, tracking=True)
    mother_name = fields.Char(string="Mother Name", tracking=True)
    birth_certificate = fields.Char(string="Birth Certificate", tracking=True)
    address = fields.Char(string="Address", tracking=True)
    
    status = fields.Selection(selection=[
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
        ], default="draft", string='Status', tracking=True)
    
    
    previous_record_ids = fields.One2many(comodel_name='student.study.history', inverse_name='student_id')
    student_image = fields.Binary(string='Image', tracking=True)
    student_document_ids = fields.Many2many('ir.attachment', string='Attachments')
    student_notes = fields.Html(string='Notes')
    number_of_documents = fields.Integer(string='Number of Document', compute="_get_number_of_documents")
    class_id = fields.Many2one('class.information', string='Class', tracking=True)
    
    
    def confirm_student(self):
        for record in self:
            if record.status == 'draft':
                record.status = 'confirmed'
                
                
    def reset_student(self):
        for record in self:
            if record.status == 'confirmed':
                record.status = 'draft'
                
    @api.depends('student_document_ids')            
    def _get_number_of_documents(self):
        for record in self:
            record.number_of_documents = len(record.student_document_ids.ids)