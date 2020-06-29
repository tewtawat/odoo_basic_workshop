from odoo import models, fields


class Slot(models.Model):
    _name = 'plot.slot'
    _description = 'Plot Slot'

    name = fields.Char(string='Slot number')

    plot_id = fields.Many2one(
        comodel_name='plot',
        string="Plot"
    )
