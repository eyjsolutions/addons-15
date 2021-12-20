# -*- coding: utf-8 -*-
# © 2008-2016 Camptocamp
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Peruvian Currency Rate Update",
    "version": "1.0",
    "author": "ITGRUPO",
    "category": "account",
    "depends": ['account','popup_it','account_fields_it'],
    "data": [
        "security/ir.model.access.csv",
        "data/cron.xml",
        "views/res_currency_view.xml",
        "wizard/currency_rate_update_wizard_view.xml",
        "wizard/currency_rate_update_now.xml",
        "views/menu_views.xml"
    ],
    'installable': True
}
