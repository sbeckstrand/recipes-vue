<template>
  <div>
    <Profile :user="$auth.user"/>
  </div>
  
</template>

<script>
export default {
  middleware: 'auth',
};
</script>