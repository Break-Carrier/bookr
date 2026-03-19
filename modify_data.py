"""
Script pour modifier les données selon les exigences du projet
"""
from backoffice.models import Livre, LivreStatus

print("=== Modifications des données ===\n")

# Récupérer tous les livres
livres = Livre.objects.all().order_by('id')

if livres.count() >= 3:
    # 1. Modifier le statut du 2ème livre de "toujours publié" à "réimpression"
    livre2 = livres[1]  # Index 1 = 2ème livre
    status_reimpression = LivreStatus.objects.get(status="réimpression")

    print(f"1. Modification du statut du 2ème livre: {livre2.nom}")
    print(f"   Ancien statut: {livre2.livre_status.status}")
    livre2.livre_status = status_reimpression
    livre2.save()
    print(f"   Nouveau statut: {livre2.livre_status.status}\n")

    # 2. Modifier le statut du 3ème livre à "en arrêt de commercialisation"
    livre3 = livres[2]  # Index 2 = 3ème livre
    status_arret = LivreStatus.objects.get(status="en arrêt de commercialisation")

    print(f"2. Modification du statut du 3ème livre: {livre3.nom}")
    print(f"   Ancien statut: {livre3.livre_status.status}")
    livre3.livre_status = status_arret
    livre3.save()
    print(f"   Nouveau statut: {livre3.livre_status.status}\n")

    # 3. Supprimer le 3ème livre
    print(f"3. Suppression du 3ème livre: {livre3.nom}")
    livre3_nom = livre3.nom
    livre3.delete()
    print(f"   '{livre3_nom}' a été supprimé\n")
else:
    print("Erreur: Pas assez de livres dans la base de données")

# 4. Afficher le nombre total de livres restants
nombre_livres = Livre.objects.count()
print(f"=== Nombre total de livres restants: {nombre_livres} ===")

# Afficher les livres restants
print("\nLivres restants:")
for livre in Livre.objects.all():
    print(f"  - {livre.nom} ({livre.prix}€) - Status: {livre.livre_status.status}")
