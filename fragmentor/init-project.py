PROJNAME = "fragmentor"

from seamless.highlevel import Context, Cell, Transformer

ctx = None
ctx2 = None
save = None

async def load():
    from seamless.metalevel.bind_status_graph import bind_status_graph_async
    import json

    global ctx, ctx2, save
    graph = json.load(open("graph/" + PROJNAME + ".seamless"))
    ctx = Context()
    ctx.add_zip("graph/" + PROJNAME + ".zip")
    ctx.set_graph(graph, mounts=True, shares=True)
    await ctx.translation(force=True)

    status_graph = json.load(open("graph/" + PROJNAME + "-monitoring.seamless"))

    ctx2 = await bind_status_graph_async(
        ctx, status_graph,
        mounts=True,
        shares=True,
        zips=["graph/" + PROJNAME + "-monitoring.zip"],
    )
    def save():
        import os, itertools, shutil

        def backup(filename):
            if not os.path.exists(filename):
                return filename
            for n in itertools.count():
                n2 = n if n else ""
                new_filename = "{}.bak{}".format(filename, n2)
                if not os.path.exists(new_filename):
                    break
            shutil.move(filename, new_filename)
            return filename

        ctx.save_graph(backup("graph/" + PROJNAME + ".seamless"))
        ctx2.save_graph(backup("graph/" + PROJNAME + "-monitoring.seamless"))
        ctx.save_zip(backup("graph/" + PROJNAME + ".zip"))
        ctx2.save_zip(backup("graph/" + PROJNAME + "-monitoring.zip"))

    print("""Project loaded.

    Main context is "ctx"
    Status context is "ctx2"
    Run save() to save the context
    """)