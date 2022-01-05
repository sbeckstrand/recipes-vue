<template>
  <div>
    <Nav />
    <Profile :user="$auth.user"/>
  </div>
  
</template>

<script>
export default {
  middleware: 'auth',
};
</script>