import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import _global from './components/Common'
import _router from "@/components/router";
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)


Vue.config.productionTip = false
Vue.use(ElementUI)

Vue.prototype._global = _global

new Vue({
  router:_router,
  render: h => h(App),
}).$mount('#app')
