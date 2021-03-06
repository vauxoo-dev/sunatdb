# coding: utf-8
#
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2014 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info@vauxoo.com
#
#    Coded by: Edgard Pimentel (pimentelrojas@gmail.com)
#              Luis Torres (luis_t@vauxoo.com)
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
{
    "name": "Consulting Partners by RUC",
    "version": "9.0.1.0",
    "author": "Vauxoo",
    "category": "SUNATDB\\Peru",
    "website": "http://www.vauxoo.com/",
    "license": "",
    "depends": [
        "base_vat",
        "auth_oauth",
    ],
    "demo": [],
    "data": [
        'data/ir_cron.xml',
        'view/res_users_view.xml',
    ],
    "test": [],
    "js": [],
    "css": [],
    "qweb": [],
    "installable": True,
    "auto_install": False
}
