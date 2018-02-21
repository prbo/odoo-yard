from openerp import api, fields, models
from openerp import tools
from HTMLParser import HTMLParser
from random import randint
import logging
from openerp.api import onchange
_logger = logging.getLogger(__name__)

class InheritWebsiteSupportTicketCategories(models.Model):
    _inherit = 'website.support.ticket.categories'
    _description = 'Ticket Categories'
    rec_name = 'complete_name'
    
    parent_id = fields.Many2one('website.support.ticket.categories', string='Category Name Parent', ondelete='restrict', domain=[('type_view','=',1)])
    child_ids = fields.One2many('website.support.ticket.categories', 'parent_id', "Child Activities")
    complete_name = fields.Char(translate=True, string='Name', compute='_get_complete_name')
    type_view = fields.Boolean('Type View')
    sla = fields.Integer('SLA')
    
    @api.one
    @api.depends('name','parent_id')
    def _get_complete_name(self):
        if self.parent_id:
            self.complete_name = self.parent_id.name + ' / ' + self.name
        else:
            self.complete_name = self.name