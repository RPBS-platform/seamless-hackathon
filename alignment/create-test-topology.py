from seamless.highlevel import Context, Cell, Transformer

# ctx = Context() ...

ctx.test1 = Context()   # for team bash
ctx.test2 = Context()   # for team Python
await ctx.translation()

# Team bash

# 1. Align input sequences

ctx.test1.seq1 = Cell("text")
ctx.test1.seq1.mount("team-bash/seq1.txt")

ctx.test1.seq2 = Cell("text")
ctx.test1.seq2.mount("team-bash/seq2.txt")

ctx.align = Transformer()
ctx.align.language = "docker"
ctx.align.docker_image = "pegi3s/emboss"
ctx.align.seq1 = ctx.test1.seq1
ctx.align.seq2 = ctx.test1.seq2
ctx.align.code.mount("team-bash/align.bash")

ctx.test1.alignment = ctx.align
ctx.test1.alignment.celltype = "text"
ctx.test1.alignment.mount("team-bash/output/alignment.water", "w")

# 2. Align scrambled sequences

ctx.test1.scrambled1 = Cell("text")
ctx.test1.scrambled1.mount("team-bash/scrambled1.txt")
ctx.test1.scrambled2 = Cell("text")
ctx.test1.scrambled2.mount("team-bash/scrambled2.txt")

ctx.align_scrambled = Transformer()
ctx.align_scrambled.language = "docker"
ctx.align_scrambled.docker_image = "pegi3s/emboss"
ctx.align_scrambled.scrambled1 = ctx.test1.scrambled1
ctx.align_scrambled.scrambled2 = ctx.test1.scrambled2
ctx.align_scrambled.code.mount("team-bash/align_scrambled.bash")

ctx.test1.scrambled_scores = ctx.align_scrambled
ctx.test1.scrambled_scores.celltype = "text"
ctx.test1.scrambled_scores.mount("team-bash/output/scrambled_scores.txt", "w")

# Team Python

# 1. Scramble sequences

ctx.test2.seq1 = Cell("text")
ctx.test2.seq1.mount("team-python/seq1.txt")

ctx.test2.seq2 = Cell("text")
ctx.test2.seq2.mount("team-python/seq2.txt")

ctx.scramble_code = Cell("text")
ctx.scramble_code.mount("team-python/scramble.py")

ctx.scramble1 = Transformer()
ctx.scramble1.seq = ctx.test2.seq1
ctx.scramble1.code = ctx.scramble_code

ctx.test2.scrambled1 = ctx.scramble1
ctx.test2.scrambled1.celltype = "text"
ctx.test2.scrambled1.mount("team-python/output/scrambled1.txt","w")

ctx.scramble2 = Transformer()
ctx.scramble2.seq = ctx.test2.seq2
ctx.scramble2.code = ctx.scramble_code

ctx.test2.scrambled2 = ctx.scramble2
ctx.test2.scrambled2.celltype = "text"
ctx.test2.scrambled2.mount("team-python/output/scrambled2.txt","w")

# 2. Analyze alignment scores

ctx.test2.alignment = Cell("text")
ctx.test2.alignment.mount("team-python/alignment.water")

ctx.test2.scrambled_scores = Cell("text")
ctx.test2.scrambled_scores.mount("team-python/scrambled_scores.txt", "w")

ctx.analyze_alignment_scores = Transformer()
ctx.analyze_alignment_scores.alignment = ctx.test2.alignment
ctx.analyze_alignment_scores.scrambled_scores = ctx.test2.scrambled_scores
ctx.analyze_alignment_scores.code.mount("team-python/analyze_alignment_scores.py")

ctx.test2.significance = ctx.analyze_alignment_scores
ctx.test2.significance.celltype = "plain"
ctx.test2.significance.mount("team-python/output/significance.json", "w")

#  Team web

ctx.seq1 = Cell("text")
ctx.seq1.mount("team-web/seq1.txt")
ctx.seq1.share(readonly=False)

ctx.seq2 = Cell("text")
ctx.seq2.mount("team-web/seq2.txt")
ctx.seq2.share(readonly=False)

ctx.alignment = Cell("text")
ctx.alignment.mount("team-web/alignment.water")
ctx.alignment.share()

ctx.significance = Cell("plain")
ctx.significance.mount("team-web/significance.json")
ctx.significance.share()

ctx.html = Cell("text")
ctx.html.mount("team-web/index.html")
ctx.html.mimetype = "html"
ctx.html.share("index.html")

ctx.js = Cell("text")
ctx.js.mount("team-web/index.js")
ctx.js.mimetype = "js"
ctx.js.share("index.js")

ctx.client_js = Cell("text")
ctx.client_js.mount("seamless-client.js", mode="r")
ctx.client_js.mimetype = "js"
ctx.client_js.share("seamless-client.js")
