<template>
  <div class="home">
    <p>This is a home page</p>
    <button @click="request" type="button" name="button">Click me</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'home',
  components: {
  },
  methods: {
    request: function() {
      axios.get('http://localhost:5000/ping')
      .then(function(response) {
        console.log(response);
      })
      .catch(function(error) {
        console.log(error);
      })
    }
  }
}
</script>
