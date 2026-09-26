{
    "name": "School Management",
    "version": "19.0.1.0.0",
    "summary": "School Management Software",
    "description": """
        School Management Application
        =============================

        Manage students, teachers, classes,
        subjects, attendance and other school operations.
    """,
    "author": "Bayazid Hasan",
    "category": "Education",
    "license": "LGPL-3",

    "depends": [
        "base",
        "portal"
    ],

    'data': [
        "security/ir.model.access.csv",
        'security/student_security.xml',
        "views/student_information_views.xml",
        'views/class_information_views.xml',
    ],

    "installable": True,
    "application": True,
}