# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser
from openerp import models, fields, api

# class website_support_indonesia(models.Model):
#     _name = 'website_support_indonesia.website_support_indonesia'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class SchedulePersonInCharge(models.Model):

    _name = 'schedule.person.in.charge'
    _description = 'Schedule PIC'

    pic = fields.Many2one('res.users', 'Person In Charge')
    start_date = fields.Date('Start Date',required=True)
    end_date = fields.Date('End Date',required=True)
    
    @api.multi
    def _get_group_ids(self):
        return self.env['res.groups'].search([('category_id','=','Human Resources'),('name','not in',['employee','Employee'])])
    
    @api.multi
    @api.onchange()
    def _set_pic_hr(self):
        user_id = []
        group_ids = self._get_group_ids()
        for record in group_ids:
            for records in record.users:
                user_id.append(records.id)
            
        return{
               'domain':{
                         'pic':[('id','in',user_id)]
                         }
               }
    
    @api.one
    def send_mail_template(self, template_name):
        template = self.env.ref(template_name)
        self.env['mail.template'].browse(template.id).send_mail(self.id,force_send=True)

    @api.multi
    def database(self):
        for item in self:
            db = item.env.cr.dbname
        return db

    @api.multi
    def web_url(self):
        for item in self:
            web = item.env['ir.config_parameter'].sudo().get_param('web.base.url')
        return web

    @api.multi
    def email_model(self):
        for item in self:
            model = item._name
        return model
        
    @api.one
    def get_mail_recipient(self):
        mail_recipient = ''
        groups_ids = self._get_group_ids()
        for record in groups_ids:
            for records in record.users:
                mail_recipient = ('' if records.partner_id.email == False else records.partner_id.email  + ',') + mail_recipient 
        parser = HTMLParser()
        return parser.unescape(mail_recipient)    
        
    @api.model
    def create(self,vals):
        res = super(SchedulePersonInCharge,self).create(vals)
        res.send_mail_template('website_support_indonesia.new_pic_schedule')
        return res
    
    @api.multi
    def write(self,vals):
        self.send_mail_template('website_support_indonesia.update_pic_schedule')
        return super(SchedulePersonInCharge,self).write(vals)