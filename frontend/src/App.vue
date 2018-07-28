<template>
  <div id="app">
    <div id="nav">
      <Menu/>
    </div>
    <router-view/>
  </div>
</template>

<script type="text/javascript">
    import Menu from '@/components/Menu.vue'

    export default {
      data() {
        return {

        }
      },
      components: {
        Menu
      }
    }
</script>

<style scoped lang="scss">
#app {
  display: grid;
  grid-template-columns: auto 1fr;
}

</style>
