import json
import logging
import werkzeug
import werkzeug.utils
from datetime import datetime
from math import ceil

from openerp import SUPERUSER_ID
from openerp.addons.web import http
from openerp.addons.web.http import request
from openerp.tools.misc import DEFAULT_SERVER_DATETIME_FORMAT as DTF, ustr

from openerp.addons.survey.controllers.main import WebsiteSurvey

_logger = logging.getLogger(__name__)

class Mqo_invite_only(WebsiteSurvey):
    # Survey start
    @http.route(['/survey/start/<model("survey.survey"):survey>',
                 '/survey/start/<model("survey.survey"):survey>/<string:token>'],
                type='http', auth='public', website=True)
    def start_survey(self, survey, token=None, **post):
        if survey.invite_only:
            if not token or token == "phantom":
                return request.website.render("website.403")
        return super(Mqo_invite_only, self).start_survey(survey, token, **post)
    