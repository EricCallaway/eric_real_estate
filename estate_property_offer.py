# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate property offer information'

    price = fields.Float(string="Price")
    status = fields.Selection([
        ('accepted','Accepted'),
        ('refused','Refused')
    ], copy=False)
    partner_id = fields.Many2one('res.partner', string="Partner ID")
    property_id = fields.Many2one('estate.property', string="Property ID")

    

   