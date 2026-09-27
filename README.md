# Fleet Maintenance Scheduler

An Odoo module for scheduling and tracking maintenance jobs on company vehicles — which vehicle, which mechanic, what parts were used, and the full job lifecycle from request to completion.

Built as a hands-on learning project to practice Many2many relations, dynamic domains, multi-state workflows, QWeb PDF reporting, and layered role-based security (including field-level write restrictions beyond what `ir.rule` alone can enforce).

## Features

- **Vehicle and mechanic pool management** — register vehicles and assign a pool of qualified mechanics to each one.
- **Parts catalog** — a simple parts list with per-unit cost, reusable across maintenance jobs.
- **Dynamic mechanic assignment** — when scheduling a job, only mechanics qualified for the selected vehicle are selectable.
- **Full maintenance workflow** — jobs move through a real state machine: `Draft → Scheduled → In Progress → Done`, with a separate `Cancelled` path from any open state.
- **Automatic cost calculation** — total parts cost is computed live from the parts used on a job.
- **Printable job sheets** — a QWeb-generated PDF summarizing the vehicle, mechanic, parts used, and total cost for a given job.
- **Data integrity rule** — a job's completion date can't be set while it's still in `Draft` or `Scheduled`.
- **Two-tier role-based security**
  - **Fleet Managers** — full access to vehicles, parts, and all maintenance jobs.
  - **Fleet Mechanics** — can view and update only their own assigned jobs (to progress them through the workflow), but cannot create, delete, reassign, or reschedule jobs. This restriction is enforced at both the record level (`ir.rule`) and the field level (a `write()` override), since standard record rules alone can't prevent a user from editing specific fields on a record they're otherwise allowed to touch.
  - All other users have no access to fleet data by default.

## Models

| Model | Purpose |
| --- | --- |
| `fleet.vehicle` | Master data for company vehicles, including their pool of qualified mechanics |
| `fleet.part` | Simple parts catalog (name + unit cost) |
| `fleet.maintenance` | A single maintenance job: vehicle, mechanic, parts used, dates, and workflow state |

## Installation

1. Copy the module folder into your Odoo `addons` path.
2. Restart the Odoo server.
3. Activate developer mode, go to **Apps**, click **Update Apps List**.
4. Search for "Fleet Maintenance Scheduler" and click **Install**.

## Usage

1. Go to **Fleet Maintenance → Configuration → Vehicles** to register vehicles and assign qualified mechanics to each.
2. Go to **Fleet Maintenance → Configuration → Parts** to set up your parts catalog.
3. Go to **Fleet Maintenance → Maintenance Jobs** to schedule a new job — select a vehicle, then a mechanic from that vehicle's qualified pool.
4. Move the job through its lifecycle using the header buttons (Confirm → Start Work → Mark Done), or cancel it at any point before completion.
5. Use **Print Job Sheet** to generate a PDF summary of the job.
6. Assign users to the **Fleet Manager** or **Fleet Mechanic** group (Settings → Users) to control what they can see and do.

## Security model in detail

| Group | Vehicles / Parts | Maintenance Jobs |
| --- | --- | --- |
| Fleet Manager | Full CRUD | Full CRUD, all jobs |
| Fleet Mechanic | No access | Read/update only their own assigned jobs; cannot create, delete, reassign, or reschedule |
| No group | No access | No access |

Field-level restriction for mechanics (preventing reassignment or rescheduling on jobs they're otherwise allowed to update) is enforced in Python via a `write()` override, not just the view layer — this closes a real gap where `ir.rule` alone only restricts *which records* a user can touch, not *which fields* on an allowed record.

## Folder structure

```
fleet_maintenance_scheduler/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── fleet_vehicle.py
│   ├── fleet_part.py
│   └── fleet_maintenance.py
├── security/
│   ├── fleet_security_groups.xml
│   ├── ir.model.access.csv
│   └── fleet_maintenance_rule.xml
├── report/
│   ├── fleet_maintenance_report_action.xml
│   └── fleet_maintenance_report_template.xml
└── views/
    ├── view_fleet_vehicle_form.xml
    ├── view_fleet_vehicle_list.xml
    ├── view_fleet_part_form.xml
    ├── view_fleet_part_list.xml
    ├── view_fleet_maintenance_form.xml
    ├── view_fleet_maintenance_list.xml
    ├── fleet_actions.xml
    └── fleet_menus.xml
```

## Requirements

- Odoo 19.0+
- No external Python dependencies beyond Odoo core

## Category

Fleet

## License

LGPL-3

## Author

Chike Chiagbaizu
