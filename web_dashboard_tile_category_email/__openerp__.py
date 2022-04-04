# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Email Dashboard Tile Value",
    "version": "8.0.2.0.0",
    "category": "web",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        "email_template",
        "web_dashboard_tile_category",
    ],
    "data": [
        "views/tile_category_views.xml",
    ],
}
