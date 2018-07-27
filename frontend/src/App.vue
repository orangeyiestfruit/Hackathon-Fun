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

<style lang="scss">

</style>
