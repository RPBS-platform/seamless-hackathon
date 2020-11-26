ctx = connect_seamless()

ctx.self.onsharelist = function(sharelist) {

  var inputElement = document.getElementById("a");
  inputElement.addEventListener("change", change_a, false);
  function change_a() {
    ctx["a"].set(this.value)
  }
  ctx["a"].onchange = function() {
    value = this.value
    document.getElementById("a").value = value
  }

  var inputElement = document.getElementById("b");
  inputElement.addEventListener("change", change_b, false);
  function change_b() {
    ctx["b"].set(this.value)
  }
  ctx["b"].onchange = function() {
    value = this.value
    document.getElementById("b").value = value
  }

  ctx["c"].onchange = function() {
    value = this.value
    document.getElementById("c").value = value
  }

}
