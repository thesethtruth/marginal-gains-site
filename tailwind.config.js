/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}', './src/**/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: [
      {
        mytheme: {
          "primary": "#B800FF",
          "secondary": "#F87060",
          "accent": "#37cdbe",
          "neutral": "#0e0505",
          "base-100": "#202020",
          "info": "#00a8ff",
          "success": "#009019",
          "warning": "#ff8100",
          "error": "#cf284c",
        },
      },
    ],
  },
  plugins: [
    require('daisyui'),
  ],
};
