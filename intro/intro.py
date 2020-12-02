from seamless.highlevel import Context, Transformer, Cell

ctx = Context()

ctx.a = Cell()
ctx.a.set(2)

ctx.b = Cell()
ctx.b.set(3)

ctx.add = Transformer()
ctx.add.a = ctx.a
ctx.add.b = ctx.b
ctx.add.code = "a + b"

ctx.result = Cell()
ctx.result = ctx.add

ctx.compute()
ctx.save_graph("intro.seamless")
ctx.save_zip("intro.zip")
