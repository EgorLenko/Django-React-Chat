from django.core.management.base import BaseCommand

import faker
from faker.providers import python, person, phone_number, profile, job
import django

django.setup()

from ChatnGo.models import UserProfile, ChatRoom, Message


class Command(BaseCommand):
    help = 'Create a fake data to fill database for testing purposes'

    def handle(self, *args, **options):
        fake = faker.Faker()
        try:

            fake.add_provider(python)
            fake.add_provider(person)
            fake.add_provider(phone_number)
            fake.add_provider(profile)
            fake.add_provider(job)
        except (Exception,) as exc:
            self.stdout.write(self.style.error('An error occurred while configuring faker library'))
            self.stdout.write(self.style.error(f'Error -> {exc}'))

        bulk_user_list = []
        bulk_message_list = []
        try:
            for _ in range(20):
                bulk_user_list.append(
                    UserProfile(first_name=fake.first_name(), last_name=fake.last_name(), phone=fake.phone_number(),
                                password=fake.pystr(), email=fake.simple_profile().get('mail'),
                                username=fake.simple_profile().get('username')))
            UserProfile.objects.bulk_create(bulk_user_list)

            for _ in range(5):
                obj = ChatRoom.objects.create(name=fake.job())
                obj.members.set(UserProfile.objects.all())

            for _ in range(40):
                bulk_message_list.append(
                    Message(user=UserProfile.objects.order_by("?").first(), room=ChatRoom.objects.order_by("?").first(),
                            content=fake.pystr(max_chars=100)))
            Message.objects.bulk_create(bulk_message_list)
        except (Exception,) as exc:
            self.stdout.write(self.style.ERROR('An error occurred while creating fake data'))
            self.stdout.write(self.style.ERROR(f'Error -> {exc}'))

        self.stdout.write(self.style.SUCCESS('Successfully create fake data'))
