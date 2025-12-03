import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath, URL } from 'node:url'
import path from 'path'

export default defineConfig({
  plugins: [vue()],
  envDir: path.resolve(__dirname, './'), // Explicitly only read .env from portal directory
  envPrefix: 'VITE_', // Only load vars with VITE_ prefix
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    port: 3000,
    proxy: {
      // Proxy API requests to barbara-agent FastAPI server
      '/api': {
        target: 'https://barbara-agent.fly.dev',
        changeOrigin: true,
        secure: true
      }
    }
  }
})

