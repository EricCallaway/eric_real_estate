# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate property information.'

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, string="Available From")
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2, string="Bedrooms")
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(string="Garden Area (sqm)")
    garden_orientation = fields.Selection([
        ('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West')
    ], default="north")
    active = fields.Boolean(default=True)
    state = fields.Selection([
        ('new','New'),
        ('offer_recieved','Offer Received'),
        ('offer_accepted','Offer Accepted'),
        ('sold','Sold'),
        ('cancelled','Cancelled')
    ], required=True, copy=False, default="new")
    
