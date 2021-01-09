var request = new XMLHttpRequest();
const data = "ui=%3CREQUIRED%3E&apiKey=%3CREQUIRED%3E";

request.withCredentials = true;
request.open("POST", "https://yandextranslatezakutynskyv1.p.rapidapi.com/getSupportedLanguages");

request.setRequestHeader("content-type", "application/x-www-form-urlencoded");
request.setRequestHeader("x-rapidapi-key", "afa3404f83mshf2743be05f8bfeap15b74ejsn3b8517cde47b");
request.setRequestHeader("x-rapidapi-host", "YandexTranslatezakutynskyV1.p.rapidapi.com");

request.onload = function() {

    var response = request.response;
    var parsedData = JSON.parse(response);
    console.log(parsedData); 
}


request.send(data);