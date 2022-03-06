const { CleanWebpackPlugin } = require("clean-webpack-plugin");

module.exports = {
    publicPath: "static/",
    configureWebpack: {
        devServer: {
            devMiddleware: {
                index: true,
                mimeTypes: { phtml: "text/html" },
                publicPath: "./dist",
                serverSideRender: true,
                writeToDisk: true,
            },
        },
        plugins: [new CleanWebpackPlugin()],
    },
};