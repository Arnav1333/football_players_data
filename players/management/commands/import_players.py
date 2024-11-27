import pandas as pd
from django.core.management.base import BaseCommand
from players.models import Player

class Command(BaseCommand):
    help = 'Import players from a CSV file'

    def handle(self, *args, **kwargs):
        # Path to your CSV file
        file_path = 'top5-players.csv'

        # Read the dataset
        data = pd.read_csv(file_path)

        
        for _, row in data.iterrows():
            Player.objects.create(
                name=row['Player'],
                nationality=row['Nation'],
                club=row['Squad'],
                competition=row['Comp']
            )

        self.stdout.write(self.style.SUCCESS('Data imported successfully!'))
