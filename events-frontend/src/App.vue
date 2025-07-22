<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
html, body, #app {
  margin: 0;
  padding: 0;
  height: 100%;
  background-color: #121212;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #eee;
  display: flex;
  justify-content: center;
  align-items: center;
}

.container {
  background: #1e1e1e;
  padding: 2.5rem 2rem;
  border-radius: 12px;
  box-shadow: 0 10px 25px rgba(0,0,0,0.6);
  width: 100%;
  max-width: 800px;
  
}

.title {
  font-size: 2rem;
  font-weight: 900;
  text-align: center;
  margin-bottom: 2rem;
  color: #fff;
  text-shadow: 0 0 6px rgba(255, 255, 255, 0.3);
}

form {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
  width: 100%;
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
.buttons {
  display: flex;
  gap: 0.75rem;
}

button {
  padding: 0.5rem 1rem; 
  font-size: 1rem;
  border: none;
  border-radius: 8px;
  background: linear-gradient(90deg, #4caf50, #388e3c);
  color: white;
  cursor: pointer;
  font-weight: 600;
  transition: background 0.3s, box-shadow 0.3s;
  min-width: 90px; 
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
  white-space: nowrap;
  margin-left: 1rem;
}

.event-description {
  font-size: 0.9rem;
  color: #555;
  white-space: nowrap;
  margin-left: 1rem;
}

</style>
