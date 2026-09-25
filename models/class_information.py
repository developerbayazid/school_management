from odoo import models, fields, api

class ClassInformation(models.Model):
    _name = 'class.information'
    _description = 'Class Information'

    name = fields.Char(string="Name", required=True)
    class_teacher_id = fields.Many2one('res.partner', string='Teacher' ,required=True)
    number_of_seat = fields.Integer(string='Number of Seat', required=True)
    