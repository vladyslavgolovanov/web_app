from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from faker import Faker
# from polls.models import Question as Poll

f = Faker()


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='+', type=int)

    def handle(self, *args, **options):
        for _ in range(options["count"][0]):
            User.objects.create_user(
                username=f.user_name(),
                email=f.email(),
                password=f.password())