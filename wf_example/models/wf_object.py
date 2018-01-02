from openerp import models, fields, api, exceptions

class wf_object(models.Model):
    _name = 'wf.object'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
        
    @api.multi
    def _get_user(self):
        user= self.env['res.users'].browse(self.env.uid)
        return user
    
    @api.multi
    def _get_employee(self):
        employee = self.env['hr.employee'].search([('user_id','=',self._get_user().id)])
        return employee
    
    @api.multi
    def _get_office_level_id(self):
        try:
            employee = self._get_employee().office_level_id.name
        except:
            raise exceptions.ValidationError('Office level Name Is Null')
        return employee
    
    @api.multi
    def _get_office_level_id_code(self):
        try:
            employee = self._get_employee().office_level_id.code
        except:
            raise exceptions.ValidationError('Office level Name Is Null')
        return employee
    
    state = fields.Selection([
        ('draft', "Draft"),
        ('approval7', "RO Head"),
        ('approval1', "Dept Head"),
        ('approval2', "Div Head"),
        ('budget', 'Budgeting'),
        ('technic', 'Technical'),
        ('finance', 'Finance'),
        ('director', 'Director'),
        ('president_director', 'President Director'),
        ('done', 'Done'),
        ('canceled', 'Canceled'),
        ('rejected', 'Rejected'),
    ], default='draft', track_visibility='onchange')
    total_estimate_price = fields.Float('Total Estimated Price')
    type_location = fields.Char('Location',default=_get_office_level_id,readonly = 1)
    code = fields.Char('code location',default=_get_office_level_id_code,readonly = 1)
    department_id = fields.Many2one('hr.department','Department')
    assigned_to = fields.Many2one('res.users', 'Approver')
    requester = fields.Many2one('res.users', 'Requester')
    
#     signal
    @api.multi
    def action_draft(self):
        self.state = 'draft'
        
    @api.multi
    def action_approval1(self):
        self.state = 'approval1'
    
    @api.multi
    def action_approval2(self):
        self.state = 'approval2'
        
    @api.multi
    def action_approval7(self):
        self.state = 'approval7'
        
    @api.multi
    def action_budget(self):
        self.state = 'budget'
        
    @api.multi
    def action_technic(self):
        self.state = 'technic'
    
    @api.multi
    def action_finance(self):
        self.state = 'finance'
    
    @api.multi
    def action_director(self):
        self.state = 'director'
    
    @api.multi
    def action_president_director(self):
        self.state = 'president_director'
        
    @api.multi
    def action_done(self):
        self.state = 'done'
        
    @api.multi
    def action_canceled(self):
        self.state = 'canceled'
        
    @api.multi
    def action_rejected(self):
        self.state = 'rejected'
    
#     function used in condition    
    @api.multi   
    def get_total_estimate_price(self):
        return self.total_estimate_price
    
    @api.multi
    def get_type_location(self):
        return self.type_location
    
    @api.multi
    def get_code(self):
        return self.code
    
    @api.multi
    def get_department_code(self):
        return self.department_id.code
    
    #Method get Pricing
    @api.multi
    def get_price_low(self):
        return float(1000000)
    
#     function to set approver
    @api.multi
    def get_dept_approver(self):
        return ''
    
    @api.multi
    def get_div_approver(self):
        return ''
    
    @api.multi
    def get_technical_approver(self):
        return ''
    
    @api.multi
    def get_budget_approver(self):
        return ''
    
    @api.multi
    def get_financial_approver(self):
        return ''
    
    @api.multi
    def get_director(self):
        return ''
    
    @api.multi
    def get_president_director(self):
        return ''