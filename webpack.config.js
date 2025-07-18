const path = require("path");
const autoprefixer = require("autoprefixer");
const miniCssExtractPlugin = require("mini-css-extract-plugin");
const { SourceMap } = require("module");

module.exports = {
  entry: {
    main: "./assets/js/index.js",
    custom: "./assets/js/custom.js",
  },
  output: {
    filename: "js/[name].js",
    path: path.resolve(__dirname, "static/compiled_assets/"),
  },
  plugins: [new miniCssExtractPlugin({ filename: "css/[name].css" })],
  devtool: "source-map",
  module: {
    rules: [
      {
        test: /\.(woff|woff2|ttf|eot)$/,
        generator: {
          filename: "fonts/[hash][ext]",
        },
      },
      {
        test: /\.js$/,
        enforce: "pre",
        use: ["source-map-loader"],
      },
      //handle inlide data:// for svgs in bootstrap scss files
      {
        mimetype: "image/svg+xml",
        scheme: "data",
        type: "asset/resource",
        generator: {
          filename: "icons/[hash].svg",
        },
      },
      {
        test: /\.(scss)$/,
        use: [
          {
            // creates .css  files
            loader: miniCssExtractPlugin.loader,
          },
          {
            // Interprets `@import` and `url()` like `import/require()` and will resolve them
            loader: "css-loader",
          },
          {
            // Loader for webpack to process CSS with PostCSS
            loader: "postcss-loader",
            options: {
              postcssOptions: {
                plugins: [autoprefixer],
              },
            },
          },
          {
            // Loads a SASS/SCSS file and compiles it to CSS
            loader: "sass-loader",
            options: {
              sassOptions: {
                // Optional: Silence Sass deprecation warnings. See note below.
                silenceDeprecations: [
                  "mixed-decls",
                  "color-functions",
                  "global-builtin",
                  "import",
                ],
              },
            },
          },
        ],
      },
    ],
  },
};
