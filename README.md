# 📚 Projet Bookr - Gestion de Livres Django

Projet Django complet pour la gestion de livres avec requêtes avancées de base de données.

## 🎯 Fonctionnalités Implémentées

### Modèles
- ✅ **LivreType** - Types de livres (roman, nouvelle, polar, biographie)
- ✅ **LivreStatus** - Statuts (toujours publié, en arrêt de commercialisation, réimpression)
- ✅ **Livre** - Livres avec nom, prix et relations ForeignKey

### Requêtes (8 requêtes demandées)
1. ✅ Liste de tous les livres créés
2. ✅ Livres qui commencent par "L"
3. ✅ Livres contenant "Misérables"
4. ✅ Livres prix >= 10€
5. ✅ Livres prix >= 10€ ET statut "toujours publié"
6. ✅ Livre avec le prix le plus élevé
7. ✅ Liste des statuts
8. ✅ Nombre total de livres

### Interface
- ✅ Page web moderne affichant toutes les requêtes
- ✅ CSS séparé (design responsive avec dégradés)
- ✅ Admin Django configuré

## 📋 Structure du Projet

```
bookr_project/
├── bookr/
│   ├── backoffice/              # App gestion (modèles)
│   │   ├── models.py            # Modèles Livre, LivreType, LivreStatus
│   │   ├── admin.py             # Admin Django configuré
│   │   └── management/commands/ # Commandes Django
│   │       ├── populate_books.py
│   │       ├── modify_books.py
│   │       └── reset_books.py
│   ├── bookr_app/               # App affichage (vues)
│   │   ├── views.py             # Toutes les requêtes
│   │   ├── templates/           # Templates HTML
│   │   └── static/              # CSS séparé
│   ├── bookr/                   # Configuration
│   │   ├── settings.py
│   │   └── urls.py
│   ├── demo_queries.py          # Script de démonstration
│   └── manage.py
└── README.md

## 🚀 Démarrage Rapide (2 minutes)

### 1. Installation
```bash
pip install django psycopg2-binary
```

### 2. Configuration
```bash
cd bookr
python manage.py migrate          # Créer la base de données
python manage.py populate_books   # Créer les données initiales
```

### 3. Lancer le Serveur
```bash
python manage.py runserver
```

**🌐 Accédez à:** http://127.0.0.1:8000/

Toutes les 8 requêtes sont affichées sur la page d'accueil!

---

## 📖 Commandes Django Disponibles

### Gestion des Données

#### Peupler la base
```bash
python manage.py populate_books
```
Crée les types, statuts et 3 livres initiaux (sans doublons).

#### Modifier les données
```bash
python manage.py modify_books
```
Effectue les modifications demandées:
- Modifie le statut du 2ème livre → "réimpression"
- Modifie le statut du 3ème livre → "en arrêt de commercialisation"
- Supprime le 3ème livre
- Affiche le nombre restant

#### Réinitialiser complètement
```bash
python manage.py reset_books
```
Supprime TOUTES les données et recrée les données initiales (avec confirmation).

Pour forcer sans confirmation:
```bash
python manage.py reset_books --no-input
```

### Démonstration

#### Voir toutes les requêtes dans la console
```bash
python manage.py shell -c "exec(open('demo_queries.py', encoding='utf-8').read())"
```
Affiche les 8 requêtes avec résultats et statistiques.

---

## 👤 Administration Django

### Créer un superutilisateur
```bash
python manage.py createsuperuser
```

### Accéder à l'admin
1. Démarrer: `python manage.py runserver`
2. Ouvrir: http://127.0.0.1:8000/admin/
3. Interface complète avec filtres et recherche

---

## 🗄️ Base de Données

### SQLite (par défaut)
✅ **Déjà configuré** - Aucune installation nécessaire  
Fichier: `db.sqlite3`

### PostgreSQL (optionnel)

#### 1. Créer la base PostgreSQL
```sql
CREATE DATABASE bookr_db ENCODING 'UTF8';
CREATE USER bookr_user WITH PASSWORD 'bookr_password';
GRANT ALL PRIVILEGES ON DATABASE bookr_db TO bookr_user;
```

#### 2. Modifier `bookr/settings.py`
Commentez SQLite et décommentez la configuration PostgreSQL:
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "bookr_db",
        "USER": "bookr_user",
        "PASSWORD": "bookr_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

#### 3. Appliquer les migrations
```bash
python manage.py migrate
python manage.py populate_books
```

## 🔍 Requêtes Django Implémentées

### 1. Tous les livres créés
```python
Livre.objects.all()
```

### 2. Livres qui commencent par "L"
```python
Livre.objects.filter(nom__startswith="L")
```
**Résultat:** Les Misérables

### 3. Livres contenant "Misérables"
```python
Livre.objects.filter(nom__icontains="Misérables")
```
**Résultat:** Les Misérables

### 4. Livres prix >= 10€
```python
Livre.objects.filter(prix__gte=10)
```
**Résultat:** Honoré de Balzac (11€)

### 5. Prix >= 10€ ET statut "toujours publié"
```python
Livre.objects.filter(prix__gte=10, livre_status__status="toujours publié")
```
**Résultat:** Honoré de Balzac

### 6. Livre avec le prix le plus élevé
```python
Livre.objects.order_by('-prix').first()
# Alternative
Livre.objects.aggregate(Max('prix'))
```
**Résultat:** Honoré de Balzac (11€)

### 7. Liste des statuts
```python
LivreStatus.objects.all()
```
**Résultat:** 3 statuts

### 8. Nombre total de livres
```python
Livre.objects.count()
```
**Résultat:** 3 livres

## 📊 Données Initiales

### Types de Livres
- roman, nouvelle, polar, biographie

### Statuts
- toujours publié
- en arrêt de commercialisation  
- réimpression

### Livres Créés
1. **Les Misérables** - 8€ (roman, toujours publié)
2. **Madame Bovary** - 7€ (roman, toujours publié)
3. **Honoré de Balzac** - 11€ (roman, toujours publié)

---

## 🐍 Shell Django - Exemples

```python
# Ouvrir le shell
python manage.py shell

# Importer les modèles
from backoffice.models import Livre, LivreType, LivreStatus

# Voir tous les livres
for livre in Livre.objects.all():
    print(f"{livre.nom} - {livre.prix}€")

# Filtrer
Livre.objects.filter(nom__startswith="L")
Livre.objects.filter(prix__gte=10)

# Livre le plus cher
Livre.objects.order_by('-prix').first()

# Compter
Livre.objects.count()

# Créer un nouveau livre
roman = LivreType.objects.get(genre="roman")
publie = LivreStatus.objects.get(status="toujours publié")
nouveau = Livre.objects.create(
    nom="Le Comte de Monte-Cristo",
    prix=9.50,
    livre_type=roman,
    livre_status=publie
)

# Modifier
livre = Livre.objects.get(nom="Madame Bovary")
livre.prix = 8.50
livre.save()

# Supprimer
livre.delete()
```

---

## 🔧 Concepts Django Utilisés

### Modèles
- CharField, DecimalField
- ForeignKey avec `on_delete=PROTECT`
- `related_name` pour relations inverses
- Meta class (verbose_name, ordering)
- Méthode `__str__()`

### QuerySets
- `.filter()`, `.all()`, `.get()`
- `.count()`, `.first()`
- `.order_by()`, `.aggregate()`
- Lookups: `__startswith`, `__icontains`, `__gte`
- Relations: `livre_status__status`

### Vues & Templates
- Function-based views
- `render()` avec context
- Template tags: `{% for %}`, `{% if %}`, `{% empty %}`
- `{% load static %}`, `{% static %}`
- Template filters: `|pluralize`

### Admin
- ModelAdmin personnalisé
- `list_display`, `list_filter`, `search_fields`
- `fieldsets` pour organisation
- `@admin.register` decorator

### Management Commands
- Héritage de `BaseCommand`
- Méthode `handle()`
- Arguments avec `add_arguments()`
- Style coloré: `self.style.SUCCESS()`

---

## 📝 URLs du Projet

- **/** - Page principale (toutes les requêtes)
- **/admin/** - Interface d'administration
- **/backoffice** - Vues backoffice (optionnel)

---

## 🆘 Dépannage

### Le serveur ne démarre pas
```bash
# Vérifier que vous êtes dans le bon dossier
cd bookr
python manage.py runserver
```

### Erreur "Table doesn't exist"
```bash
python manage.py migrate
python manage.py populate_books
```

### Pas de données
```bash
python manage.py reset_books --no-input
```

### Port déjà utilisé
```bash
python manage.py runserver 8001
```

---

## 📚 Technologies

- **Django 6.0.3** - Framework web
- **Python 3.13** - Langage
- **SQLite** - Base de données (défaut)
- **PostgreSQL** - Support inclus
- **HTML5/CSS3** - Frontend moderne

---

## ✅ Checklist du Projet

- [x] Modèles avec ForeignKey
- [x] Migrations créées et appliquées
- [x] Données initiales créées
- [x] 8 requêtes implémentées
- [x] Interface web moderne
- [x] CSS séparé (pas inline)
- [x] Admin Django configuré
- [x] Management commands
- [x] Encodage UTF-8 correct
- [x] Documentation complète

---

**Projet réalisé dans le cadre du cours Django - M2**  
**Statut: ✅ Complet et fonctionnel**
