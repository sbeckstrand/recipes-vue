<template>
  <div>
    <Profile :user="user"/>
  </div>
  
</template>

<script>
export default {
    middleware: 'auth',
    async asyncData({ params, $axios }) {
        let user = {}
        try {
            user = await $axios.$get(`ttp://localhost:8000/api/users/${params.id}`)
        } catch (error) {
            console.log(error)
        }
        
        return { user }
    }
};
</script>