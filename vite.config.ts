import {resolve} from 'path';

module.exports = {
  plugins: [],
  root: resolve('./static/src'),
  base: '/static/',
  server: {
    host: 'localhost',
    port: 5173,
    open: false,
    watch: {
      usePolling: true,
      disableGlobbing: false,
    },
  },
  resolve: {
    extensions: ['.js', '.json', 'ts'],
  },
  build: {
    outDir: resolve('./static/dist'),
    assetsDir: '',
    manifest: 'manifest.json',
    emptyOutDir: true,
    target: 'es2015',
    rollupOptions: {
      input: {
        main: resolve('./static/src/scripts/main.ts'),
        styles: resolve('./static/src/styles/style.scss'),
      },
      output: {
        chunkFileNames: undefined,
      },
    },
  },
};