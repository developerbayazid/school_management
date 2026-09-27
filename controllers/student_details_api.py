from odoo import http
from odoo.http import request


class StudentDetailsAPI(http.Controller):

    @http.route(
        '/student/details',
        type='http',
        auth='user',
        website=True
    )
    def get_student_details(self, **kwargs):

        students = request.env['student.information'].search(
            [],
            order='name asc'
        )

        values = {
            'students': students,
        }

        return request.render(
            'school_management.portal_my_student_details',
            values
        )

    @http.route(
        '/student/details/<int:student_id>',
        type='http',
        auth='user',
        website=True
    )
    def get_student_profile(self, student_id, **kwargs):

        student = request.env['student.information'].browse(student_id)

        if not student.exists():
            return request.not_found()

        values = {
            'student': student,
        }

        return request.render(
            'school_management.student_profile',
            values
        )