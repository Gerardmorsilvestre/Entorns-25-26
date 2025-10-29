# Requisits Tècnics TapatApp

## Arquitectura
[Client Servidor](charts/mvc-generic.mermaid)

## 1. Backend (Seridor i Gestió de Dades)
El backend serà el cor del sistema, encarregat de gestionar dades, usuaris o la lògica del sistema.

### a. Requisits del Servidor
- Allotjament: Hosting compartit
- Base de dades: Mysql o MariaDB
- Sistemes Operatius: Linux o Windows
- WebService: RESTFul llibreria Python Flask 

### b. Llenguatges de programació
- Python

### c. Seguretat
- Autentificació i autorització pels usuaris
- Xifratge de dades HTTPS
- Còpies de seguretat automàtiques

## 2. Frontend
El frontend...

### a. Tipus de Clients
- App Mòbil: Android
- Consola Python
- Framework Multiplataforma: Flutter (Apps IOS Android, web, Desktop)

### b. Emmagatzematge local i sincronització
- Dades guardem en local: Token, nickname
- Seguretat: HTTPS, autentificació serveis per Token

### c.Gestió d'accesibilitat
- Nivells A, AA, AAA d'accesibilitat

## 3. Requisits generals Infrasetrucutura

### a. Gestió d'usuari i autentificació
- Rols Usuari: Tutor i cuidador
- Seguretat password: md5 o sha256

### b. Requisitts d'infraestrucutra
- Xarxa Internet 
- Espai d'emmagatzematge a Servidor: 1Tb
- APIs a tercers: No en fem servir

## 4. Requisits del Procés de desenvolupament
- IDE's: VSCode Python, Android Studio, PyCharm
- Control de versions: git, GitHub
- Metodologia de desenvolupament: SCRUM
- Testing i proves de qualitat(QA): Tests i proves unitàries
