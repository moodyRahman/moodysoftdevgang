
var list = ["<li>item 0</li>",
"<li>item 1</li>",
"<li>item 2</li>",
"<li>item 3</li>",
"<li>item 4</li>",
"<li>item 5</li>",
"<li>item 6</li>",
"<li>item 7</li>]"];

var addItem = function(e){
  listdom = document.getElementById("thelist");
  list.push("<li>word</li>");
  out = list.toString();
  while (out.indexOf(',') != -1) {
    out = out.replace(/,/, "");
  }
  out = out.replace("]", "")
  out = out.replace("[", "")
  console.log(out)
  listdom.innerHTML = out;
};

var removeItem = function(e){
  listdom = document.getElementById("thelist");
  list.pop();
  out = list.toString();
  while (out.indexOf(',') != -1) {
    out = out.replace(/,/, "");
  }
  out = out.replace("]", "")
  out = out.replace("[", "")
  console.log(out)
  listdom.innerHTML = out;
};



document.getElementById("b").addEventListener("click", function(){addItem();});
document.getElementById("thelist").addEventListener("click", function(){removeItem();} );

function triggerEvent( elem, event ) {
  var clickEvent = new Event( event ); // Create the event.
  elem.dispatchEvent( clickEvent );    // Dispatch the event.
}
