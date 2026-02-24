{
    'name': 'Company Enrichment',
    'summary': 'Company enrichment fields and keyword tags for contacts',
    'description': '''
        Adds enrichment fields to company contacts to mirror HubSpot-style
        company properties. Designed to match Studio field names (x_*) so
        production can replicate the same data model via Studio.

        Features:
        - Company Keywords taxonomy (tags under res.partner.category)
        - Target Account marker
        - Warehouse / receiving information fields
        - Social media URL fields
        - Company profile fields (year founded, employee count, revenue range)
    ''',
    'version': '19.0.1.0.0',
    'category': 'Sales/CRM',
    'license': 'LGPL-3',
    'author': 'CEM Tech',
    'depends': [
        'base',
        'contacts',
    ],
    'data': [
        'data/company_keyword_tags.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
