# -*- encoding: utf-8 -*-
{
	'name': 'Generacion de Secuencias para Diarios',
	'category': 'account',
	'author': 'ITGRUPO',
	'depends': ['account_fields_it'],
	'version': '1.0',
	'description':"""
	Generacion de Secuencias para Diarios
	""",
	'auto_install': False,
	'demo': [],
	'data':	[
			'security/ir.model.access.csv',
			'views/account_journal.xml',
			'wizards/account_sequence_journal_wizard.xml',
			'wizards/sequence_wizard.xml'
			],
	'installable': True
}
