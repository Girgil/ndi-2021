insert into BATEAU(idBateau, typeBat, nomBat)
values (1, 'canot', 'Sainte-Sophie');
insert into BATEAU(idBateau, typeBat, nomBat)
values (2, 'bateau', 'MOUETTE');
insert into BATEAU(idBateau, typeBat, nomBat)
values (3, 'bateau', 'LITTLE STAR');


insert into EQUIPAGE(idEquipage, nomEquipage)
values (1, 'de Ficquet Pierre');
insert into EQUIPAGE(idEquipage, nomEquipage)
values (2, 'de Joseph Bouteille');
insert into EQUIPAGE(idEquipage, nomEquipage)
values (3, 'de Auguste Brunet');


insert into SAUVETAGE(idSauvetage, nomSauvetage, dateSauvetage)
values (1, 'Sauvetage du LITTLE STAR',null);
insert into SAUVETAGE(idSauvetage, nomSauvetage, dateSauvetage)
values (2, 'Sauvetage du MOUETTE',null);
insert into SAUVETAGE(idSauvetage, nomSauvetage, dateSauvetage)
values (3, 'Sauvetage de pecheurs',null);


insert into PERSONNE(idpersonne, nompersonne, prenompersonne, datenaispersonne, datemortpersonne, etatcivilpersonne, descendancepersonne)
values (1, 'DELUGNY', 'Pierre', null, null, 
"Naissance le 11 août 1824 à Gravelines
Décédé le 11 avril 1912 à Malo-les-Bains",
"Fils de Pierre Bonaventure Delugny marin et de Marie Geneviève Lamotte
Mariage le 15 septembre 1842 à Gravelines avec Joséphine Zoonekindt dont
André, Pierre, Charles DELUGNY Pilote et sauveteur");

insert into PERSONNE(idpersonne, nompersonne, prenompersonne, datenaispersonne, datemortpersonne, etatcivilpersonne, descendancepersonne)
values (2, 'GOSSIN', 'Charles', null , Null, 
"– Naissance 18 juin 1839 Gravelines
– Décédé 22 avril 1933 à Malo-les-Bains",
"Fils de Pierre Jean – Contremaître chez un armateur (1813 – 1873)
et Marie Martine Madeleine FICQUET (1804 – 1877) dont :
             – Pierre Louis Joseph* (1837 – 1902)
             – Jules, Auguste (1842 – 1921)
            Pilote  Médaille d’or du sauvetage -Ministère de la Marine
             – Félix Auguste (1844 – 1892)
Péri en mer à bord de la goélette ‘REINE » le 16/03/1892
* Pierre Louis aura un fils Pierre Gossin  Sauveteur Pilote maitre au cabotage – 1864 – 1914 deux sauvetages a son actif en 1905
Premier mariage avec Marie Rosalie FICQUET (1846 – ) fille de Pierre Ficquet dont :
                                                Paul Lucien (1885 – 1954) Acte 504 naissance 1885 Dunkerque
Mariage 3 juillet 1917 avec Julie Emma Blanckaert à Malo-les-Bains      Divorce (Source base Léonore)
Recensé en 1906 et 1926 au 25 avenue Gaspard Malo à Malo-les-Bains");

insert into PERSONNE(idpersonne, nompersonne, prenompersonne, datenaispersonne, datemortpersonne, etatcivilpersonne, descendancepersonne)
values (3, 'FICQUET', 'Pierre', null, Null, 
"Naissance le 12 mars 1816 à Gravelines
Fils de Jacques François (marin pêcheur) (1791 -…) et de Marie Louise Victoire BOUCLET
Décès en 17 avril 1901  
Pierre Ficquet devient ainsi  le beau-père d’un futur patron du canot qui recevra aussi la Légion d’Honneur. 
Ils sont tous les deux présents sur le canot lors du naufrage du SPRING le 2 novembre 1867.",
"Mariage le 22/08/1838 avec Marie Joséphine BARRA à Gravelines
Descendance
 – Antoine Joseph Auguste Patron du canot de sauvetage Chevalier de la Légion d’Honneur Pilote (1844 – 1910) Marié le 15 novembre 1871 avec Marie Louise NOEDTS
 – Jean Pierre Louis 1839-1960 marié le 18 novembre 1863, Dunkerque (59), avec Catherine Léonide LAMPEENE 1841
 – Hortense Claire 1854-1941,  mariée le le 11/02/1879 à Victor-Edouard Charles HENDERYCKSEN
 – Marie Rosalie Emma FICQUET mariée le  3 février 1864 à Charles Alexis GOSSIN");


insert into MEDAILLE(idmedaille, nommedaille)
values (1, "Médaille d'honneur");
insert into MEDAILLE(idmedaille, nommedaille)
values (2, 'MÉDAILLE D’HONNEUR
POUR ACTES DE DÉVOUEMENT
ET FAITS DE SAUVETAGE');


insert into SAUVETEUR(idsauveteur, idpersonne)
values (1, 3);


insert into AVOIR_MEDAILLE(idMedaille, idSauveteur)
values (1, 1);
insert into AVOIR_MEDAILLE(idMedaille, idSauveteur)
values (2, 1);


insert into APPARTENIR(idSauveteur, idEquipage, rolePersonne)
values (1, 1, "Patron");


insert into SAUVER_PERSONNE(idSauvetage, idPersonne)
values (1, 1);
insert into SAUVER_PERSONNE(idSauvetage, idPersonne)
values (2, 2);


insert into EFFECTUER(idsauvetage, idbateau, idequipage)
values (1, 1, 1);
insert into EFFECTUER(idsauvetage, idbateau, idequipage)
values (2, 3, 1);


insert into SAUVER_BATEAU(idSauvetage, idBateau, nbPersonneSauvee)
values (1, 1, 50);
insert into SAUVER_BATEAU(idSauvetage, idBateau, nbPersonneSauvee)
values (2, 3, 2);