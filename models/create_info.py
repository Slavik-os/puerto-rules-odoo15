from odoo import api,fields,models,tools,_
from odoo.exceptions import ValidationError

class InfoCreateManagment(models.Model):
    _name = "info.managment.create"
    #_inherit = ['expiditeur.select']
    _description = " Model for managment Selection Controll "
    # select_add = fields.Many2one("expiditeur.select",string="add")
    # expiditeur_ids = fields.Selection(select_add=[("NEW","NEWVALUE")])
