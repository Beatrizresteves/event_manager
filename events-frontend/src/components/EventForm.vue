<!-- src/components/EventForm.vue -->
<template>
	<form @submit.prevent="enviarEvento" class="event-form">
	  <h2>Criar Novo Evento</h2>
  
	  <div class="form-group">
		<label for="nome">Nome:</label>
		<input id="nome" v-model="evento.nome" required placeholder="Digite o nome do evento" />
	  </div>
  
	  <div class="form-group">
		<label for="data">Data:</label>
		<input id="data" v-model="evento.data" type="date" required />
	  </div>
  
	  <div class="form-group">
		<label for="local">Local:</label>
		<input id="local" v-model="evento.local" required placeholder="Digite o local do evento" />
	  </div>
  
	  <button type="submit" class="btn-submit">Salvar</button>
  
	  <p v-if="mensagem" class="mensagem-sucesso">{{ mensagem }}</p>
	  <p v-if="erro" class="mensagem-erro">Erro: {{ erro }}</p>
	</form>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
	name: 'EventForm',
	data() {
	  return {
		evento: {
		  nome: '',
		  data: '',
		  local: ''
		},
		mensagem: '',
		erro: ''
	  }
	},
	methods: {
	  async enviarEvento() {
		try {
			console.log(this.tokenUsuario)
		  const resposta = await axios.post('http://localhost:8000/api/events/', this.evento, {
			headers: {
				Authorization: `Token ${this.tokenUsuario}`
			}
			})
		  this.mensagem = 'Evento criado com sucesso!'
		  this.erro = ''
		  this.evento = { nome: '', data: '', local: '' }
		  this.$emit('evento-criado') // se quiser atualizar a lista
		} catch (error) {
		  this.erro = error.response?.data?.detail || 'Erro ao criar evento'
		  this.mensagem = ''
		}
	  }
	}
  }
  </script>
  
  <style scoped>
  .event-form {
	max-width: 400px;
	margin: 1rem auto;
	background: #fff;
	border-radius: 8px;
	padding: 20px 25px;
	box-shadow: 0 4px 12px rgb(0 0 0 / 0.1);
	font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  
  .event-form h2 {
	text-align: center;
	color: #333;
	margin-bottom: 20px;
	font-weight: 600;
  }
  
  .form-group {
	margin-bottom: 15px;
	display: flex;
	flex-direction: column;
  }
  
  .form-group label {
	margin-bottom: 6px;
	font-weight: 500;
	color: #555;
  }
  
  .form-group input[type="text"],
  .form-group input[type="date"] {
	padding: 10px 12px;
	border: 1.8px solid #ccc;
	border-radius: 6px;
	font-size: 1rem;
	transition: border-color 0.3s ease;
  }
  
  .form-group input[type="text"]:focus,
  .form-group input[type="date"]:focus {
	outline: none;
	border-color: #3b82f6; /* azul suave */
	box-shadow: 0 0 6px rgba(59, 130, 246, 0.4);
  }
  
  .btn-submit {
	width: 100%;
	padding: 12px 0;
	background-color: #3b82f6;
	border: none;
	color: white;
	font-weight: 600;
	font-size: 1.1rem;
	border-radius: 6px;
	cursor: pointer;
	transition: background-color 0.3s ease;
  }
  
  .btn-submit:hover {
	background-color: #2563eb;
  }
  
  .mensagem-sucesso {
	margin-top: 15px;
	color: #16a34a; /* verde */
	font-weight: 600;
	text-align: center;
  }
  
  .mensagem-erro {
	margin-top: 15px;
	color: #dc2626; /* vermelho */
	font-weight: 600;
	text-align: center;
  }
  </style>
  