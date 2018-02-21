from openerp import api, fields, models
from openerp import tools
from HTMLParser import HTMLParser
from random import randint
from datetime import datetime, timedelta
import logging
from openerp.api import onchange
from reportlab.lib.pdfencrypt import computeO
_logger = logging.getLogger(__name__)

class InheritWebsiteSupportTicket(models.Model):
    _inherit = 'website.support.ticket'
    
    category = fields.Many2one('website.support.ticket.categories', string="Category", track_visibility='onchange', domain=[('type_view','=',False)])
    overdue_date = fields.Datetime('Overdue Date', compute='_get_ovderdue_date')
    
    @api.multi
    @api.depends('create_date')
    def _get_ovderdue_date(self):
        for item in self:
            sla = self.env['website.support.ticket.categories'].search([('id','=',item.category.id)]).sla
            datetime_object = datetime.strptime(item.create_date, '%Y-%m-%d %H:%M:%S')
            item.overdue_date = datetime_object + timedelta(sla)