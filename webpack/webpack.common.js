/* WEBPACK COMMON 
 *
 * This module will export code that is necessary to the configuration of
 * both production and development environments.
 *
 * dev and prod builds will always involve the following
 *  - build and convert nice es6+ javascript to crappy oldschool javascript
 *  - build css files
 *  - output all built files to /website/static/build/
 */

const merge = require('webpack-merge');
const parts = require('./webpack.parts');
const path = require('path');

module.exports = merge([
  {
    entry: {
      index: path.resolve(parts.PATHS.assets, 'js', 'index.js'),
      carousel: path.resolve(parts.PATHS.assets, 'js', 'carousel.js'),
    },
    output: {
      path: parts.PATHS.output,
      publicPath: parts.PATHS.public,
      filename: 'js/[name].bundle.js',
    },
    externals: {
        // require("jquery") is external and available
        //  on the global var jQuery
        "jquery": "jQuery"
    },
  },
  parts.extractCSS({
    test: /\.css/,
    use: ['css-loader'],
    output: 'css/[name].css', 
  }),
  parts.loadJavaScript({
    include: path.resolve(parts.PATHS.assets, 'js'),
    exclude: /node_modules/,
  }),
]);
