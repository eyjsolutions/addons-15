# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AccountMove(models.Model):
	_inherit = 'account.move'

	def action_post(self):
		for move in self:
			if move.move_type in ['out_invoice', 'in_invoice', 'out_refund', 'in_refund']:
				for line in move.line_ids:
					#if not line.is_advance_check:
					line.type_document_id = move.l10n_latam_document_type_id.id or None
					line.nro_comp = move.ref or None
		return super(AccountMove,self).action_post()