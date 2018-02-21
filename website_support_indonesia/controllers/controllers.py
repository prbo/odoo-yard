# -*- coding: utf-8 -*-
import werkzeug
import json
import base64
from random import randint
import os

import logging
import website_support
_logger = logging.getLogger(__name__)

import openerp.http as http
from openerp.http import request

from openerp.addons.website.models.website import slug


class SupportTicketController(http.Controller):

    @http.route('/support/ticket/inherit_submit', type="http", auth="user", website=True)
    def support_submit_ticket(self, **kw):
        """Let's public and registered user submit a support ticket"""
        person_name = ""
        if http.request.env.user.name != "Public user":
            person_name = http.request.env.user.name
        pic = http.request.env['schedule.person.in.charge'].sudo().search([],order = 'end_date desc',limit=1).pic    
        return http.request.render('website_support_indonesia.support_submit_ticket', {'categories': http.request.env['website.support.ticket.categories'].sudo().search([('type_view','=',False)]), 'person_name': person_name, 'email': http.request.env.user.email, 'pic':pic})

    
class RestrictSupportTicketController(website_support.controllers.main.SupportTicketController):
 
    @http.route('/support/help', auth="user")
    def support_help(self, **kw):
        """Displays all help groups and thier child help pages"""
        return super(RestrictSupportTicketController, self).support_help()
