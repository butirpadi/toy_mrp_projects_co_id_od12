# -*- coding: utf-8 -*-
from odoo import http

# class ToyMrpProjectsCoIdOd12(http.Controller):
#     @http.route('/toy_mrp_projects_co_id_od12/toy_mrp_projects_co_id_od12/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/toy_mrp_projects_co_id_od12/toy_mrp_projects_co_id_od12/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('toy_mrp_projects_co_id_od12.listing', {
#             'root': '/toy_mrp_projects_co_id_od12/toy_mrp_projects_co_id_od12',
#             'objects': http.request.env['toy_mrp_projects_co_id_od12.toy_mrp_projects_co_id_od12'].search([]),
#         })

#     @http.route('/toy_mrp_projects_co_id_od12/toy_mrp_projects_co_id_od12/objects/<model("toy_mrp_projects_co_id_od12.toy_mrp_projects_co_id_od12"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('toy_mrp_projects_co_id_od12.object', {
#             'object': obj
#         })