from odoo import api, fields, models


class QualityAlertTeam(models.Model):
    _inherit = "quality.alert.team"

    team_members = fields.Many2many('res.users', string='Team Members')
