# -*- coding: utf-8 -*-
"""
Script pour nettoyer et recréer les données avec le bon encodage UTF-8
"""
import sys
import os

# Force UTF-8 encoding
if sys.version_info[0] >= 3:
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from backoffice.models import Livre, LivreType, LivreStatus

print("=== Nettoyage et recréation des données ===\n")

# Supprimer toutes les données existantes
print("1. Suppression des données existantes...")
Livre.objects.all().delete()
LivreType.objects.all().delete()
LivreStatus.objects.all().delete()
print("   ✓ Données supprimées\n")

# 2. Créer les LivreType
print("2. Création des types de livres...")
genre_roman = LivreType.objects.create(genre="roman")
print("   ✓ Type 'roman' créé")

genre_nouvelle = LivreType.objects.create(genre="nouvelle")
print("   ✓ Type 'nouvelle' créé")

genre_polar = LivreType.objects.create(genre="polar")
print("   ✓ Type 'polar' créé")

genre_biographie = LivreType.objects.create(genre="biographie")
print("   ✓ Type 'biographie' créé\n")

# 3. Créer les LivreStatus
print("3. Création des statuts de livres...")
status_publie = LivreStatus.objects.create(status="toujours publié")
print("   ✓ Statut 'toujours publié' créé")

status_arret = LivreStatus.objects.create(status="en arrêt de commercialisation")
print("   ✓ Statut 'en arrêt de commercialisation' créé")

status_reimpression = LivreStatus.objects.create(status="réimpression")
print("   ✓ Statut 'réimpression' créé\n")

# 4. Créer les 3 Livres
print("4. Création des livres...")

livre1 = Livre.objects.create(
    nom="Les Misérables",
    prix=8,
    livre_type=genre_roman,
    livre_status=status_publie
)
print("   ✓ 'Les Misérables' créé")

livre2 = Livre.objects.create(
    nom="Madame Bovary",
    prix=7,
    livre_type=genre_roman,
    livre_status=status_publie
)
print("   ✓ 'Madame Bovary' créé")

livre3 = Livre.objects.create(
    nom="Honoré de Balzac",
    prix=11,
    livre_type=genre_roman,
    livre_status=status_publie
)
print("   ✓ 'Honoré de Balzac' créé\n")

print("=== Données créées avec succès! ===")
print(f"\nNombre total de livres: {Livre.objects.count()}")
print(f"Nombre total de types: {LivreType.objects.count()}")
print(f"Nombre total de statuts: {LivreStatus.objects.count()}")

print("\nVérification des accents:")
for livre in Livre.objects.all():
    print(f"  - {livre.nom}")
