from . import models
from odoo import api, fields, SUPERUSER_ID


def _compute_current_approver(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    all_requests = env['approval.request'].sudo().search([])
    for rec in all_requests:
        print('hook', rec)
        rec.compute_current_approver()
    # if any(c.partner_id.country_id.code == 'MX' for c in env['res.company'].search([])):
    #     l10n_mx = env['ir.module.module'].sudo().search([
    #         ('name', '=', 'l10n_mx_hr'),
    #         ('state', 'not in', ['installed', 'to install', 'to upgrade']),
    #     ])
    #     if l10n_mx:
    #         l10n_mx.button_install()
