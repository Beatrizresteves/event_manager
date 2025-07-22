# Event Manager API

Sistema de gerenciamento de eventos com Django REST Framework.

## ⚙️ Tecnologias

- Python 3.8+
- Django 4.2.x
- Django REST Framework
- djangorestframework-simplejwt
- PostgreSQL
- Celery + Redis (tarefas assíncronas)
- Docker / Docker Compose (opcional)

---

## 🚀 Como rodar localmente

1. **Clone o repositório**  
   ```bash
   git clone git@github.com:SeuUsuario/event_manager.git
   cd event_manager
Crie e ative o ambiente virtual

   ```bash
python3 -m venv venv
source venv/bin/activate
   ```

Instale as dependências
  
   ```bash
pip install -r requirements.txt
   ```

Configure variáveis de ambiente
Crie um arquivo .env na raiz, baseado em .env.example:
   
   ```bash
DB_NAME=event_manager
DB_USER=event_user
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
DJANGO_SECRET_KEY=sua_chave_secreta
   ```
Prepare o banco de dados

   ```bash
sudo -u postgres psql
CREATE DATABASE event_manager;
CREATE USER event_user WITH PASSWORD 'sua_senha';
GRANT ALL PRIVILEGES ON DATABASE event_manager TO event_user;
\q
   ```

Aplique as migrações

bash
Copiar código
python manage.py migrate
Crie o superusuário

   ```bash
python manage.py createsuperuser
   ```

Rode o servidor de desenvolvimento

   ```bash
python manage.py runserver
   ```

Acesse em: http://127.0.0.1:8000/

🔑 Endpoints de Autenticação JWT
POST /api/token/
Obter Access e Refresh tokens
Body JSON:

json
Copiar código
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
POST /api/token/refresh/
Renovar Access token
Body JSON:

json
Copiar código
{
  "refresh": "seu_refresh_token"
}
Em todas as outras requisições autenticadas, envie no header:

makefile
Copiar código
Authorization: Bearer <access_token>
📚 Principais Endpoints da API
Usuários

GET /api/users/

POST /api/users/ (registro público)

GET /api/users/{id}/

PUT /api/users/{id}/

DELETE /api/users/{id}/

Eventos

GET /api/events/

POST /api/events/

GET /api/events/{id}/

PUT /api/events/{id}/

DELETE /api/events/{id}/




🐳 Docker (opcional)
Se preferir usar Docker, crie um docker-compose.yml com serviços para:

web (Django)

db (Postgres)

redis (broker Celery)

worker (Celery)

E rode:

   ```bash
docker-compose up --build
   ```


🧪 Testes
Para rodar a suíte de testes:

   ```bash
python manage.py test
   ```

Verifique cobertura para models, views, serializers e tasks.

📖 Documentação da API
Você pode usar o DRF Spectacular ou drf-yasg para gerar documentação interativa Swagger/Redoc.

Pronto! Com isso você tem um README completo, instrutivo e pronto para orientar qualquer pessoa a instalar, testar e usar sua aplicação.
