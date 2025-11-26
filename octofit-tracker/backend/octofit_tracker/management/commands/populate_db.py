from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting existing data...')
        
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        self.stdout.write('Creating teams...')
        
        # Create teams
        team_marvel = Team.objects.create(
            name='Team Marvel',
            members=['ironman', 'spiderman', 'blackwidow', 'thor', 'hulk']
        )
        
        team_dc = Team.objects.create(
            name='Team DC',
            members=['batman', 'superman', 'wonderwoman', 'flash', 'aquaman']
        )
        
        self.stdout.write('Creating users...')
        
        # Create Marvel users
        User.objects.create(username='ironman', email='tony@stark.com', team='Team Marvel')
        User.objects.create(username='spiderman', email='peter@parker.com', team='Team Marvel')
        User.objects.create(username='blackwidow', email='natasha@avengers.com', team='Team Marvel')
        User.objects.create(username='thor', email='thor@asgard.com', team='Team Marvel')
        User.objects.create(username='hulk', email='bruce@banner.com', team='Team Marvel')
        
        # Create DC users
        User.objects.create(username='batman', email='bruce@wayne.com', team='Team DC')
        User.objects.create(username='superman', email='clark@kent.com', team='Team DC')
        User.objects.create(username='wonderwoman', email='diana@themyscira.com', team='Team DC')
        User.objects.create(username='flash', email='barry@allen.com', team='Team DC')
        User.objects.create(username='aquaman', email='arthur@curry.com', team='Team DC')
        
        self.stdout.write('Creating activities...')
        
        # Create activities for Marvel heroes
        today = date.today()
        Activity.objects.create(user='ironman', type='Flying', duration=120, date=today - timedelta(days=1))
        Activity.objects.create(user='ironman', type='Strength Training', duration=60, date=today)
        Activity.objects.create(user='spiderman', type='Web Swinging', duration=90, date=today - timedelta(days=2))
        Activity.objects.create(user='spiderman', type='Cardio', duration=45, date=today)
        Activity.objects.create(user='blackwidow', type='Combat Training', duration=75, date=today - timedelta(days=1))
        Activity.objects.create(user='thor', type='Hammer Training', duration=100, date=today)
        Activity.objects.create(user='hulk', type='Smashing', duration=50, date=today - timedelta(days=3))
        
        # Create activities for DC heroes
        Activity.objects.create(user='batman', type='Martial Arts', duration=80, date=today - timedelta(days=1))
        Activity.objects.create(user='batman', type='Detective Work', duration=120, date=today)
        Activity.objects.create(user='superman', type='Flying', duration=150, date=today - timedelta(days=2))
        Activity.objects.create(user='wonderwoman', type='Sword Training', duration=70, date=today)
        Activity.objects.create(user='flash', type='Speed Running', duration=30, date=today - timedelta(days=1))
        Activity.objects.create(user='aquaman', type='Swimming', duration=90, date=today)
        
        self.stdout.write('Creating leaderboard...')
        
        # Create leaderboard entries
        Leaderboard.objects.create(team='Team Marvel', points=2500)
        Leaderboard.objects.create(team='Team DC', points=2450)
        
        self.stdout.write('Creating workouts...')
        
        # Create workout suggestions
        Workout.objects.create(
            name='Hero Strength Circuit',
            description='A circuit training routine focusing on strength and endurance. Includes push-ups, pull-ups, and weighted squats.',
            difficulty='Intermediate'
        )
        
        Workout.objects.create(
            name='Speed and Agility Drills',
            description='High-intensity interval training with sprints, ladder drills, and cone exercises to improve speed and agility.',
            difficulty='Advanced'
        )
        
        Workout.objects.create(
            name='Beginner Hero Training',
            description='A beginner-friendly full-body workout with bodyweight exercises. Includes squats, lunges, and planks.',
            difficulty='Beginner'
        )
        
        Workout.objects.create(
            name='Combat Conditioning',
            description='Mixed martial arts inspired workout combining cardio, strength, and flexibility training.',
            difficulty='Advanced'
        )
        
        Workout.objects.create(
            name='Cardio Blast',
            description='30-minute high-energy cardio session with jumping jacks, burpees, and mountain climbers.',
            difficulty='Intermediate'
        )
        
        Workout.objects.create(
            name='Power Lifting Session',
            description='Heavy compound lifts including deadlifts, bench press, and squats for maximum strength gains.',
            difficulty='Advanced'
        )
        
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with superhero test data!'))
        self.stdout.write(f'Created {User.objects.count()} users')
        self.stdout.write(f'Created {Team.objects.count()} teams')
        self.stdout.write(f'Created {Activity.objects.count()} activities')
        self.stdout.write(f'Created {Leaderboard.objects.count()} leaderboard entries')
        self.stdout.write(f'Created {Workout.objects.count()} workouts')
