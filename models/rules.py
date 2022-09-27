from odoo import api,fields,models,tools,_
from odoo.exceptions import ValidationError

class RulesManagment(models.Model):
    _name ="rules.creation"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Rules managment for puerto transit"
    _rec_name = 'rule_name'

    rule_name = fields.Char(string="Rule name")
    rules = fields.Text(string="Rule")