from os import name

from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError


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
    student_image = fields.Binary(string='Image')
    student_document_ids = fields.Many2many('ir.attachment', string='Attachments')
    student_notes = fields.Html(string='Notes')
    number_of_documents = fields.Integer(string='Number of Document', compute="_get_number_of_documents")
    class_id = fields.Many2one('class.information', string='Class', tracking=True)
    gender = fields.Selection(selection=[
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other'),
        ], string='Gender', tracking=True)
    
    
    
    def confirm_student(self):
        for record in self:
            if record.status == 'draft':
                record.status = 'confirmed'
                
                
    def reset_student(self):
        for record in self:
            return{
                "name": _('Draft Reason'),
                "type": "ir.actions.act_window",
                "res_model": "draft.reason",
                "view_mode": "form",
                "target": "new",
                "context": {
                    "default_student_id": record.id,
                },
            }
                
    @api.depends('student_document_ids')            
    def _get_number_of_documents(self):
        for record in self:
            record.number_of_documents = len(record.student_document_ids.ids)
            
            
    @api.constrains('phone_number')
    def _verify_phone_number(self):
        for student in self:
            existing_student = self.env['student.information'].search([('phone_number', '=', student.phone_number), ('id', '!=', student.id)])
            if existing_student:
                raise ValidationError(_("Phone number must be unique. The phone number '%s' is already used by another student.") % student.phone_number)
            if not student.phone_number.isdigit():
                raise ValidationError(_("Phone number must contain only digits."))
            
            
    @api.constrains('email')
    def _verify_email(self):
        for student in self:
            existing_student = self.env['student.information'].search([('email', '=', student.email), ('id', '!=', student.id)])
            if existing_student:
                raise ValidationError(_("Email must be unique. The email '%s' is already used by another student.") % student.email)
            if student.email and not self.env['res.partner'].sudo().check_email([student.email]):
                raise ValidationError(_("Invalid email address."))
            
            
    @api.constrains('roll_number')
    def _verify_roll_number(self):
        for student in self:
            existing_student = self.env['student.information'].search([('roll_number', '=', student.roll_number), ('id', '!=', student.id)])
            if existing_student:
                raise ValidationError(_("Roll number must be unique. The roll number '%s' is already used by another student.") % student.roll_number)