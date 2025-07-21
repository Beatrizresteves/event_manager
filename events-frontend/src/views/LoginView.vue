<template>
	<form @submit.prevent="fazerLogin">
	  <input v-model="username" placeholder="Usuário" required />
	  <input v-model="password" type="password" placeholder="Senha" required />
	  <button type="submit">Entrar</button>
	  <p v-if="erro" style="color: red">{{ erro }}</p>
	</form>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
	data() {
	  return {
		username: '',
		password: '',
		erro: ''
	  }
	},
	methods: {
	  async fazerLogin() {
		try {
		  const response = await axios.post('http://localhost:8000/api/token/', {
			username: this.username,
			password: this.password
		  })
		  localStorage.setItem('access_token', response.data.access)
		  localStorage.setItem('refresh_token', response.data.refresh)
		  this.erro = ''
		  // redirecionar ou atualizar app após login
		  this.$router.push('/dashboard') 
		} catch (err) {
		  this.erro = 'Usuário ou senha inválidos'
		}
	  }
	}
  }
  </script>
  