<template>
	<div class="report-container">
	  <h2>Relatório de Eventos</h2>
	  
	  <div v-if="erro" class="error-message">{{ erro }}</div>
  
	  <div v-else-if="relatorio.length > 0" class="event-list">
		<div v-for="evento in relatorio" :key="evento.id" class="event-card">
		  <h3>{{ evento.title }}</h3>
		  <p><strong>Inscritos:</strong> {{ evento.inscritos_count }}</p>
		  <div class="participants">
			<strong>Participantes:</strong>
			<ul>
			  <li v-for="(p, index) in evento.participants" :key="index">
				{{ p.user.first_name }} {{ p.user.last_name }}
			  </li>
			</ul>
		  </div>
		</div>
	  </div>
  
	  <div v-else class="no-events">Nenhum evento encontrado.</div>
	</div>
  </template>
  
  <script>
  export default {
	data() {
	  return {
		relatorio: [],
		erro: null,
	  };
	},
	methods: {
	  async carregarRelatorio() {
		try {
		  const token = localStorage.getItem('access_token');
		  const response = await fetch('http://localhost:8000/api/events/reports/events/', {
			headers: {
			  'Authorization': `Bearer ${token}`,
			  'Content-Type': 'application/json',
			}
		  });
		  if (!response.ok) throw new Error('Erro ao buscar relatório');
  
		  this.relatorio = await response.json();
		  this.erro = null;
		} catch (err) {
		  console.error('Erro:', err);
		  this.erro = err.message || 'Erro desconhecido';
		  this.relatorio = [];
		}
	  }
	},
	mounted() {
	  this.carregarRelatorio();
	}
  }
  </script>
  
  <style scoped>
  .report-container {
	margin-top: 2rem;
	background-color: #1e1e1e;
	padding: 2rem;
	border-radius: 10px;
	color: #ddd;
	max-width: 700px;
	margin-left: auto;
	margin-right: auto;
	font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
	box-shadow: 0 0 10px rgba(0,0,0,0.7);
  }
  
  .report-container h2 {
	margin-bottom: 1.5rem;
	color: #61dafb;
	text-align: center;
	font-weight: 700;
	font-size: 2rem;
  }
  
  .error-message {
	color: #ff6b6b;
	font-weight: 600;
	margin-bottom: 1rem;
	text-align: center;
  }
  
  .no-events {
	text-align: center;
	font-style: italic;
	color: #999;
  }
  
  .event-list {
	display: flex;
	flex-direction: column;
	gap: 1.2rem;
  }
  
  .event-card {
	background-color: #292929;
	border-radius: 8px;
	padding: 1.2rem 1.5rem;
	box-shadow: 0 0 5px rgba(97, 218, 251, 0.4);
	transition: transform 0.2s ease;
  }
  
  .event-card:hover {
	transform: translateY(-5px);
	box-shadow: 0 0 15px rgba(97, 218, 251, 0.7);
  }
  
  .event-card h3 {
	margin: 0 0 0.5rem 0;
	color: #61dafb;
	font-weight: 600;
  }
  
  .event-card p {
	margin: 0 0 1rem 0;
	font-size: 1rem;
	color: #ccc;
  }
  
  .participants ul {
	list-style: disc;
	padding-left: 1.5rem;
	margin: 0;
	color: #bbb;
  }
  
  .participants li {
	margin-bottom: 0.3rem;
  }
  </style>
  