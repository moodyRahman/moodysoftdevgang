
var list = ["<li>item 0</li>",
"<li>item 1</li>",
"<li>item 2</li>",
"<li>item 3</li>",
"<li>item 4</li>",
"<li>item 5</li>",
"<li>item 6</li>",
"<li>item 7</li>]"];


listdom = document.getElementById("thelist");

var addItem = function(e){
  list.push("<li id=word>word</li>");
  out = "";
  for (var x = 0; x < list.length; x++) {
    out = out + list[x]
  }
  out = out.replace("]", "")
  out = out.replace("[", "")
  console.log(out)
  listdom.innerHTML = out;
};

var removeItem = function(e){
  list.pop();
  out = "";
  for (var x = 0; x < list.length; x++) {
    out = out + list[x]
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


var dynamicfibonacci = function(n){
  return recentfib + 2recentfib;
};

currfib = 0;
var fiblist = []
fibdom = document.getElementById("fiblist");

var addFib = function(e){
  fiblist.push("<li>" + fibonacci(currfib) + "</li>");
  currfib = currfib + 1;
  out = "";
  for (var x = 0; x < fiblist.length; x++) {
    out = out + fiblist[x]
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
