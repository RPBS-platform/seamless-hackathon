from seamless.highlevel import load_graph, Cell

ctx.a.share(readonly=False)
ctx.b.share(readonly=False)
ctx.c.share()

ctx.html = Cell("text")
ctx.html.mount("index.html")
ctx.html.mimetype = "html"
ctx.html.share("index.html")

ctx.js = Cell("text")
ctx.js.mount("index.js")
ctx.js.mimetype = "js"
ctx.js.share("index.js")

ctx.client_js = Cell("text")
ctx.client_js.mount("seamless-client.js", mode="r")
ctx.client_js.mimetype = "js"
ctx.client_js.share("seamless-client.js")

await ctx.computation()

ctx.save_graph("basic-webserver.seamless")
ctx.save_zip("basic-webserver.zip")
