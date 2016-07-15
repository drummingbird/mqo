from openerp import models, fields, api

class Mqo_InviteOnly(models.Model):
    _name = 'survey.survey'
    _inherit = 'survey.survey'
    
    # should move survey stuff into separate module.
    invite_only = fields.Boolean(string="Invite only?", default=False)

