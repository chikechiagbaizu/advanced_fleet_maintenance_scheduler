from odoo import fields, models

class FleetPart(models.Model):
    _name = 'fleet.part'
    _description = 'Fleet Part'

    name = fields.Char(string='Part Name')
    unit_cost = fields.Float(string='Unit Cost')