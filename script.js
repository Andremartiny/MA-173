function moveDivs(from, to, wheretoplacefromdiv = "-200vw", wheretoplacetodiv = "0vw") {
  const fromdiv = document.getElementById(from);
  const todiv = document.getElementById(to);
  fromdiv.style.transform = `translateX(${wheretoplacefromdiv})`;
  fromdiv.style.overflow = "hidden";
  todiv.style.transform = `translateX(${wheretoplacetodiv})`;
  todiv.style.overflow = "visible";
}
function moveDivsback(from, to, x = "0vw", y = "200vw") {
  moveDivs(to, from, y, x)
}
