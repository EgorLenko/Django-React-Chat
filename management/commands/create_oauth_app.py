# from django.core.management.base import BaseCommand
# from oauth2_provider.models import Application
#
#
# class Command(BaseCommand):
#     help = 'Create an OAuth2 application instance'
#
#     def handle(self, *args, **options):
#         app = Application.objects.create(
#             name='Oauth2App',
#             client_type=Application.CLIENT_CONFIDENTIAL,
#             authorization_grant_type=Application.GRANT_AUTHORIZATION_CODE,
#             redirect_uris='http://localhost:8000/callback',
#         )
#         self.stdout.write(self.style.SUCCESS(f'Successfully created OAuth2 application instance: {app}'))
