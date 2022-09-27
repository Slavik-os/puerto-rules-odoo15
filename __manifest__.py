{
    'name' : 'Puerto application',
    'version' : '1.0',
    'summary': 'Puerto',
    'sequence': 1,
    'description': """
        Puerto transit v1.0
    """,
    'category': 'Puerto',
    'depends': ['base', 'mail'],
    'data': [
             'security/ir.model.access.csv',
              # ~~~~~~~~~~~~~~~~~~~~~~~~~
              #  Folders view
              # ~~~~~~~~~~~~~~~~~~~~~~~~~
             'views/folders/folders_action_view.xml',
             'views/folders/folders_form_view.xml',
             'views/folders/folders_tree_view.xml',
             'views/folders/folders_search_view.xml',
             # ~~~~~~~~~~~~~~~~~~~~~~~~~
             #  Rules view
             # ~~~~~~~~~~~~~~~~~~~~~~~~~
             'views/rules/rules_action_view.xml',
             'views/rules/rules_form_view.xml',
             # ~~~~~~~~~~~~~~~~~~~~~~~~~
             #  Attachments view
             # ~~~~~~~~~~~~~~~~~~~~~~~~~
             'views/attachments/attachments_tree_view.xml',
             # ~~~~~~~~~~~~~~~~~~~~~~~~~
             #  Invoice list view
             # ~~~~~~~~~~~~~~~~~~~~~~~~~
             'views/invoice_list/invoice_list_form_view.xml',
             'views/menu.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
