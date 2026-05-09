import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'
import { VitePWA } from 'vite-plugin-pwa'
import path from 'path'

// https://vite.dev/config/
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '');
  
  return {
    server: {
      allowedHosts: [
        'ffdf-119-160-199-91.ngrok-free.app',
        'brave-tadpole-electric.ngrok-free.app',
      ],
      proxy: {
        '/ollama': {
          target: 'http://127.0.0.1:11434',
          changeOrigin: true,
          secure: false,
          rewrite: path => path.replace(/^\/ollama/, ''),
          configure: (proxy, _options) => {
            proxy.on('error', (err, _req, _res) => {
              console.log('proxy error', err);
            });
            proxy.on('proxyReq', (proxyReq, req, _res) => {
              console.log('Sending Request to the Target:', req.method, req.url);
              proxyReq.removeHeader('origin');
              proxyReq.removeHeader('referer');
            });
            proxy.on('proxyRes', (proxyRes, req, _res) => {
              console.log('Received Response from the Target:', proxyRes.statusCode, req.url);
            });
          },
        },
      },
    },
    define: {
      'import.meta.env.GEMINI_API_KEY': JSON.stringify(env.GEMINI_API_KEY),
    },
    plugins: [
      react(),
      VitePWA({
        registerType: 'autoUpdate',
        includeAssets: ['favicon.ico', 'apple-touch-icon.png', 'mask-icon.svg'],
        manifest: {
          name: 'Parla Italiano',
          short_name: 'ParlaItaliano',
          description: 'Offline Italian conversation practice',
          theme_color: '#1B6B4A',
          icons: [
            {
              src: 'pwa-192x192.png',
              sizes: '192x192',
              type: 'image/png'
            },
            {
              src: 'pwa-512x512.png',
              sizes: '512x512',
              type: 'image/png'
            }
          ]
        },
        workbox: {
          maximumFileSizeToCacheInBytes: 10 * 1024 * 1024, // 10MB
          globPatterns: ['**/*.{js,css,html,ico,png,svg}'],
          runtimeCaching: [
            {
              urlPattern: /^https:\/\/huggingface\.co\/.*\/resolve\/main\/.*$/,
              handler: 'CacheFirst',
              options: {
                cacheName: 'mlc-llm-cache',
                expiration: {
                  maxEntries: 10,
                  maxAgeSeconds: 60 * 60 * 24 * 30, // 30 days
                },
                cacheableResponse: {
                  statuses: [0, 200],
                },
              },
            },
          ],
        },
      })
    ],
    optimizeDeps: {
      include: ['react', 'react-dom', 'zustand'],
    },
    resolve: {
      dedupe: ['react', 'react-dom', 'zustand'],
      alias: {
        'react': path.resolve(__dirname, 'node_modules/react'),
        'react-dom': path.resolve(__dirname, 'node_modules/react-dom'),
        'react/jsx-runtime': path.resolve(__dirname, 'node_modules/react/jsx-runtime'),
        'react/jsx-dev-runtime': path.resolve(__dirname, 'node_modules/react/jsx-dev-runtime'),
        'zustand': path.resolve(__dirname, 'node_modules/zustand'),
        '@app/utils/analytics': path.resolve(__dirname, 'src/lib/analytics.ts'),
        '@app': path.resolve(__dirname, 'src'),
        '@shared/store': path.resolve(__dirname, 'src/store'),
        '@shared/utils': path.resolve(__dirname, 'src/utils'),
        '@shared/data': path.resolve(__dirname, 'src/data'),
        '@shared/ai': path.resolve(__dirname, 'src/ai'),
        '@shared/theme': path.resolve(__dirname, 'src/theme'),
      },
    },
  };
});
