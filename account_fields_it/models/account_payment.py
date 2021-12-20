# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class AccountPayment(models.Model):
	_inherit = 'account.payment'

	cash_flow_id = fields.Many2one('account.cash.flow',string='Flujo de Caja')
	catalog_payment_id = fields.Many2one('einvoice.catalog.payment',string='Medio de Pago')
	type_doc_cash_id = fields.Many2one('l10n_latam.document.type',string='Tipo Documento Caja')
	cash_nro_comp = fields.Char(string='Nro. de Op. Caja',size=42)
	type_document_id = fields.Many2one('l10n_latam.document.type',string='Tipo Documento')
	nro_comp = fields.Char(string='Nro. Comprobante')
	is_personalized_change = fields.Boolean(string='T.C. Personalizado',default=False)
	type_change = fields.Float(string='Tipo de Cambio',digits=(12,4),default=1)
	manual_batch_payment_id = fields.Many2one('account.batch.payment',string='Lote de Pago')
	amount_mn = fields.Float(string='Monto MN',digits=(12,2),compute='_calculate_amounts')
	amount_me = fields.Monetary(string='Monto ME',digits=(12,2),compute='_calculate_amounts')
	

	@api.depends('amount',
				'type_change',
				'currency_id')
	def _calculate_amounts(self):
		for payment in self:
			payment.amount_mn = (payment.amount * payment.type_change) if payment.currency_id != payment.company_id.currency_id else payment.amount
			payment.amount_me = payment.amount if payment.currency_id != payment.company_id.currency_id else None
class AccountPaymentRegister(models.TransientModel):
	_inherit = 'account.payment.register'

	cash_flow_id = fields.Many2one('account.cash.flow',string='Flujo de Caja')
	catalog_payment_id = fields.Many2one('einvoice.catalog.payment',string='Medio de Pago')
	type_doc_cash_id = fields.Many2one('l10n_latam.document.type',string='Tipo Documento Caja')
	cash_nro_comp = fields.Char(string='Nro. de Op. Caja',size=42)
	type_document_id = fields.Many2one('l10n_latam.document.type',string='Tipo Documento')
	nro_comp = fields.Char(string='Nro. Comprobante')
	is_personalized_change = fields.Boolean(string='T.C. Personalizado',default=False)
	type_change = fields.Float(string='Tipo de Cambio',digits=(12,4),default=1)
	manual_batch_payment_id = fields.Many2one('account.batch.payment',string='Lote de Pago')