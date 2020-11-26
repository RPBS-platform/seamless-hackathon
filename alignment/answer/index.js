ctx = connect_seamless()

ctx.self.onsharelist = function(sharelist) {

  var inputElement = document.getElementById("seq1");
  inputElement.addEventListener("change", change_seq1, false);
  function change_seq1() {
    ctx["seq1"].set(this.value)
  }
  ctx["seq1"].onchange = function() {
    value = this.value
    document.getElementById("seq1").value = value
  }

  var inputElement = document.getElementById("seq2");
  inputElement.addEventListener("change", change_seq2, false);
  function change_seq2() {
    ctx["seq2"].set(this.value)
  }
  ctx["seq2"].onchange = function() {
    value = this.value
    document.getElementById("seq2").value = value
  }

  ctx["alignment"].onchange = function() {
    value = this.value
    document.getElementById("alignment").value = value
  }

  ctx["significance"].onchange = function() {
    value = JSON.parse(this.value)
    document.getElementById("z").value = value.z.toPrecision(4)
    document.getElementById("p").value = value.p.toPrecision(4)
  }

}
