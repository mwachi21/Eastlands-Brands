/** @type {import('tailwindcss').Config} */

module.exports = {
  content: ['./templates/**/*.html'],
  theme: {
      extend: {},
  },
  plugins: [require('daisyui')],
};

// // Theme pack 
// module.exports = {
//   // ...
//   daisyui: {
//       themes: ["light", "dark", "cupcake"], // Add your desired themes here
//   },
// };