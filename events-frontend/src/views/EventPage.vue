<template>
	<div class="event-page">
	  <h1 class="page-title">Gerenciador de Eventos</h1>
  
	  <div class="event-wrapper">
		<div v-if="!showForm" class="event-list-section">
		  <EventList
			ref="listaEventos"
			@editar-evento="abrirFormulario($event)"
		  />
		  <button class="add-event-btn" @click="abrirFormulario(null)">+ Criar Evento</button>
		</div>
  
		<div v-else class="event-form-section">
		  <EventForm
			:eventoSelecionado="eventoEditando"
			@evento-criado="eventoSalvo"
			@cancelar="fecharFormulario"
			@voltar="fecharFormulario"
			/>
		</div>
	  </div>
	</div>
  </template>
  
  <script>
  import EventForm from '../components/EventForm.vue'
  import EventList from '../components/EventList.vue'
  
  export default {
	name: 'EventsPage',
	components: {
	  EventForm,
	  EventList
	},
	data() {
	  return {
		eventoEditando: null,
		showForm: false,
	  }
	},
	methods: {
	  abrirFormulario(evento) {
		this.eventoEditando = evento;
		this.showForm = true;
	  },
	  fecharFormulario() {
		this.eventoEditando = null;
		this.showForm = false;
	  },
	  eventoSalvo() {
		this.$refs.listaEventos?.carregarEventos?.()
		this.fecharFormulario();
	  }
	}
  }
  </script>
  
  <style>
  html, body, #app {
	margin: 0;
	padding: 0;
	min-height: 100vh;
	background-color: #121212;
	font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
	color: #eee;
  }
  
  #app {
	display: block; 
	width: 100%;
  }

.event-wrapper {
  position: relative;
}

.add-event-btn {
  margin-top: 1rem;
  padding: 0.75rem 1.5rem;
  font-size: 1.2rem;
  border: none;
  border-radius: 6px;
  background-color: #4caf50;
  color: white;
  cursor: pointer;
  font-weight: 600;
  transition: background-color 0.3s ease;
}

.add-event-btn:hover {
  background-color: #388e3c;
}


  </style>