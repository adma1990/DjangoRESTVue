<template>
  <div class="hello">
    <div v-for="post in posts" :key="post.id">
      <p>{{ post.name }}</p>
      <p>{{ post.description }}</p>
    </div>
   
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data: () => ({
    posts: []
  }),

  created() {
    axios
    .get("http://127.0.0.1:8000/blogs/")
    .then(response => {this.posts = response.data})
  }

  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
