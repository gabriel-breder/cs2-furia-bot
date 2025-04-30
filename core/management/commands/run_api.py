from django.core.management.commands.runserver import Command as RunserverCommand
from django.core.management import call_command
import os

class Command(RunserverCommand):
    def handle(self, *args, **options):
        db_path = 'db.sqlite3'

        if os.path.exists(db_path):
            print("🧨 Apagando banco de dados existente...")
            os.remove(db_path)

        print("🛠️ Rodando migrações...")
        call_command('migrate')

        print("📦 Carregando dados iniciais...")
        call_command('loaddata', 'initial_data')

        print("🚀 Iniciando servidor...")
        super().handle(*args, **options)
