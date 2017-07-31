$(document).ready(function(){
var header = $('#background');

var backgrounds = new Array(
    'url("img/background.jpg")'
  , 'url("img/background2.jpg")'
  , 'url("img/background3.jpg")'
  , 'url("img/background4.jpg")'  
);

var current = 0;

function nextBackground() {
    current++;
    current = current % backgrounds.length;
    header.css('background-image', backgrounds[current]);
}
setInterval(nextBackground, 5000);

header.css('background-image', backgrounds[0]);
});