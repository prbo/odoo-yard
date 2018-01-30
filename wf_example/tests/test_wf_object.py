from openerp.tests import TransactionCase
from openerp.exceptions import ValidationError


class TestWfObject(TransactionCase):
    
    def setUp(self):
        super(TestWfObject, self).setUp()
        
        self.WfObject = self.env['wf.object']
        self.Department = self.env['hr.department']
        
        val_department = {
            'name': 'Test Dept',
        }
        
        self.department_id = self.Department.sudo().create(val_department)
        
        val_wf_object = {
            'total_estimate_price': 10000,
            'state': 'draft',
            'type_location': 'HO',
            'code': 'KPST',
            'department_id' : self.department_id.id
        }
        
        self.wfobject_id = self.WfObject.sudo().create(val_wf_object)
        
    def test_01_create_wf_object(self): 
        #check object creation
        self.assertTrue(self.wfobject_id.id, 'WfObject is not created')
    
    def test_02_default_val_wf_object(self):
        #check default value
        self.assertEqual(self.wfobject_id.state, 'draft', 'Default value for state is not set')
    
    def test_03_exceptions(self):
        #check state onchange
        with self.assertRaises(ValidationError):
            self.wfobject_id.onchange_state()
            
    def test_04_create_department(self):
        #check object creation
        self.assertTrue(self.department_id.id, 'Department is not created')
        
    def test_05_create_department_inside_wf_object(self):
        #check object creation
        self.assertTrue(self.wfobject_id.department_id, 'Department inside wf object is not created')
        
    def test_06_constrains(self):
        val_wf_object = {
            'total_estimate_price': 10000,
            'state': 'draft',
            'type_location': 'HO',
            'code': 'KPST',
            'department_id' : self.department_id.id
        }
        self.WfObject.sudo().create(val_wf_object)
        self.assertTrue(self.wfobject_id.check_duplicate_total_estimate_price(),'Already had total estimate price')
        
    def test_07_onchange(self):
        val_wf_object = {
            'total_estimate_price': 10000,
            'state': 'draft',
            'type_location': 'HO',
            'code': 'KPST',
            'department_id' : self.department_id.id
        }
        self.WfObject.sudo().create(val_wf_object)
        with self.assertRaises(ValidationError):
            self.wfobject_id._onchange_total_estimate_price()
            
    def test_08_compute(self):
        val_wf_object = {
            'total_estimate_price': 10000,
            'state': 'draft',
            'type_location': 'HO',
            'code': 'KPST',
            'department_id' : self.department_id.id
        }
        self.WfObject.sudo().create(val_wf_object)
        self.assertEqual(self.wfobject_id.total_estimate_price_times_two, self.wfobject_id.total_estimate_price*2, 'Default value for state is not set')