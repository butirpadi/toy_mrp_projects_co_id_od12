from odoo import fields, api, models

class res_company(models.Model):
    _inherit = "res.company"

    sw_report_header = fields.Binary('Report Header')
    sw_report_header_landscape = fields.Binary('Report Header Landscape')