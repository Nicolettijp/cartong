# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titre', models.CharField(max_length=100)),
                ('duree', models.CharField(max_length=40, null=True, blank=True)),
                ('date_debut', models.DateField(verbose_name=b'Date de d\xc3\xa9marrage')),
                ('date_fin', models.DateField(verbose_name=b'Date de fin')),
                ('commentaire', models.TextField(null=True)),
                ('montant_prevu', models.PositiveIntegerField(null=True)),
                ('montant_disponible', models.PositiveIntegerField(null=True)),
                ('devise', models.CharField(default=b'EUR', max_length=10, choices=[('MGA', 'MGA'), ('EUR', 'EUR'), ('USD', 'USD')])),
                ('bailleurfond', models.CharField(max_length=100, null=True, blank=True)),
                ('origine', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('echelle_localisation', models.CharField(default=b'Nationale', max_length=10, choices=[('nationale', 'Nationale'), ('r\xe9gionale', 'R\xe9gionale'), ('locale', 'Locale')])),
                ('localisation', models.CharField(max_length=50)),
                ('region_status', models.SmallIntegerField(default=0, choices=[(0, b'  '), (1, b'Antananarivo'), (2, b'R\xc3\xa9gion/Commune')])),
                ('illustration', models.ImageField(null=True, upload_to=b'static/media/illustration/%Y/%m', blank=True)),
                ('creation', models.DateTimeField(auto_now_add=True, verbose_name=b'Date de cr\xc3\xa9ation fiche')),
                ('maj', models.DateTimeField(auto_now_add=True, verbose_name=b'Date de mise \xc3\xa0 jour fiche')),
            ],
            options={
                'ordering': ['-creation'],
                'verbose_name': 'Action',
                'verbose_name_plural': 'Actions',
            },
        ),
        migrations.CreateModel(
            name='Avancement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(unique=True, max_length=40, choices=[('En attente', 'En attente'), ('En cours', 'En cours'), ('Termin\xe9', 'Termin\xe9')])),
            ],
            options={
                'verbose_name_plural': 'Avancements',
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
                ('referent', models.ForeignKey(blank=True, to='cnls1.Organisme', null=True)),
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
                ('nom', models.CharField(max_length=40, choices=[('plaidoyer', 'Plaidoyer'), ('ccc', 'CCC'), ('promotion de pr\xe9servatifs', ''), ('communication de masse', ''), ('prise en charge IST', ''), ('prise en charge m\xe9dicale', ''), ('soutien', 'Soutien'), ('coordination', 'Coordination'), ('renforcement de capacit\xe9s', 'Renforcement de capacit\xe9s')])),
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
            model_name='action',
            name='avancement',
            field=models.ForeignKey(to='cnls1.Avancement', to_field=b'nom', verbose_name=b"Etat d'avancement"),
        ),
        migrations.AddField(
            model_name='action',
            name='cible',
            field=models.ManyToManyField(to='cnls1.Cible', verbose_name=b'Cibles'),
        ),
        migrations.AddField(
            model_name='action',
            name='createur',
            field=models.ForeignKey(to='cnls1.Utilisateur', to_field=b'user', verbose_name=b'nom du responsable de la fiche'),
        ),
        migrations.AddField(
            model_name='action',
            name='organisme',
            field=models.ForeignKey(verbose_name=b"organisme maitre d'oeuvre", to='cnls1.Organisme'),
        ),
        migrations.AddField(
            model_name='action',
            name='typeintervention',
            field=models.ForeignKey(verbose_name=b"Types d'intervention", to='cnls1.Typeintervention'),
        ),
    ]
