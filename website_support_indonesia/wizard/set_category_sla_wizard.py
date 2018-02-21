# -*- coding: utf-8 -*-

from openerp import models, fields, api
from datetime import datetime, timedelta
from dateutil import relativedelta
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT as DF
from openerp.tools.translate import _
from openerp import tools
from openerp.exceptions import Warning

class CategorySla(models.TransientModel):
    _name = 'category.sla'
    _description = 'Estate Common Report'

    sla = fields.Integer('SLA')
    
    @api.multi
    def set_category_sla(self):
        self.ensure_one()
        self.env['website.support.ticket.categories'].search([('type_view','=',False)]).write({'sla':self.sla})