document.getElementById('compatibility-form').addEventListener('submit', function(event) {
    event.preventDefault(); 
    var yourSign = document.getElementById('your-sign').value;
    window.location.href = "/signs/"+ yourSign + ".html";
});