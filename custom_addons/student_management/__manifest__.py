{
    'name': 'Student Management',
    'version': '1.0',
    'summary': 'Manage students and their enrollments in courses',
    'description': 'A module to manage students, courses, and enrollments.',
    'author': 'tribeedd@gmail.com',
    'website': 'https://brookhouse@school.com',
    'category': 'Education',
    'depends': ['base'],
    'data':[
        'views/student_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}