# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class AccountMove(models.Model):
	_inherit = 'account.move'

	#FUNCION PARA CAMBIAR DISPLAY NAME A NUM_VOU (ES PARTE DEL CAMPO)
	def _get_move_display_name(self, show_ref=False):
		self.ensure_one()
		name = ''
		if self.state == 'draft':
			name += {
				'out_invoice': _('Draft Invoice'),
				'out_refund': _('Draft Credit Note'),
				'in_invoice': _('Draft Bill'),
				'in_refund': _('Draft Vendor Credit Note'),
				'out_receipt': _('Draft Sales Receipt'),
				'in_receipt': _('Draft Purchase Receipt'),
				'entry': _('Draft Entry'),
			}[self.move_type]
			name += ' '
		if not self.num_vou or self.num_vou == '/':
			name += '(* %s)' % str(self.id)
		else:
			name += self.num_vou
		return name + (show_ref and self.ref and ' (%s%s)' % (self.ref[:50], '...' if len(self.ref) > 50 else '') or '')

	def action_post(self):
		res = super(AccountMove,self).action_post()
		for move in self:
			if move.num_vou == '/':
				sequence = move.journal_id.sequence_id_it
				if not sequence:
					raise UserError('Define una secuencia para el Diario escogido.')

				to_write = sequence.with_context(ir_sequence_date=move.date).next_by_id()
				move.write({'num_vou': to_write})
		return res
	
	def action_change_num_vou(self):
		for move in self:
			if move.state == 'draft':
				move.num_vou = "/"
			else:
				raise UserError("No puede alterar el nombre si no se encuentra en estado Borrador")

		return self.env['popup.it'].get_message('Se borro correctamente la secuencia.')