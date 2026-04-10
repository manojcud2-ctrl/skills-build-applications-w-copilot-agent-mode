from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes team')
        dc = Team.objects.create(name='DC', description='DC superheroes team')

        # Users
        users = [
            User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel.name),
            User.objects.create(email='steve@rogers.com', name='Steve Rogers', team=marvel.name),
            User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc.name),
            User.objects.create(email='clark@kent.com', name='Clark Kent', team=dc.name),
        ]

        # Activities
        Activity.objects.create(user=users[0].name, type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1].name, type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2].name, type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3].name, type='Yoga', duration=40, date=timezone.now().date())

        # Leaderboard
        Leaderboard.objects.create(user=users[0].name, points=100, rank=1)
        Leaderboard.objects.create(user=users[1].name, points=90, rank=2)
        Leaderboard.objects.create(user=users[2].name, points=80, rank=3)
        Leaderboard.objects.create(user=users[3].name, points=70, rank=4)

        # Workouts
        Workout.objects.create(name='Full Body Blast', description='A full body workout for all levels', difficulty='Medium')
        Workout.objects.create(name='Cardio Burn', description='High intensity cardio session', difficulty='Hard')
        Workout.objects.create(name='Strength Builder', description='Strength training for beginners', difficulty='Easy')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
