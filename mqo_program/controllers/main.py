# -*- coding: utf-8 -*-
import werkzeug
import werkzeug.urls

from openerp import http, SUPERUSER_ID
from openerp.http import request
from openerp.tools.translate import _

class ProgramsList(http.Controller):
    @http.route(['/programs/all',
                 '/programs/all/<model("mqo.benefit"):benefit>'],
                type='http', auth='public', website=True)
    def listAllPrograms(self, benefit=None):
        return self.listPrograms('all', benefit)

    @http.route(['/programs/individuals',
                 '/programs/individuals/<model("mqo.benefit"):benefit>'],
                type='http', auth='public', website=True)
    def listIndividualPrograms(self, benefit=None):
        return self.listPrograms('individuals', benefit)
    
    @http.route(['/programs/organisations',
                 '/programs/organisations/<model("mqo.benefit"):benefit>'],
                type='http', auth='public', website=True)
    def listOrganisationalPrograms(self, benefit=None):
        return self.listPrograms('organisations', benefit)

   
    def listPrograms(self, category, benefit=None):
        if category=="all": 
            domain = []
            if benefit:
                domain = [('benefits.benefit.id','=', benefit.id)]
            listname = "All programs"
        elif category=="individuals":
            domain = [('individual','=','true')]
            if benefit:
                domain = ['&',('individual','=','true'), ('benefits.benefit.id','=',benefit.id), ('benefits.benefit.category','=','individual')]
            listname = "Programs for individuals"
        elif category=="organisations":
            domain = [('organisational','=','true')]
            if benefit:
                domain = ['&', ('organisational','=','true'), ('benefits.benefit.id','=',benefit.id), ('benefits.benefit.category','!=','individual')]
            listname = "Programs for organisations"
        else:
            return request.website.render('website.404');
        programs = request.env['mqo.program'].search(domain)
        if programs:
            return request.website.render('mqo_program.list', {
                'programs': programs,
                'category': category,
                'benefit': benefit,
                'listname': listname 
            })
        else:
            return request.website.render('website.404');

class SolutionsList(http.Controller):
    @http.route('/solutions/all', type='http', auth='public', website=True)
    def listAllSolutions(self):
        return self.listSolutions('all')

    @http.route('/solutions/individuals', type='http', auth='public', website=True)
    def listIndividualSolutions(self):
        return self.listSolutions('individuals')
    
    @http.route('/solutions/organisations', type='http', auth='public', website=True)
    def listOrganisationalSolutions(self):
        return self.listSolutions('organisations')

   
    def listSolutions(self, category):
        if category=="all": 
            domain = []
            listname = "All solutions"
        elif category=="individuals":
            domain = [('program_links.program.individual','=','true'), ('category','=','individual')]
            listname = "Solutions for individuals"
        elif category=="organisations":
            domain = [('program_links.program.organisational','=','true'), ('category','!=','individual')]
            listname = "Solutions for organisations"
        else:
            return request.website.render('website.404');
        benefits = request.env['mqo.benefit'].search(domain)
        if benefits:
            return request.website.render('mqo_program.solutions', {
                'benefits': benefits,
                'category': category,
                'listname': listname 
            })
        else:
            return request.website.render('website.404');

