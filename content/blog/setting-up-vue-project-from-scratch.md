---
draft: True
template: base.html
title: "Tutorial: Setting up Vue Projects with Webpack 4 from Scratch"
---

[vue-cli](https://cli.vuejs.org) is a super handy tool for bootstrapping a Vue project. It shields us from many manual, tidy webpack configurations, and lets us worry about our application code only. But in some cases, we may want to get our hand dirty:

- we want to fine tune the configurations.
- we want to learn the blackbox.

This post is a step-by-step guide on setting up a Vue project with Webpack 4. Webpack is a tool that transforms a set of input files into a set of output files. Input files can be sass code, vue files, es6 javascripts, etc., and outputs are often standard, widely supported html, js, and css. To do that, you define a chain of transformer functions in a webpack config file, and simply run `webpack` with that config file.

In Webpack terminology:
- Input files are defined as an `entry` file. By examining the dependencies included in the entry file, Webpack will know all the inputs.
- Tranformer functions are called loaders. Loaders are usually written by a third party provider. In this example, we'll use `vue-loader` to transform `.vue` files.

Consult the [webpack guide](https://webpack.js.org/concepts/) as a reference when reading this tutorial.

Let's start with a simple Vue project includes a index.html and a app.vue file
