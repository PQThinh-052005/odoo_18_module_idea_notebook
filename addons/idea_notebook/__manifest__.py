{
    'name': 'Idea Notebook',
    'version': '18.0.1.0.0', 
    'category': 'Productivity',
    'summary': 'Quản lý ý tưởng',
    'description': '',
    'author': 'Thinh',
    'sequence': 1,
    'depends': ['base'],
    'data': [
        'security/idea_note_security.xml',
        'security/ir.model.access.csv',
        'views/idea_note_view.xml',
        'views/idea_note_menu.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'idea_notebook/static/src/**/*'
        ],
    },
    'installable': True,
    'application': True,
}