<!-- src/pages/EventsPage.vue -->
<template>
	<div class="event-page">
	  <h1>Gerenciador de Eventos</h1>
	  <EventForm @evento-criado="atualizarLista" />
	  <EventList ref="listaEventos" />
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
	methods: {
	  atualizarLista() {
		this.$refs.listaEventos?.mounted?.()
	  }
	}
  }
  </script>
  
  <style scoped>
  .event-page {
	max-width: 800px;
	margin: 0 auto;
	padding: 2rem;
  }
  </style>
  