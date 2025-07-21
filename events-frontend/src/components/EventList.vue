<template>
	<div class="container">
	  <h1 class="title">Eventos</h1>
  
	  <p v-if="error" class="error-message">{{ error }}</p>
	  <p v-if="loading" class="loading-message">Carregando eventos...</p>
  
	  <ul v-if="!loading && events.length" class="event-list">
		<li v-for="event in events" :key="event.id" class="event-item">
		  <div>
			<strong class="event-title">{{ event.title }}</strong>
			<time class="event-date" :datetime="event.date">
			  {{ formatDate(event.date) }}
			</time>
		  </div>
		  <div class="buttons">
			<button @click="editarEvento(event)">✏️</button>
			<button @click="excluirEvento(event.id)">🗑️</button>
			<button @click="participar(event)" :disabled="loadingInscricao[event.id]">
			  {{ loadingInscricao[event.id] ? 'Inscrevendo...' : 'Participar' }}
			</button>
		  </div>
		</li>
	  </ul>
  
	  <p v-else-if="!loading" class="no-events">Nenhum evento disponível.</p>
	</div>
  </template>
  
  <script setup>
  import { ref, onMounted, defineEmits, defineExpose } from 'vue'
  import axios from 'axios'
  
  const emit = defineEmits(['editar-evento'])
  
  const events = ref([])
  const loading = ref(false)
  const error = ref(null)
  const loadingInscricao = ref({})
  
  function formatDate(dateStr) {
	const date = new Date(dateStr)
	return date.toLocaleDateString('pt-BR', {
	  day: '2-digit',
	  month: 'short',
	  year: 'numeric',
	})
  }
  
  async function carregarEventos() {
	loading.value = true
	error.value = null
	try {
	  const res = await axios.get('http://localhost:8000/api/events/events/')
	  events.value = res.data.results || res.data
	} catch (err) {
	  error.value = 'Erro ao buscar eventos.'
	} finally {
	  loading.value = false
	}
  }
  
  async function excluirEvento(id) {
	if (!confirm('Tem certeza que deseja excluir este evento?')) return
  
	error.value = null
	try {
	  const token = localStorage.getItem('access_token') || ''
  
	  await axios.delete(`http://localhost:8000/api/events/events/${id}/`, {
		headers: { Authorization: `Bearer ${token}` },
	  })
  
	  await carregarEventos()
	} catch (err) {
	  console.error('Erro ao excluir evento:', err)
	  error.value = 'Erro ao excluir evento.'
	}
  }
  
  function editarEvento(evento) {
	emit('editar-evento', evento)
  }
  
  async function participar(event) {
	loadingInscricao.value[event.id] = true
	try {
	  const token = localStorage.getItem('access_token')
	  if (!token) {
		alert('Você precisa estar logado para se inscrever.')
		loadingInscricao.value[event.id] = false
		return
	  }
  
	  await axios.post(
		'http://localhost:8000/api/events/participants/',
		{ event: event.id },
		{
		  headers: { Authorization: `Bearer ${token}` },
		}
	  )
	  alert(`Inscrição no evento "${event.title}" realizada com sucesso!`)
	} catch (err) {
	  if (err.response?.data?.non_field_errors) {
		alert(err.response.data.non_field_errors.join('\n'))
	  } else {
		alert('Erro ao inscrever no evento.')
	  }
	} finally {
	  loadingInscricao.value[event.id] = false
	}
  }
  
  defineExpose({ carregarEventos })
  
  onMounted(carregarEventos)
  </script>
  
  <style scoped>
  /* seu CSS permanece igual */
  .container {
	background: #1e1e1e;
	padding: 2rem;
	border-radius: 12px;
	box-shadow: 0 10px 25px rgba(0, 0, 0, 0.6);
	max-width: 800px;
	margin: 3rem auto;
	font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
	color: #eee;
  }
  
  .title {
	font-size: 2rem;
	font-weight: 800;
	text-align: center;
	margin-bottom: 1.5rem;
	color: #fff;
	text-shadow: 0 0 6px rgba(255, 255, 255, 0.3);
  }
  
  .event-list {
	list-style: none;
	padding: 0;
	margin: 0;
  }
  
  .event-item {
	background: #fff;
	color: #222;
	border-radius: 12px;
	padding: 1rem 1.25rem;
	margin-bottom: 1.25rem;
	box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
	display: flex;
	justify-content: space-between;
	align-items: center;
	transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  
  .event-item:hover {
	transform: translateY(-4px);
	box-shadow: 0 12px 25px rgba(0, 0, 0, 0.3);
  }
  
  .event-title {
	font-weight: 700;
	font-size: 1.2rem;
	letter-spacing: 0.03em;
  }
  
  .event-date {
	font-size: 0.9rem;
	color: #555;
	white-space: nowrap;
	margin-left: 1rem;
  }
  
  .error-message {
	color: #dc2626;
	text-align: center;
	font-weight: 600;
	margin-bottom: 1rem;
  }
  
  .loading-message {
	color: #ccc;
	text-align: center;
	font-style: italic;
	margin-bottom: 1rem;
  }
  
  .no-events {
	text-align: center;
	font-style: italic;
	color: #aaa;
  }
  
  .buttons {
	display: flex;
	gap: 0.5rem;
  }
  
  button {
	border: none;
	background: #333;
	cursor: pointer;
	font-size: 1.1rem;
  }
  </style>
  