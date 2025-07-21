<template>
	<div class="container">
	  <h1 class="title">Eventos</h1>
  
	  <ul class="event-list">
		<li v-for="event in events" :key="event.id" class="event-item">
		  <strong class="event-title">{{ event.title }}</strong>
		  <time class="event-date" :datetime="event.date">{{ formatDate(event.date) }}</time>
		</li>
	  </ul>
	</div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  
  const events = ref([])
  const loading = ref(false)
  const error = ref(null)
  
  function formatDate(dateStr) {
	const date = new Date(dateStr)
	return date.toLocaleDateString('pt-BR', { day: '2-digit', month: 'short', year: 'numeric' })
  }
  
  onMounted(async () => {
	loading.value = true
	error.value = null
	try {
		const res = await axios.get(`http://localhost:8000/api/events/events/?_=${Date.now()}`)
		events.value = res.data.results || res.data
	  	console.log('Resposta da API:', res.data)


	} catch (err) {
	  error.value = 'Erro ao buscar eventos. Tente novamente mais tarde.'
	  console.error('Erro ao buscar eventos:', err)
	} finally {
	  loading.value = false
	}
  })
  </script>

  <style scoped>
  body, html, #app {
	margin: 0;
	height: 100%;
	background-color: #121212;
	font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
	color: #eee;
  }
  
  .container {
	max-width: 400px;
	margin: 3rem auto;
	padding: 1.5rem;
  }
  
  .title {
	font-size: 2.5rem;
	font-weight: 900;
	text-align: center;
	margin-bottom: 2rem;
	color: #fff;
	text-shadow: 0 0 6px rgba(255 255 255 / 0.3);
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
	cursor: default;
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
	font-style: normal;
	white-space: nowrap;
	margin-left: 1rem;
  }
  </style>