# © 2023 - Today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/LGPL).

{
    "name": "Project Group Create",
    "author": "Numigi",
    "maintainer": "Numigi",
    'license': 'LGPL-3',
    "website": "https://bit.ly/numigi-com",
    "category": "Project Management",
    "summary": "Add a group that manage creation rights on project",
    "depends": ["project", "base_extended_security"],
    "data": [
        "security/res_groups.xml",
        "security/extended_security_rule.xml",
    ],
    "installable": True,
}
