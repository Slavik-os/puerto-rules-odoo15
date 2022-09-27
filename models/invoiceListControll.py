from odoo import api,fields,models,tools,_
from odoo.exceptions import ValidationError


class InvoiceListControll(models.Model):
    _name ="invoice.list.controll"
    _description = "Invoice List Controll for Puerto transit application"
    # Entete fecture

    dum_ids = fields.Many2one("folder.managment",sring="N Dum")
    dum = fields.Char(related="dum_ids.n_dum",string="N Dum")
    currency_id = fields.Many2one("res.currency", string="Valuta", required=True)