import Vue from 'vue'

// Import fonts and other global styles
//import '@/assets/fonts/fonts.scss'
import '@/styles/globals.scss'

// AT UIKIT
import AtComponents from 'at-ui'
import 'at-ui-style'
Vue.use(AtComponents)

import App from './App.vue'


import router from './router'
import store from './store'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
