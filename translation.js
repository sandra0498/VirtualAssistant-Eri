var unirest = require("unirest");

var req = unirest("GET", "https://microsoft-azure-translation-v1.p.rapidapi.com/translate");

req.query({
	"from": "en",
	"to": "es",
	"text": "Hello%2C world!"
});

req.headers({
	"x-rapidapi-host": "microsoft-azure-translation-v1.p.rapidapi.com",
	"x-rapidapi-key": "afa3404f83mshf2743be05f8bfeap15b74ejsn3b8517cde47b",
	"accept": "application/json",
	"useQueryString": true
});


req.end(function (res) {
	if (res.error) throw new Error(res.error);

	console.log(res.body);
});
