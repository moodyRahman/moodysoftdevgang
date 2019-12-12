
var list = ["<li id=0>item 0</li>",
"<li id=1>item 1</li>",
"<li id=2>item 2</li>",
"<li id=3>item 3</li>",
"<li id=4>item 4</li>",
"<li id=5>item 5</li>",
"<li id=6>item 6</li>",
"<li id=7>item 7</li>]"];


var fiblist = []

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


document.getElementById("b").addEventListener("click", function(){addItem();});
document.getElementById("thelist").addEventListener("click", function(){removeItem();} );
document.getElementById("fb").addEventListener("click", function(){addFib()});

function triggerEvent( elem, event ) {
  var clickEvent = new Event( event ); // Create the event.
  elem.dispatchEvent( clickEvent );    // Dispatch the event.
}
