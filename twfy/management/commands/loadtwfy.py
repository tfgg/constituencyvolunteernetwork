import sys
import simplejson as json
from optparse import make_option
import urllib

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from twfy.models import SurveyInvite
from ynmp.models import Candidacy

from settings import TWFY_SECRET_KEY

class Command(BaseCommand):
    option_list =  BaseCommand.option_list + (
        make_option('--file', '-f', dest='filename',
                    action="store",
                    help="JSON file to load from"),
        make_option('--url', '-u', dest='url',
                    action="store",
                    help="JSON url to load from"),
        )
    help = "Load data from TWFY to local database"
                        
    def handle(self, *args, **options):
        filename = options.get('filename', None)
        url = options.get('url', None)
        if filename:
            data = open(filename, "r").read()
        elif url:
            url += "?secret=" + TWFY_SECRET_KEY
            resp = urllib.urlopen(url)
            _, data = resp.headers, resp.read()
        else:
            raise CommandError("Must specify one of url or file")
        try:
            parsed = json.loads(data)
        except ValueError:
            print "Problem parsing", data
            sys.exit(1)
        for invite in parsed:
            ynmp_id = str(invite['ynmp_id'])
            try:
                candidacy = Candidacy.objects\
                            .get(ynmp_id=ynmp_id)            
                surveyinvite, _ = SurveyInvite.objects\
                                  .get_or_create(ynmp_id=ynmp_id,
                                                 candidacy=candidacy)
                surveyinvite.emailed = invite['survey_invite_emailed']
                surveyinvite.filled_in = invite['survey_filled_in']
                surveyinvite.candidacy = candidacy
                surveyinvite.survey_token = invite['survey_token']
                surveyinvite.save()
            except Candidacy.DoesNotExist:
                continue
