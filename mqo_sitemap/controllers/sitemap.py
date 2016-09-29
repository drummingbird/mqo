# -*- coding: utf-8 -*-
import cStringIO
import datetime
from itertools import islice

import logging
import re

import werkzeug.utils
import urllib2
import werkzeug.wrappers
import base64

import openerp
from openerp.addons.web import http
from openerp.http import request, STATIC_CACHE

from openerp.addons.website.controllers.main import Website

_logger = logging.getLogger(__name__)

# Completely arbitrary limits
LOC_PER_SITEMAP = 45000
SITEMAP_CACHE_TIME = datetime.timedelta(hours=12)

class MQO_Sitemap(Website):
    # Overwrite existing controller.
    @http.route('/sitemap.xml', type='http', auth="public", website=True)
    def sitemap_xml_index(self):
        cr, uid, context = request.cr, openerp.SUPERUSER_ID, request.context
        ira = request.registry['ir.attachment']
        iuv = request.registry['ir.ui.view']
        hostname = request.httprequest.url_root.replace("http://","").replace("https://","").replace(":","-").replace("/","")
        mimetype ='application/xml;charset=utf-8'
        content = None

        def create_sitemap(url, content):
            ira.create(cr, uid, dict(
                datas=content.encode('base64'),
                mimetype=mimetype,
                type='binary',
                name=url,
                url=url,
            ), context=context)

        sitemap = ira.search_read(cr, uid, [('url', '=' , '/' + hostname + '-sitemap.xml'), ('type', '=', 'binary')], ('datas', 'create_date'), context=context)
        if sitemap:
            # Check if stored version is still valid
            server_format = openerp.tools.misc.DEFAULT_SERVER_DATETIME_FORMAT
            create_date = datetime.datetime.strptime(sitemap[0]['create_date'], server_format)
            delta = datetime.datetime.now() - create_date
            if delta < SITEMAP_CACHE_TIME:
                content = sitemap[0]['datas'].decode('base64')

        if not content:
            # Remove all sitemaps in ir.attachments as we're going to regenerated them
            sitemap_ids = ira.search(cr, uid, [('url', '=like' , '/' + hostname + '-sitemap%.xml'), ('type', '=', 'binary')], context=context)
            if sitemap_ids:
                ira.unlink(cr, uid, sitemap_ids, context=context)

            pages = 0
            first_page = None
            locs = request.website.sudo(user=request.website.user_id.id).enumerate_pages()
            while True:
                start = pages * LOC_PER_SITEMAP
                values = {
                    'locs': islice(locs, start, start + LOC_PER_SITEMAP),
                    'url_root': request.httprequest.url_root[:-1],
                }
                urls = iuv.render(cr, uid, 'website.sitemap_locs', values, context=context)
                if urls.strip():
                    page = iuv.render(cr, uid, 'website.sitemap_xml', dict(content=urls), context=context)
                    if not first_page:
                        first_page = page
                    pages += 1
                    create_sitemap('/' + hostname + '-sitemap-%d.xml' % pages, page)
                else:
                    break
            if not pages:
                return request.not_found()
            elif pages == 1:
                content = first_page
            else:
                # Sitemaps must be split in several smaller files with a sitemap index
                content = iuv.render(cr, uid, 'website.sitemap_index_xml', dict(
                    pages=range(1, pages + 1),
                    url_root=request.httprequest.url_root,
                ), context=context)
            create_sitemap('/' + hostname + '-sitemap.xml', content)

        return request.make_response(content, [('Content-Type', mimetype)])

    