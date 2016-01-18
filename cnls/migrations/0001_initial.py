# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titre', models.CharField(max_length=100, verbose_name=b"Titre de l'action")),
                ('date_debut', models.DateField(verbose_name=b'Date de d\xc3\xa9marrage')),
                ('date_fin', models.DateField(verbose_name=b'Date de fin')),
                ('duree', models.CharField(max_length=40, null=True, verbose_name=b"Dur\xc3\xa9e de l'action", blank=True)),
                ('avancement', models.CharField(default=b'En cours', max_length=10, verbose_name=b"Etat d'avancement", choices=[('En attente', 'En attente'), ('En cours', 'En cours'), ('Termin\xe9', 'Termin\xe9')])),
                ('description', models.TextField(null=True, verbose_name=b"Description de l'action")),
                ('commentaire', models.TextField(null=True, verbose_name=b"Observations sur l'action")),
                ('montant_prevu', models.PositiveIntegerField(null=True, verbose_name=b'Montant pr\xc3\xa9vu')),
                ('montant_disponible', models.PositiveIntegerField(null=True, verbose_name=b'Montant disponible')),
                ('devise', models.CharField(default=b'EUR', max_length=10, choices=[('MGA', 'MGA'), ('EUR', 'EUR'), ('USD', 'USD')])),
                ('bailleurfond', models.CharField(max_length=100, null=True, verbose_name=b'Bailleurs de fond', blank=True)),
                ('origine', models.CharField(max_length=100, verbose_name=b'Origine de la donn\xc3\xa9e')),
                ('contact', models.EmailField(max_length=100, verbose_name=b"Mail du contact \xc3\xa0 l'origine de la donn\xc3\xa9e")),
                ('echelle_localisation', models.CharField(max_length=10, verbose_name=b'Echelle nationale?', choices=[(b'  ', b'  '), (b'Oui', b'Oui'), (b'Non', b'Non')])),
                ('operateur', models.CharField(max_length=100, verbose_name=b"Op\xc3\xa9rateur en lien avec l'action")),
                ('resultat_cf_annee_ant', models.CharField(max_length=100, verbose_name=b"R\xc3\xa9sultat par rapport \xc3\xa0 l'ann\xc3\xa9e pr\xc3\xa9c\xc3\xa9dente")),
                ('priorite_psn', models.CharField(max_length=100, verbose_name=b"Priorit\xc3\xa9 du PSN que l'activit\xc3\xa9 appuie")),
                ('creation', models.DateTimeField(auto_now_add=True, verbose_name=b'Date de cr\xc3\xa9ation fiche')),
                ('maj', models.DateTimeField(auto_now_add=True, verbose_name=b'Date de la derni\xc3\xa8re mise \xc3\xa0 jour fiche')),
                ('login_maj', models.DateTimeField(auto_now_add=True, verbose_name=b'Date de la derni\xc3\xa8re connection \xc3\xa0 la fiche action')),
            ],
            options={
                'ordering': ['-creation'],
                'verbose_name': 'Action',
                'verbose_name_plural': 'Actions',
            },
        ),
        migrations.CreateModel(
            name='ActionCible',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action', models.ForeignKey(to='cnls.Action')),
            ],
            options={
                'verbose_name_plural': 'Cibles',
            },
        ),
        migrations.CreateModel(
            name='ActionLocalisation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region_status', models.CharField(max_length=10, verbose_name=b"D\xc3\xa9finir la localisation de l'action ?", choices=[('Tananarive', 'Tananarive'), ('R\xe9gionale', 'R\xe9gionale'), ('Locale', 'Locale')])),
                ('choix_status', models.CharField(max_length=50, null=True, verbose_name=b'limite choisie', blank=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(default=b'SRID=3857;POINT(0.0 0.0)', srid=3857)),
                ('action', models.ForeignKey(to='cnls.Action')),
            ],
            options={
                'verbose_name_plural': 'Localisation',
            },
        ),
        migrations.CreateModel(
            name='ActionTypeintervention',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('objectif', models.PositiveIntegerField(null=True, verbose_name=b'Nombre de personnes vis\xc3\xa9')),
            ],
            options={
                'verbose_name_plural': "Types d'intervention",
            },
        ),
        migrations.CreateModel(
            name='Cible',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=40, choices=[('population g\xe9n\xe9rale', 'Population g\xe9n\xe9rale'), ('adultes', 'Adultes'), ('personnes vivant avec le vih', 'Personnes vivant avec le VIH'), ('perdus de vue', 'Perdus de vue'), ('personnes vivant avec le vih', 'Personnes vivant avec le VIH'), ('perdus de vue', 'Perdus de vue'), ('consommateurs de drogues injectables', 'Consommateurs de drogues injectables'), ('homme ayant des rapports avec d\u2019autres hommes', 'Homme ayant des rapports avec d\u2019autres hommes'), ('travailleuses du sexe', 'Travailleuses du sexe'), ('hommes \xe0 comportements \xe0 hauts risques', 'Hommes \xe0 comportements \xe0 hauts risques'), ('clients des tds', 'Clients des TdS'), ('populations migrantes', 'Populations migrantes'), ('population marc\xe9rale', 'Population carc\xe9rale'), ('forces arm\xe9es', 'Forces arm\xe9es'), ('femmes enceintes', 'Femmes enceintes'), ('femmes victimes de violences sexuelles', 'Femmes victimes de violences sexuelles'), ('leaders religieux ou traditionnels', 'Leaders religieux ou traditionnels'), ('personnels de sant\xe9', 'Personnels de sant\xe9'), ('autres (cercles associatifs, cercles religieux, etc)', 'Autres (Cercles associatifs, cercles religieux, etc)'), ('jeunes', 'Jeunes'), ('jeunes scolaris\xe9s', 'Jeunes scolaris\xe9s'), ('jeunes non-scolaris\xe9s', 'Jeunes non-scolaris\xe9s'), ('orphelins et enfants vuln\xe9rables', 'Orphelins et Enfants Vuln\xe9rables')])),
            ],
            options={
                'verbose_name_plural': 'Cibles',
            },
        ),
        migrations.CreateModel(
            name='Organisme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(unique=True, max_length=40)),
                ('description', models.TextField(null=True)),
                ('logo', models.ImageField(null=True, upload_to=b'static/media/logo/%Y/%m', blank=True)),
                ('referent', models.ForeignKey(blank=True, to='cnls.Organisme', null=True)),
            ],
            options={
                'ordering': ['nom'],
                'verbose_name': 'Organisme',
                'verbose_name_plural': 'Organismes',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(unique=True, max_length=40, choices=[('Partenaire sur une Action', 'Partenaire'), ('Bailleur', 'Bailleur'), ("Organisme ma\xeetre d'oeuvre", 'Organisme')])),
            ],
            options={
                'verbose_name_plural': 'Status',
            },
        ),
        migrations.CreateModel(
            name='Typeintervention',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=40, choices=[('plaidoyer', 'Plaidoyer'), ('ccc', 'CCC'), ('promotion de pr\xe9servatifs', 'Promotion de pr\xe9servatifs'), ('communication de masse', 'Communication de masse'), ('prise en charge IST', 'Prise en charge IST'), ('prise en charge m\xe9dicale', 'Prise en charge m\xe9dicale'), ('soutien', 'Soutien'), ('coordination', 'Coordination'), ('renforcement de capacit\xe9s', 'Renforcement de capacit\xe9s')])),
            ],
            options={
                'verbose_name_plural': "Types d'intervention",
            },
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(null=True, upload_to=b'media/photos/%Y/%m', blank=True)),
                ('is_responsable', models.BooleanField(default=False, verbose_name=b'Responsable autoris\xc3\xa9 \xc3\xa0 \xc3\xa9diter la fiche')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
                'verbose_name': 'Utilisateur',
                'verbose_name_plural': 'Utilisateurs',
            },
        ),
        migrations.AddField(
            model_name='actiontypeintervention',
            name='Typeintervention',
            field=models.ForeignKey(to='cnls.Typeintervention'),
        ),
        migrations.AddField(
            model_name='actiontypeintervention',
            name='action',
            field=models.ForeignKey(to='cnls.Action'),
        ),
        migrations.AddField(
            model_name='actioncible',
            name='cible',
            field=models.ForeignKey(to='cnls.Cible'),
        ),
        migrations.AddField(
            model_name='action',
            name='createur',
            field=models.ForeignKey(verbose_name=b'Nom du responsable de la fiche', to='cnls.Utilisateur'),
        ),
        migrations.AddField(
            model_name='action',
            name='organisme',
            field=models.ForeignKey(verbose_name=b"organisme maitre d'oeuvre", to='cnls.Organisme'),
        ),
    ]
