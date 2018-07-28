<template lang="html">
  <at-menu active-name="1" id="nav">
  <at-menu-item name="1"><i class="icon icon-home"></i>Home</at-menu-item>

  <at-submenu>
    <template slot="title"><i class="icon icon-book"></i>My Items</template>
    <at-menu-item-group title="Group Two">
      <at-menu-item name="2-1">Submenu One</at-menu-item>
      <at-menu-item name="2-2">Submenu Two</at-menu-item>
    </at-menu-item-group>
    <at-menu-item-group title="Group Three">
      <at-menu-item name="3-1">Submenu Three</at-menu-item>
      <at-menu-item name="3-2" disabled>Submenu Four</at-menu-item>
    </at-menu-item-group>
  </at-submenu>

  <at-menu-item name="4"><i class="icon icon-plus-square"></i>Create an Item</at-menu-item>
  <at-menu-item name="5"><i class="icon icon-info"></i>About</at-menu-item>
  </at-menu>
</template>

<script>
export default {
 data() {
   return {

   }
 },
 methods: {

 }
}
</script>

<style scoped lang="scss">
  @import '@/styles/variables.scss';

</style>
