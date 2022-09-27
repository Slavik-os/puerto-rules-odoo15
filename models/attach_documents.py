from odoo import api,fields,models,tools,_
from datetime import datetime
from odoo.exceptions import ValidationError


class AttachDocument(models.Model):
    _name ="attach.document.managment"
    _inherit = ['mail.thread','mail.activity.mixin',]
    _description = "Attach Document managment for puerto transit"

    attachment_type = fields.Selection([
        ('Annexe Outlook','Annexe Outlook'),
        ('Annexe Commerciale','Annexe Commerciale')],string="Type d'annexe",tracking=True)

    documment_type = fields.Selection([
        ("Annexe Signature", "Annexe Signature"),
        ("AUTORISATION DOUANE", "AUTORISATION DOUANE"),
        ("Bon a deliverer", "Bon a deliverer"),
        ("BULLETIN ENTREE", "BULLETIN ENTREE"),
        ("BULLETIN SORTIE", "BULLETIN SORTIE"),
        ("CERTIFICAT D'iNSPECTION", "CERTIFICAT D'iNSPECTION"),
        ("CHEQUE", "CHEQUE"),
        ("CMR", "CMR"),
        ("CONFIRMATION DU CHARGE", "CONFIRMATION DU CHARGE"),
        ("Connaissement", "Connaissement"),
        ("Copie DUM", "Copie DUM"),
        ("Copie Sous DUM", "Copie Sous DUM"),
        ("Demande de service", "Demande de service"),
        ("Demande de Tr", "Demande de Tr"),
        ("DETAIL FACTURE", "DETAIL FACTURE"),
        ("Bat des factures", "Bat des factures"),
        ("Bat Ventillation", "Bat Ventillation"),
        ("EUR1", "EUR1"),
        ("FACTURE ONSA", "FACTURE ONSA"),
        ("Facture PORTNET", "Facture PORTNET"),
        ("Factures", "Factures"),
        ("Fiche dimputation", "Fiche dimputation"),
        ("Fiche de liquidation", "Fiche de liquidation"),
        ("LISTE DE COLISAGE", "LISTE DE COLISAGE"),
        ("LTA", "LTA"),
        ("Main Levee", "Main Levee"),
        ("Servicede Taxation", "Servicede Taxation"),
        ("NOTE D'EMBARQUEMENT", "NOTE D'EMBARQUEMENT"),
        ("NOTE DE FRET", "NOTE DE FRET"),
        ("PHYTO SANITAIRE", "PHYTO SANITAIRE"),
        ("RECU ESPECE", "RECU ESPECE"),
        ("RMT", "RMT"),
        ("SCELLES", "SCELLES"),
        ("SWIFT BANCAISE B.G AT", "SWIFT BANCAISE B.G AT"),
        ("Ticket de paiement", "Ticket de paiement"),
        ("TMPA", "TMPA"),
        ("TRYTIQUE", "TRYTIQUE"),
        ("VERSEMENT", "VERSEMENT"),
        ("VIREMENT", "VIREMENT"),

    ],string="Type document",tracking=True)

    comment = fields.Text(string="",tracking=True)
    upload_attach = fields.Binary(string="Attachment")
    document_fname = fields.Char(string="File Name")
    date_time_created = fields.Char(string="Date & Temp de creation",compute="_compute_today_time_date")

    def _compute_today_time_date(self):
        for rec in self :
            rec.date_time_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")