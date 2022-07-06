import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './index.css'
import "vue-connect-wallet/dist/style.css";
import VueConnectWallet from 'vue-connect-wallet'

const app = createApp(App)

app.use(router)
app.use(VueConnectWallet)

app.mount('#app')
