# Entorns-25-26
Incial
## Requisits Funcionals TapaApp

[RequisitsFuncionalsTapatApp](RequisitsFuncionalsTapatApp.md)

## Requisits Tècnics TapaApp

[RequisitsTècnicsTapatApp](RequisitsTècnicsTapatApp.md)

## Configuració GIThub VsCode

Aquí configurem VSCode

## Planificació Scrum
- Iteració 1: 12/11 - 17/12 (15H) - Conexió Clinet Server
- Iteració 2: 12/01 - 04/02 (12H) - End Points WebService, dades Tutor i Child
- Iteració 3: 09/02 - 04/03 (10H) - Diagrames OO, Login i Seguretat
- Iteració 4: 09/03 - 08/04 (11H) - Visites Wireframes i BBDD
- Iteració 5: 13/04 - 29/04 (09H) - Pegat i Testing

[Projecte a GiutHub](https://github.com/users/Gerardmorsilvestre/projects/2/views/1)

# Prototip 1

Connectar Client / Servidor.
Consultar dades d'usuari per nom.

[Diagrama d'arquitectura prototip 1](charts/diagramaprototip1.mermaid)

## End-Points WebService

Definició del En-point del WebService: 

URL Server desenvolupament: http://localhost:5000/

| URL | Method | Paràmetres | Descripció | Output |
|--------------|--------------|--------------|----------|----------|
| /user       | /user   | GET    | username <String> obligatori | Retornem la informació   de    | { "code_response=1, descripcio="", name="Gustavo Lloris", username="glloris",passwoprd="12345", rol="tutor", email="glloris@xtec.cat"} 