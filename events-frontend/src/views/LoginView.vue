<template>
  <div id="app">
		<form @submit.prevent="fazerLogin" class="login-form">
			<h2 class="title">Login</h2>
			<input
				v-model.trim="email"
				placeholder="E-mail"
				required
				autocomplete="email"
			/>
			<input
				v-model="password"
				type="password"
				placeholder="Senha"
				required
				autocomplete="current-password"
			/>
			<button type="submit" :disabled="loading">
				{{ loading ? 'Entrando...' : 'Entrar' }}
			</button>
			<p v-if="erro" class="error-message">{{ erro }}</p>
		</form>
	</div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
	name: 'LoginView',
	data() {
	  return {
		email: '',
		password: '',
		erro: '',
		loading: false,
	  }
	},
	methods: {
	  async fazerLogin() {
		this.erro = ''
		this.loading = true
		try {
		  const response = await axios.post('http://localhost:8000/api/token/', {
			email: this.email,
			password: this.password,
		  })
		  console.log(response)
		  localStorage.setItem('access_token', response.data.access)
		  localStorage.setItem('refresh_token', response.data.refresh)
		  this.$router.push('/eventos')
		} catch (err) {
		  this.erro = 'Usuário ou senha inválidos'
		} finally {
		  this.loading = false
		}
	  }
	}
  }
  </script>
  
  <style scoped>

  html, body, #app {
	margin: 0;
	height: 100vh; 
	background-color: #121212;
	font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
	color: #eee;
	display: flex;
	justify-content: center; 
	align-items: center;   
  }
  
  .container {
	background: #1e1e1e;
	padding: 2.5rem 3rem;
	border-radius: 12px;
	box-shadow: 0 10px 25px rgba(0,0,0,0.6);
	width: 100%;
	max-width: 360px;
  }
  
  .login-form {
	display: flex;
	flex-direction: column;
	gap: 1.25rem;
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
  
  .error-message {
	color: #f44336; 
	font-weight: 700;
	text-align: center;
	margin-top: -0.5rem;
	font-size: 0.9rem;
	user-select: none;
  }
  
  </style>
  