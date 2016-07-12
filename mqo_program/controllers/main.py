# -*- coding: utf-8 -*-
import werkzeug
import werkzeug.urls

from openerp import http, SUPERUSER_ID
from openerp.http import request
from openerp.tools.translate import _

class ProgramsList(http.Controller):
    @http.route('/programs/all', type='http', auth='public', website=True)
    def listAllPrograms(self):
        return self.listPrograms('all')

    @http.route('/programs/individuals', type='http', auth='public', website=True)
    def listIndividualPrograms(self):
        return self.listPrograms('individuals')
    
    @http.route('/programs/organisations', type='http', auth='public', website=True)
    def listOrganisationalPrograms(self):
        return self.listPrograms('organisations')

   
    def listPrograms(self, category):
        if category=="all": 
            domain = []
            listname = "All programs"
        elif category=="individuals":
            domain = [('individual','=','true')]
            listname = "Programs for individuals"
        elif category=="organisations":
            domain = [('organisational','=','true')]
            listname = "Programs for organisations"
        else:
            return request.website.render('website.404');
        programs = request.env['mqo.program'].search(domain)
        if programs:
            return request.website.render('mqo_program.list', {
                'programs': programs,
                'category': category,
                'listname': listname 
            })
        else:
            return request.website.render('website.404');

