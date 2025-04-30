from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connection
import os

class Command(BaseCommand):
    help = 'Reseta o banco de dados e popula com dados iniciais'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Resetando o banco de dados...'))

        # Dropa todas as tabelas (somente se usar SQLite)
        if 'sqlite3' in connection.settings_dict['ENGINE']:
            db_path = connection.settings_dict['NAME']
            if os.path.exists(db_path):
                os.remove(db_path)
                self.stdout.write(self.style.SUCCESS('Banco SQLite apagado com sucesso.'))

        # Recria o banco de dados
        call_command('migrate')

        # Popula com fixtures ou lógica customizada
        call_command('loaddata', 'initial_data.json')  # ou um script personalizado

        self.stdout.write(self.style.SUCCESS('Banco de dados resetado e populado.'))
