# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Web Tile Dashboard Category",
    "version": "8.0.1.2.0",
    "category": "web",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        "web_dashboard_tile",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/tile_category_views.xml",
        "menu.xml",
    ],
}
