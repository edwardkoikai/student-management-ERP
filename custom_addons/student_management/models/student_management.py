from odoo import models, fields, api

class Student(models.Model):
    _name = 'student.management'
    _description = 'Student Management'

    name = fields.Char(string='Name', required=True)
    registration_number = fields.Char(string='Registration Number', required=True)
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Text(string='Address')
    profile_photo = fields.Binary(string='Profile Photo')
    year_of_study = fields.Integer(string='Year of Study')
    enrollment_ids = fields.One2many('student.enrollment', 'student_id', string='Enrollments')

    @api.depends('date_of_birth')
    def _compute_age(self):
        today = fields.Date.today()
        for student in self:
            if student.date_of_birth:
                student.age = today.year - student.date_of_birth.year
            else:
                student.age = 0


class Course(models.Model):
    _name = 'course.management'
    _description = 'Course Management'

    name = fields.Char(string='Course Name', required=True)
    code = fields.Char(string='Course Code', required=True)
    description = fields.Text(string='Description')
    enrollment_ids = fields.One2many('student.enrollment', 'course_id', string='Enrollments')


class Enrollment(models.Model):
    _name = 'student.enrollment'
    _description = 'Student Enrollment'

    student_id = fields.Many2one('student.management', string='Student', required=True)
    course_id = fields.Many2one('course.management', string='Course', required=True)
    enrollment_date = fields.Date(string='Enrollment Date', default=fields.Date.today)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('enrolled', 'Enrolled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft')