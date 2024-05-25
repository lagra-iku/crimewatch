/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['app/templates/**/*.html'],
  theme: {
    extend: {},
    colors: {
      'deepNavy': '#153A4C',
      'lightNavy': '#153A4C',
      'mutedTeal': '#417d92',
      'lightTeal': '#4e9ba1',
      'lightBlue': '#B1C6CA',
      'lightBlueGrey': '#D9E3E5', 
      'white': '#ffffff', 
    },
    fontFamily: {
      'sans': ['Montserrat'],
      'serif': ['ui-serif', 'Georgia'],
      'mono': ['ui-monospace', 'SFMono-Regular'],
      'display': ['Oswald'],
      'body': ['"Montserrat"'],
    },
    gradientColorStops: theme => ({
      'deepNavy': '#153A4C',
      'black': '#000000',
  }),
  },
  plugins: [],
}
