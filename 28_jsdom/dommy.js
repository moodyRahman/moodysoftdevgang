
var list = ["<li>item 0</li>",
"<li>item 1</li>",
"<li>item 2</li>",
"<li>item 3</li>",
"<li>item 4</li>",
"<li>item 5</li>",
"<li>item 6</li>",
"<li>item 7</li>]"];




var fiblist = []

var addItem = function(e){
  listdom = document.getElementById("thelist");
  list.push("<li id=word>word</li>");
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

var fibonacci = function (n) {
    if (n == 0) {
        return 0;
    }
    if (n == 1) {
        return 1;
    }
    return (fibonacci(n - 1) + fibonacci(n - 2));
};



currfib = 0;


var addFib = function(e){
  fibdom = document.getElementById("fiblist");
  fiblist.push("<li>" + fibonacci(currfib) + "</li>");
  currfib = currfib + 1;
  out = fiblist.toString();
  while (out.indexOf(',') != -1) {
    out = out.replace(/,/, "");
  }
  out = out.replace("]", "")
  out = out.replace("[", "")
  console.log(out)
  fibdom.innerHTML = out;
};


header = document.getElementById("h")
document.getElementById("b").addEventListener("click", function(){addItem();});
document.getElementById("thelist").addEventListener("click", function(){removeItem();} );
document.getElementById("fb").addEventListener("click", function(){addFib()});
// document.getElementById("thelist").addEventListener("mouseover", function(e){console.log(e.target.attributes[0]);});
// document.getElementById("thelist").addEventListener("mouseleave", function(e){});
document.getElementById("thelist").addEventListener("mouseover", function(e){console.log(e.target.innerHTML);header.innerHTML=e.target.innerHTML});
document.getElementById("thelist").addEventListener("mouseleave", function(e){header.innerHTML="Hello World!"});

function triggerEvent( elem, event ) {
  var clickEvent = new Event( event ); // Create the event.
  elem.dispatchEvent( clickEvent );    // Dispatch the event.
}
