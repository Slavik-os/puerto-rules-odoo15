from odoo import api,fields,models,tools,_
from odoo.exceptions import ValidationError


class FolderChargesManagment(models.Model):
    _name ="folder.charges.managment"
    _inherit = ['mail.thread','mail.activity.mixin',]
    _description = "Folder Charges managment for puerto transit"

