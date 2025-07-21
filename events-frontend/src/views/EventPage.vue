<template>
	<div class="event-page">
	  <h1 class="page-title">Gerenciador de Eventos</h1>
  
	  <div class="event-wrapper">
		<EventForm
		  :eventoSelecionado="eventoEditando"
		  @evento-criado="atualizarLista"
		/>
		<EventList
		  ref="listaEventos"
		  @editar-evento="eventoEditando = $event"
		/>
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
			eventoEditando: null
		}
	},
	methods: {
    	atualizarLista() {
			this.$refs.listaEventos?.carregarEventos?.()
			this.eventoEditando = null
		}
	}
  }
  </script>
  
  <style>
  html, body, #app {
	margin: 0;
	padding: 0;
	min-height: 100vh; /* <- não use height fixa! */
	background-color: #121212;
	font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
	color: #eee;
  }
  
  #app {
	display: block; /* Remova qualquer flex desnecessário */
	width: 100%;
  }
  </style>