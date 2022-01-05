<template>
  <div class="container"> 

    <!-- Profile Information -->
    <section class="section">
        <h1 class="title">{{ editableUser.first_name }} {{ editableUser.last_name }}</h1>

        <p>User ID: {{ editableUser.id }}</p>
        <p>Email: {{ editableUser.email }}</p>
        <p>Favorited {{ favoriteCount }} times</p>

        <!-- Should include a Date Joined -->
    </section>

    <!-- Submitted Recipes -->
    <section class="section">
      <h1 class="title">Recipes</h1>
      <!-- In order of favorited count -->
    </section>

    <!-- Favorites -->
    <section class="section">
      <h1 class="title">Favorites</h1>
    </section>


  </div>
</template>

<script>
export default {
  middleware: 'auth',
  data() {
    return {
      editableUser: {},
      favoriteCount: 0,
    }
  },
  props: {
    user: Object
  },
  watch: {
    user: {
      handler (user) {
        if (user) {
          console.log(user)
          this.editableUser = user
          if (this.user.pk) {
            this.editableUser.id = user.pk
          }
        }
      },
      deep: true,
      immediate: true
    }
  },
};
</script>