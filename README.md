Proyecto con Traefik, PostgreSQL, Neo4j y Flask

Este proyecto configura un entorno con Traefik, PostgreSQL, Neo4j y Flask para gestionar bases de datos y una API de manera organizada.

---

## ¿Qué hace este proyecto?
- Usa **Traefik** como enrutador para gestionar las conexiones a los servicios.
- Configura **PostgreSQL** como base de datos relacional.
- Configura **Neo4j** como base de datos orientada a grafos.
- Implementa una **API en Flask** que responde a solicitudes en la ruta `/localhost/Harold-Rodriguez/`.
- Permite acceder a los servicios mediante dominios personalizados:
  - **PostgreSQL** → `http://postgresql.localhost`
  - **Neo4j** → `http://neo4j.localhost`
  - **API** → `http://localhost/Harold-Rodriguez/`

---

## **🚀 ¿Cómo correr el proyecto desde cero?**

### **1️⃣ Clonar el repositorio**
Si no tienes el proyecto en tu máquina, clónalo con:  
```bash
git clone https://github.com/Haroldmedina2003/parcial.git

