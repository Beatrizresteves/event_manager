<template>
	<div class="container">
	  <form @submit.prevent="enviarEvento" class="event-form">
		<h2 class="title">Criar Novo Evento</h2>
  
		<div class="form-group">
		  <label for="title">Nome:</label>
		  <input
			id="title"
			v-model="evento.title"
			required
			placeholder="Digite o nome do evento"
		  />
		</div>
  
		<div class="form-group">
		  <label for="date">Data:</label>
		  <input
			id="date"
			v-model="evento.date"
			type="date"
			required
		  />
		</div>
  
		<div class="form-group">
		  <label for="time">Hora:</label>
		  <input
			id="time"
			v-model="evento.time"
			type="time"
			required
		  />
		</div>
  
		<div class="form-group">
		  <label for="location">Local:</label>
		  <input
			id="location"
			v-model="evento.location"
			required
			placeholder="Digite o local do evento"
		  />
		</div>
  
		<button type="submit" :disabled="loading">
		  {{ loading ? 'Salvando...' : 'Salvar' }}
		</button>
  
		<p v-if="mensagem" class="mensagem-sucesso">{{ mensagem }}</p>
		<p v-if="erro" class="mensagem-erro">Erro: {{ erro }}</p>
	  </form>
	</div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
	name: 'EventForm',
	data() {
		return {
		evento: {
			title: '',
			date: '',
			time: '',
			location: ''
		},
		mensagem: '',
		erro: '',
		loading: false,
		token: localStorage.getItem('access_token') || ''
		}
	},
	watch: {
		eventoSelecionado: {
			immediate: true,
			handler(novoEvento) {
				if (novoEvento) {
					this.evento = {
					id: novoEvento.id,
					title: novoEvento.title,
					date: novoEvento.date,
					time: novoEvento.time || '',       
					location: novoEvento.location
					}
				} else {
					this.resetarFormulario()
				}
			}
		}
	},
	props: {
		eventoSelecionado: {
			type: Object,
			default: null
		}
		},
	methods: {
		async enviarEvento() {
			this.loading = true
			this.mensagem = ''
			this.erro = ''
			try {
				const url = this.evento.id
				? `http://localhost:8000/api/events/events/${this.evento.id}/`
				: 'http://localhost:8000/api/events/events/'
				const metodo = this.evento.id ? 'put' : 'post'

				await axios({
				method: metodo,
				url,
				data: this.evento,
				headers: { Authorization: `Bearer ${this.token}` }
				})

				this.mensagem = this.evento.id ? 'Evento atualizado!' : 'Evento criado!'
				this.evento = { title: '', date: '', time: '', location: '' }
				this.$emit('evento-criado')
			} catch (error) {
				this.erro = 'Erro ao salvar evento'
			} finally {
				this.loading = false
			}
		},
		async resetarFormulario() {
			this.evento = {
				id: novoEvento.id,
				nome: novoEvento.title,   
				data: novoEvento.date,     
				local: novoEvento.location 
				}
		}
	}
  }
  </script>
  <style scoped>
  .container {
	background: #1e1e1e;
	padding: 2rem;
	border-radius: 12px;
	box-shadow: 0 10px 25px rgba(0, 0, 0, 0.6);
	max-width: 800px;
	margin: 2rem auto;
	font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
	color: #eee;
  }
  
  .title {
	font-size: 1.75rem;
	font-weight: 800;
	text-align: center;
	margin-bottom: 1.5rem;
	color: #fff;
	text-shadow: 0 0 6px rgba(255, 255, 255, 0.3);
  }
  
  .event-form {
	display: flex;
	flex-direction: column;
	gap: 1.25rem;
  }
  
  .form-group {
	display: flex;
	flex-direction: column;
  }
  
  .form-group label {
	font-weight: 500;
	margin-bottom: 0.4rem;
	color: #bbb;
  }
  
  input {
	padding: 0.75rem 1rem;
	font-size: 1rem;
	border: 2px solid #333;
	border-radius: 8px;
	background-color: #2a2a2a;
	color: #eee;
	transition: border-color 0.3s, box-shadow 0.3s;
  }
  
  input:focus {
	outline: none;
	border-color: #4caf50;
	box-shadow: 0 0 6px #4caf50aa;
  }
  
  input::placeholder {
	color: #999;
  }
  
  button {
	padding: 0.75rem 1rem;
	font-size: 1rem;
	border: none;
	border-radius: 8px;
	background: linear-gradient(90deg, #4caf50, #388e3c);
	color: white;
	cursor: pointer;
	font-weight: 600;
	transition: background 0.3s, box-shadow 0.3s;
  }
  
  button:hover:not(:disabled) {
	background: linear-gradient(90deg, #66bb6a, #2e7d32);
	box-shadow: 0 4px 12px #66bb6aaa;
  }
  
  button:disabled {
	cursor: not-allowed;
	opacity: 0.6;
	background: #555;
	box-shadow: none;
  }
  
  .mensagem-sucesso {
	color: #16a34a;
	font-weight: 600;
	text-align: center;
	font-size: 0.95rem;
  }
  
  .mensagem-erro {
	color: #dc2626;
	font-weight: 600;
	text-align: center;
	font-size: 0.95rem;
  }
  </style>
  