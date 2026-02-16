
import csv, json
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)

    def handle(self, *args, **kwargs):
        with open(kwargs["csv_file"], newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                json.loads(row["cluster_subjects"])
        self.stdout.write(self.style.SUCCESS("Import validated"))
