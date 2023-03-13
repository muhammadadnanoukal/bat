from odoo import fields, models

import inspect


class MailActivity(models.Model):
    _inherit = 'mail.activity'

    def activity_format(self):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        print('caller name:', calframe[1][3])
        result = super(MailActivity, self).activity_format()
        activity_type_approval_id = self.env.ref('approvals.mail_activity_data_approval').id
        print('got to activity', activity_type_approval_id)
        for activity in result:
            if activity['activity_type_id'][0] == activity_type_approval_id and \
                    activity['res_model'] == 'approval.request':
                request = self.env['approval.request'].browse(activity['res_id'])
                approver = request.approver_ids.filtered(lambda approver: activity['user_id'][0] == approver.user_id.id)
                activity['approver_id'] = approver.id
                activity['approver_status'] = approver.status
        print('result in activity_format', result)
        return result
