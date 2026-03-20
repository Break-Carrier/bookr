# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from backoffice.models import Auteur, Livre, LivreType, LivreStatus


class Command(BaseCommand):
    help = 'Peuple la base de données avec les données de test'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('=== Création des données ===\n'))

        # 1. Types de livres
        self.stdout.write('1. Types de livres...')
        genre_roman, _ = LivreType.objects.get_or_create(genre="roman")
        genre_nouvelle, _ = LivreType.objects.get_or_create(genre="nouvelle")
        genre_polar, _ = LivreType.objects.get_or_create(genre="polar")
        genre_biographie, _ = LivreType.objects.get_or_create(genre="biographie")
        self.stdout.write('   OK\n')

        # 2. Statuts
        self.stdout.write('2. Statuts...')
        status_publie, _ = LivreStatus.objects.get_or_create(status="toujours publié")
        status_arret, _ = LivreStatus.objects.get_or_create(status="en arrêt de commercialisation")
        status_reimpression, _ = LivreStatus.objects.get_or_create(status="réimpression")
        self.stdout.write('   OK\n')

        # 3. Auteurs
        self.stdout.write('3. Auteurs...')
        hugo, created = Auteur.objects.get_or_create(
            prenom="Victor", nom="Hugo",
            defaults={'nationalite': "Française"}
        )
        self.stdout.write(f"   - Victor Hugo {'créé' if created else 'existe déjà'}")

        flaubert, created = Auteur.objects.get_or_create(
            prenom="Gustave", nom="Flaubert",
            defaults={'nationalite': "Française"}
        )
        self.stdout.write(f"   - Gustave Flaubert {'créé' if created else 'existe déjà'}")

        balzac, created = Auteur.objects.get_or_create(
            prenom="Honoré de", nom="Balzac",
            defaults={'nationalite': "Française"}
        )
        self.stdout.write(f"   - Honoré de Balzac {'créé' if created else 'existe déjà'}\n")

        # 4. Livres
        self.stdout.write('4. Livres...')

        livre1, created = Livre.objects.get_or_create(
            nom="Les Misérables",
            defaults={'prix': 8, 'auteur': hugo, 'livre_type': genre_roman, 'livre_status': status_publie}
        )
        self.stdout.write(f"   - 'Les Misérables' {'créé' if created else 'existe déjà'}")

        livre2, created = Livre.objects.get_or_create(
            nom="Madame Bovary",
            defaults={'prix': 7, 'auteur': flaubert, 'livre_type': genre_roman, 'livre_status': status_publie}
        )
        self.stdout.write(f"   - 'Madame Bovary' {'créé' if created else 'existe déjà'}")

        livre3, created = Livre.objects.get_or_create(
            nom="Le Père Goriot",
            defaults={'prix': 11, 'auteur': balzac, 'livre_type': genre_roman, 'livre_status': status_publie}
        )
        self.stdout.write(f"   - 'Le Père Goriot' {'créé' if created else 'existe déjà'}\n")

        self.stdout.write(self.style.SUCCESS('=== Données créées avec succès! ==='))
        self.stdout.write(f"Livres: {Livre.objects.count()} | Auteurs: {Auteur.objects.count()} | Types: {LivreType.objects.count()} | Statuts: {LivreStatus.objects.count()}")
