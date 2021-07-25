# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Estate property tag information'

    name = fields.Char(required=True)