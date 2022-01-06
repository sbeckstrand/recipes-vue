<template>
    <div>
        <div class="container">
            <div class="section">
                <h1 v-if="error.statusCode === 404" class="title">404 Page not found</h1>
                <h1 v-else class="title">An Error Occurred</h1>
            </div>
        </div>
            
    </div>
</template>

<script>
export default {
  props: ['error']
}
</script>