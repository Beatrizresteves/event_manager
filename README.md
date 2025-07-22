
# Event Manager API + Frontend

Sistema de gerenciamento de eventos com backend em Django REST Framework e frontend em Vue 3.

---

## Tecnologias utilizadas

- Python 3.8+
- Django 4.2
- Django REST Framework
- djangorestframework-simplejwt (JWT Authentication)
- PostgreSQL
- Celery + Redis (para tarefas assíncronas)
- Vue 3 + Vite + Vuetify
- Axios
- Docker / Docker Compose 

---

## Rodando o projeto localmente

### Backend

1. Clone o repositório

```bash
git clone https://github.com/Beatrizresteves/event_manager/
```

2. Crie e ative o ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Crie arquivo `.env` na raiz do projeto com as variáveis:

```env
POSTGRES_DB=eventdb
POSTGRES_USER=usuario
POSTGRES_PASSWORD=senha123
DJANGO_SECRET_KEY=sua_chave_secreta
EMAIL_HOST=sandbox.smtp.mailtrap.io
EMAIL_PORT=2525
EMAIL_HOST_USER=seu_usuario_mailtrap
EMAIL_HOST_PASSWORD=sua_senha_mailtrap
YOUTUBE_API_KEY=sua_chave_youtube
```

4. Suba os containers com Docker Compose:  
```bash
docker-compose up --build
```

5. A aplicação estará disponível em:  
```
http://localhost:8000
```

6. Prepare o banco de dados PostgreSQL

No terminal do postgres:

```sql
CREATE DATABASE event_manager;
CREATE USER event_user WITH PASSWORD 'sua_senha';
GRANT ALL PRIVILEGES ON DATABASE event_manager TO event_user;
```

7. Aplique as migrações

```bash
docker-compose exec web python manage.py migrate
```

8. Crie um superusuário

```bash
docker-compose exec web python manage.py createsuperuser
```

---

### Frontend

1. No diretório do frontend:

```bash
cd ../frontend
npm install
npm run dev
```

O frontend estará disponível em: `http://localhost:5173`


## Autenticação JWT

- Login:  
  `POST /api/token/`  
  Body JSON:  
  ```json
  {
    "username": "seu_usuario",
    "password": "sua_senha"
  }
  ```

- Refresh token:  
  `POST /api/token/refresh/`  
  Body JSON:  
  ```json
  {
    "refresh": "seu_refresh_token"
  }
  ```

- Em todas as requisições autenticadas, envie no header:  
  ```
  Authorization: Bearer <access_token>
  ```

---

## Endpoints principais da API

### Usuários

- `GET /api/users/`  
- `POST /api/users/` (registro público)  
- `GET /api/users/{id}/`  
- `PUT /api/users/{id}/`  
- `DELETE /api/users/{id}/`

### Eventos

- `GET /api/events/` (listar eventos públicos)  
- `POST /api/events/` (criar evento — autenticado)  
- `GET /api/events/{id}/`  
- `PUT /api/events/{id}/`  
- `DELETE /api/events/{id}/`

### Participantes / Inscrições

- `POST /api/events/participants/` (inscrever usuário autenticado no evento)  
- `GET /api/events/participants/me/` (listar inscrições do usuário autenticado)

---

## Testes

Para rodar os testes backend:

```bash
python manage.py test
```

Ou via Docker:

```bash
docker-compose exec web pytest
```

---

## Frontend — funcionalidades

- Cadastro e login de usuários  
- Listar eventos disponíveis  
- Criar, editar e excluir eventos (usuário autenticado)  
- Inscrição em eventos  
- Visualizar eventos em que o usuário está inscrito  
