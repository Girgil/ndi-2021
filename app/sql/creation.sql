DROP TABLE IF EXISTS "SAUVER_BATEAU";
DROP TABLE IF EXISTS "SAUVER_PERSONNE";
DROP TABLE IF EXISTS "SAUVER_EQUIPAGE";
DROP TABLE IF EXISTS "APPARTENIR";
DROP TABLE IF EXISTS "EFFECTUER";
DROP TABLE IF EXISTS "AVOIR_MEDAILLE";
DROP TABLE IF EXISTS "EQUIPAGE";
DROP TABLE IF EXISTS "BATEAU";
DROP TABLE IF EXISTS "SAUVETEUR";
DROP TABLE IF EXISTS "MEDAILLE";
DROP TABLE IF EXISTS "PERSONNE";
DROP TABLE IF EXISTS "SAUVETAGE";

CREATE TABLE "SAUVER_BATEAU" (
  "idSauvetage" INTEGER,
  "idBateau" INTEGER,
  "nbPersonneSauvee" INTEGER,
  PRIMARY KEY ("idSauvetage", "idBateau"),
  FOREIGN KEY ("idSauvetage") REFERENCES "SAUVETAGE" ("idSauvetage"),
  FOREIGN KEY ("idBateau") REFERENCES "BATEAU" ("idBateau")
);

CREATE TABLE "BATEAU" (
  "idBateau" INTEGER,
  "typeBat" VARCHAR(42),
  "nomBat" VARCHAR(42),
  PRIMARY KEY ("idBateau")
);

CREATE TABLE "EQUIPAGE" (
  "idEquipage" INTEGER,
  "nomEquipage" VARCHAR(42),
  PRIMARY KEY ("idEquipage")
);

CREATE TABLE "APPARTENIR" (
  "idSauveteur" INTEGER,
  "idEquipage" INTEGER,
  "rolePersonne" VARCHAR(42),
  PRIMARY KEY ("idSauveteur", "idEquipage"),
  FOREIGN KEY ("idSauveteur") REFERENCES "SAUVETEUR" ("idSauveteur"),
  FOREIGN KEY ("idEquipage") REFERENCES "EQUIPAGE" ("idEquipage")
);

CREATE TABLE "SAUVETAGE" (
  "idSauvetage" INTEGER,
  "nomSauvetage" VARCHAR(42),
  "dateSauvetage" DATE,
  PRIMARY KEY ("idSauvetage")
);

CREATE TABLE "EFFECTUER" (
  "idsauvetage" INTEGER,
  "idbateau" INTEGER,
  "idequipage" INTEGER,
  PRIMARY KEY ("idSauvetage", "idBateau", "idEquipage"),
  FOREIGN KEY ("idSauvetage") REFERENCES "SAUVETAGE" ("idSauvetage"),
  FOREIGN KEY ("idBateau") REFERENCES "BATEAU" ("idBateau"),
  FOREIGN KEY ("idEquipage") REFERENCES "EQUIPAGE" ("idEquipage")
);

CREATE TABLE "SAUVETEUR" (
  "idsauveteur" INTEGER,
  "idpersonne" INTEGER,
  PRIMARY KEY ("idsauveteur"),
  FOREIGN KEY ("idpersonne") REFERENCES "PERSONNE" ("idpersonne")
);

CREATE TABLE "AVOIR_MEDAILLE" (
  "idMedaille" INTEGER,
  "idSauveteur" INTEGER,
  PRIMARY KEY ("idMedaille", "idSauveteur"),
  FOREIGN KEY ("idMedaille") REFERENCES "MEDAILLE" ("idMedaille"),
  FOREIGN KEY ("idSauveteur") REFERENCES "SAUVETEUR" ("idSauveteur")
);

CREATE TABLE "SAUVER_PERSONNE" (
  "idSauvetage" INTEGER,
  "idPersonne" INTEGER,
  PRIMARY KEY ("idSauvetage", "idPersonne"),
  FOREIGN KEY ("idSauvetage") REFERENCES "SAUVETAGE" ("idSauvetage"),
  FOREIGN KEY ("idPersonne") REFERENCES "PERSONNE" ("idPersonne")
);

CREATE TABLE "PERSONNE" (
  "idpersonne",
  "nompersonne" VARCHAR(42),
  "prenompersonne" VARCHAR(42),
  "datenaispersonne" VARCHAR(42),
  "datemortpersonne" VARCHAR(42),
  "etatcivilpersonne" TEXT,
  "descendancepersonne" TEXT,
  PRIMARY KEY ("idpersonne")
);

CREATE TABLE "MEDAILLE" (
  "idmedaille" INTEGER,
  "nommedaille" VARCHAR(42),
  PRIMARY KEY ("idmedaille")
);

CREATE TABLE "UTILISATEUR"(
  "idUser" INTEGER PRIMARY KEY NOT NULL,
  "username" TEXT,
  "passwordUser" BLOB,
  "emailUser" TEXT,
  "roleUtilisateur" TEXT CHECK("roleUtilisateur" IN ('U','A'))
);

CREATE TABLE "SESSION"(
  "tokenSession" TEXT NOT NULL,
  "idUser" TEXT NOT NULL,
  FOREIGN KEY(idUser) REFERENCES UTILISATEUR(idUser)
);