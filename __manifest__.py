{
    'name': 'Advanced Fleet Maintenance Scheduler',
    'summary': 'Advanced Fleet Maintenance Scheduler',
    'description': """
    A small tool for scheduling and tracking maintenance on company vehicles — realistic, and a natural companion to the equipment tracker.
    """,
    'author': 'Chike Chiagbaizu',
    'maintainer': 'Chike Chiagbaizu',
    'version': '19.0.1.0.0',
    'license': 'LGPL-3',
    'category': 'Fleet',
    'sequence': 1,
    'application': True,
    'installable': True,
    'depends': [
        'base'
    ],
    'data': [
        'security/group_fleet_maintenance.xml',
        'security/ir.model.access.csv',
        'security/ir_rule_fleet_mechanic.xml',
        'views/fleet_actions.xml',
        'views/view_fleet_maintenance_form.xml',
        'views/view_fleet_maintenance_list.xml',
        'views/view_fleet_part_form.xml',
        'views/view_fleet_part_list.xml',
        'views/view_fleet_vehicle_form.xml',
        'views/view_fleet_vehicle_list.xml',
        'report/action_vehicle_maintenance_job_sheet.xml',
        'report/vehicle_maintenance_job_sheet.xml',
        'views/fleet_menus.xml',
    ]
}