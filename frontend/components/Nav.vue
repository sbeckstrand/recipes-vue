<template>
    <div class="container">
        <b-navbar>
            <template #brand>
                <b-navbar-item href="/">
                    <b-icon
                        pack="fas"
                        icon="leaf"
                        size="is-medium">
                    </b-icon>
                </b-navbar-item>
            </template>
            
            <template #start>
                <b-navbar-item href="/dashboard">
                    Dashboard
                </b-navbar-item>
                <b-navbar-item href="/browse">
                    Find Recipes
                </b-navbar-item>
            </template>

            <template #end>
                <div v-if="authenticated">
                    <b-navbar-item>
                        <div class="buttons">
                            <a href="/profile" class="button is-primary">Profile</a>
                            <a class="button is-light" @click="logout()">Logout</a>
                        </div>
                    </b-navbar-item>
                </div>
                <div v-else>
                    <b-navbar-item tag="div">
                        <div class="buttons">
                            <a class="button is-primary" @click="loginWithGoogle()">Log in</a>
                        </div>
                    </b-navbar-item>
                </div>
            </template>
        </b-navbar>
    </div>
</template>

<script>
export default {
    data() {
      return {
        authenticated: false
      }
    },
    created() {
        this.authenticated = this.$auth.loggedIn
    },
    methods: {
        loginWithGoogle() {
            this.$auth.loginWith("google")
            this.authenticated = true
        },
        logout() {
            this.$auth.logout()
            this.authenticated = false
        }
    }
}
</script>

<style>

</style>