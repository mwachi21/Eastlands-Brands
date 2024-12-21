set up with Taliwind CSS with Daisy UI plugin

Installing Daisy UI Plugin alongside Tailwind

```bash
npm install -D tailwindcss postcss autoprefixer daisyui
npx tailwindcss init
```
tailwind.config.js should include :-
```js
module.exports = {
    content: ['./templates/**/*.html'], // Scan Flask templates for classes
    theme: {
        extend: {},
    },
    plugins: [require('daisyui')],
};
```
Run the Tailwind build process
```bash
npx tailwindcss -i ./static/css/style.css -o ./static/css/app.css --watch
```

Gitignore for Daisy UI plugin
```bash
node_modules
yarn.lock
/package-lock.json
.next
/dist
/colors
/index.js
.idea
.DS_Store
*.tgz
/coverage
./build
```