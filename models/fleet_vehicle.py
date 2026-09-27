from odoo import models, fields

class FleetVehicle(models.Model):
    _name = 'fleet.vehicle'
    _description = 'Fleet Vehicle'

    name = fields.Char(string='Plate Number')
    vehicle_type = fields.Selection(selection=[
        ('car','Car'),
        ('van','Van'),
        ('truck','Truck'),
    ], string='Vehicle Type')
    mechanic_ids = fields.Many2many(comodel_name='res.users', string='Mechanics')