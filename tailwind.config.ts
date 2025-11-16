import type { Config } from 'tailwindcss'

const config: Config = {
  content: ['./app/**/*.{js,ts,jsx,tsx,mdx}'],
  theme: {
    extend: {
      colors: {
        atelier: {
          50: '#faf9f7', 100: '#f5f3f0', 200: '#ebe7e1', 300: '#e1dbd3', 400: '#d1cac0',
          500: '#c1b9ad', 600: '#a89d8f', 700: '#8b7f6f', 800: '#6e6454', 900: '#5a5240', 950: '#3d3a31',
        },
        luxury: { gold: '#d4af37', silver: '#c0c0c0', bronze: '#cd7f32', platinum: '#e5e4e2' }
      },
      fontFamily: { serif: ['Georgia', 'serif'] }
    },
  },
  plugins: [],
}
export default config