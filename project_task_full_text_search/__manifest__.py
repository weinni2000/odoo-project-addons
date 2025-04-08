# -*- coding: utf-8 -*-
# © 2022 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Project Task Full Text Search',

    'author': 'Numigi',
    'maintainer': 'Numigi',
    'website': 'https://bit.ly/numigi-com',
    'license': 'LGPL-3',
    'category': 'Project',
    'depends': ['project'],
    'external_dependencies': {
        'python': ['unidecode'],
    },
    'data': [
        'views/project_task.xml',
    ],
    'installable': True,
}
