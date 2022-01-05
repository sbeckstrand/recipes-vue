<template>
  <div>
    <Nav />
    <Profile :profile="$auth.user"/>
  </div>
  
</template>

<script>
export default {
  middleware: 'auth',
};
</script>