# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class DraftReason(models.TransientModel):
    _name = 'draft.reason'
    _description = _('Draft Reason')

    student_id = fields.Many2one('student.information', string=_('Student'), required=True)
    reason = fields.Text(string=_('Reason'), required=True)


    def add(self):       
        self.student_id.write(
            {
                'status': 'draft',
            }
        )
        
        self.student_id.message_post(
            body=_('Student status changed to draft. Reason: %s') % self.reason,
            subtype_xmlid='mail.mt_note'
        )
       