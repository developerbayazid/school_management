from odoo import models, fields


class OthersSchool(models.Model):
    _name = "others.school"
    _description = "Others School"
    
    name = fields.Char(string='Name', required=True)
    


class StudentStudyHistory(models.Model):
    _name = 'student.study.history'
    _description = 'Student Study History'

    student_id = fields.Many2one('student.information')
    others_school_id = fields.Many2one('others.school', string="Others School", required=True)
    passing_year = fields.Char(string="Passing Year", required=True)
    class_name = fields.Char(string="Class Name", required=True)
    