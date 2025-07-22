<template>
	<!-- Lista de eventos -->
	<div v-if="!showForm && !mostrarRelatorio" class="event-list-section">
		<EventList
			ref="listaEventos"
			@editar-evento="abrirFormulario($event)"
		/>
		<!-- Botões de ação -->
		<div class="buttons-row">
			<button class="add-event-btn" @click="abrirFormulario(null)">+ Criar Evento</button>
			<button class="add-event-btn" @click="abrirRelatorio">📊 Ver Relatório</button>
		</div>
	</div>

	<!-- Formulário de evento -->
	<div v-else-if="showForm" class="event-form-section">
		<EventForm
			:eventoSelecionado="eventoEditando"
			@evento-criado="eventoSalvo"
			@cancelar="fecharFormulario"
			@voltar="fecharFormulario"
		/>
	</div>

	<!-- Relatório -->
	<div v-else-if="mostrarRelatorio" class="event-report-section">
		<EventReport />
		<button class="add-event-btn" @click="fecharRelatorio">⬅ Voltar</button>
	</div>
</template>

  <script>
  import EventForm from '../components/EventForm.vue'
  import EventList from '../components/EventList.vue'
  import EventReport from '../components/EventReport.vue' 

  export default {
	name: 'EventsPage',
	components: {
	  EventForm,
	  EventList,
	  EventReport
	},
	data() {
	  return {
		eventoEditando: null,
		showForm: false,
		mostrarRelatorio: false
	  }
	},
	methods: {
	  abrirFormulario(evento) {
		this.eventoEditando = evento;
		this.showForm = true;
		this.mostrarRelatorio = false;
	  },
	  fecharFormulario() {
		this.eventoEditando = null;
		this.showForm = false;
	  },
	  eventoSalvo() {
		this.$refs.listaEventos?.carregarEventos?.()
		this.fecharFormulario();
	  },
	  abrirRelatorio() {
		this.showForm = false;
		this.mostrarRelatorio = true;
	  },
	  fecharRelatorio() {
		this.mostrarRelatorio = false;
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

.buttons-row {
	display: flex;
	gap: 1rem;
	margin-top: 1rem;
}

  </style>