from odoo import models, fields, api
from odoo.exceptions import ValidationError

class FleetMaintenance(models.Model):
    _name = 'fleet.maintenance'
    _description = 'Fleet Maintenace'

    vehicle_id = fields.Many2one(comodel_name='fleet.vehicle', string='Vehicle')
    assigned_mechanic_id = fields.Many2one(comodel_name='res.users', string='Assigned Mechanic')
    issue_description = fields.Text(string='Issue Description')
    scheduled_date = fields.Date(string='Scheduled Date')
    completed_date = fields.Date(string='Completed Date')
    parts_used_ids = fields.Many2many(comodel_name='fleet.part', string='Parts Used')
    total_parts_cost = fields.Float(string='Total Parts Cost', compute='_compute_total_parts_cost', store=True)
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string='State', default='draft', required=True)

    def action_confirm(self):
        for record in self:
            if record.state == 'draft':
                record.write({
                    'state': 'scheduled'
                })

    def action_start(self):
        for record in self:
            if record.state == 'scheduled':
                record.write({
                    'state': 'in_progress'
                })

    def action_done(self):
        for record in self:
            if record.state == 'in_progress':
                record.write({
                    'state': 'done'
                })

    def action_cancelled(self):
        for record in self:
            if record.state in ('draft', 'scheduled', 'in_progress'):
                record.write({
                    'state': 'cancelled'
                })
    
    @api.onchange('vehicle_id')
    def _onchange_vehicle_id(self):
        if self.vehicle_id:
            return {
                'domain': {
                    'assigned_mechanic_id': [('id','in',self.vehicle_id.mechanic_ids.ids)]
                }
            }
        return {
            'domain': {
                'assigned_mechanic_id': []
            }
        }
    
    @api.depends('parts_used_ids.unit_cost')
    def _compute_total_parts_cost(self):
        for record in self:
            record.total_parts_cost = sum(record.parts_used_ids.mapped('unit_cost'))
    
    def action_print_job_sheet(self):
        self.ensure_one()

        return self.env.ref(
            'advanced_fleet_maintenance_scheduler.action_vehicle_maintenance_job'
        ).report_action(self)

    @api.constrains('completed_date')
    def validate_completed_date(self):
        for record in self:
            if record.state in ('draft', 'scheduled') and record.completed_date:
                raise ValidationError(f"Vehicle state is on {record.state}, you cannot set completed date yet.")