var request = new XMLHttpRequest();

request.open("GET", "https://google-translate20.p.rapidapi.com/languages");

request.setRequestHeader("x-rapidapi-key", "afa3404f83mshf2743be05f8bfeap15b74ejsn3b8517cde47b");
request.setRequestHeader("x-rapidapi-host", "google-translate20.p.rapidapi.com");

request.onload = function() {

    var response = request.response;
    var parsedData = JSON.parse(response);
    console.log(parsedData); 
}

request.send();