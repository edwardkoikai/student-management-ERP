rom odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class student(models.Model):
    _name = 'student.management'
    _description = 'Student Management'

    name = fields.Char(string="Student Name", required=True)
    registration_number = fields.Char(string="Registration Number")
    age = fields.Integer(string="Age")
    date_of_birth = fields.Char(string="Date_of_Birth")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string = "Gender", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    address = fields.Char(string="Address") 
    profile_photo = fields.Binary(string="Student Image", attachment=True)
    year_of_study = fields.Selection([
       ('year one', 'Year One'),
       ('year two', 'Year Two'),
       ('year three', 'Year Three'),
       ('year four', 'Year Four'),
    ], string="Year of Study")
    
    # Guardian Details
    guardian_name = fields.Char(string="Guardian Name")
    guardian_phone = fields.Char(string="Guardian Phone")
    guardian_email = fields.Char(string="Guardian Email")

    @api.constrains('age')
    def _check_age(self):
        for record in self:
            if record.age and (record.age < 1 or record.age > 120):
                raise ValidationError("Age must be between 1 and 120")

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if record.email and not re.match(r"[^@]+@[^@]+\.[^@]+", record.email):
                raise ValidationError("Invalid email format")

    @api.constrains('phone')
    def _check_phone(self):
        for record in self:
            if record.phone and not record.phone.isdigit():
                raise ValidationError("Phone number must contain only digits")
