from django.shortcuts import render
from backoffice.models import Livre, LivreType, LivreStatus
from django.db.models import Sum


def index(request):
    tous_les_livres = Livre.objects.all()
    livres_commencent_L = Livre.objects.filter(nom__startswith="L")
    livres_avec_miserables = Livre.objects.filter(nom__icontains="Misérables")
    livres_prix_gte_10 = Livre.objects.filter(prix__gte=10)
    livres_prix_10_et_publie = Livre.objects.filter(
        prix__gte=10,
        livre_status__status="toujours publié"
    )
    livre_prix_max = Livre.objects.order_by('-prix').first()
    statuts_livres = LivreStatus.objects.all()
    nombre_total_livres = Livre.objects.count()

    tous_les_types = LivreType.objects.all()
    valeur_catalogue = Livre.objects.aggregate(total=Sum('prix'))['total'] or 0
    nombre_types = tous_les_types.count()
    nombre_statuts = statuts_livres.count()

    context = {
        'tous_les_livres': tous_les_livres,
        'livres_commencent_L': livres_commencent_L,
        'livres_avec_miserables': livres_avec_miserables,
        'livres_prix_gte_10': livres_prix_gte_10,
        'livres_prix_10_et_publie': livres_prix_10_et_publie,
        'livre_prix_max': livre_prix_max,
        'statuts_livres': statuts_livres,
        'nombre_total_livres': nombre_total_livres,
        'tous_les_types': tous_les_types,
        'valeur_catalogue': valeur_catalogue,
        'nombre_types': nombre_types,
        'nombre_statuts': nombre_statuts,
    }

    return render(request, 'bookr_app/index.html', context)
