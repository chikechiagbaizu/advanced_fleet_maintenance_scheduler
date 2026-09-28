from odoo import models, fields, api

class FleetMaintenancePartLine(models.Model):
    _name = 'fleet.maintenance.part.line'
    _description = 'Fleet Maintenance Part Line'

    maintenance_id = fields.Many2one(comodel_name='fleet.maintenance', string='Maintenance Job', required=True, ondelete='cascade')
    part_id = fields.Many2one(comodel_name='fleet.part', string='Part', ondelete='cascade')
    unit_cost = fields.Float(related='part_id.unit_cost', string='Unit Cost', store=True)
    quantity = fields.Float(string='Quantity', default=1.0, required=True)
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True)

    @api.depends('unit_cost','quantity')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.unit_cost