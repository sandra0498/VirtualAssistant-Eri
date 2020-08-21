var unirest = require("unirest");

var req = unirest("GET", "https://microsoft-azure-translation-v1.p.rapidapi.com/translate");

req.query({
	"from": "en",
	"to": "es",
	"text": "Hello%2C world!"
});

req.headers({
	"x-rapidapi-host": "microsoft-azure-translation-v1.p.rapidapi.com",
	"x-rapidapi-key": "SIGN-UP-FOR-KEY",
	"accept": "application/json",
	"useQueryString": true
});


req.end(function (res) {
	if (res.error) throw new Error(res.error);

	console.log(res.body);
});
