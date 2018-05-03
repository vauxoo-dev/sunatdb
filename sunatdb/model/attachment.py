# -*- coding: utf-8 -*-
# Copyright 2017 Vauxoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class IrsAttachment(models.Model):
    _name = 'sunatdb.attachment'

    db_check_update = fields.Boolean("SUNAT Padron check update",
                                     default=False, copy=False)
    db_zip = fields.Binary(string="File to store the SUNAT RUC database")
