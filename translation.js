var unirest = require("unirest");

var req = unirest("POST", "https://microsoft-translator-text.p.rapidapi.com/translate");

req.query({
	"profanityAction": "NoAction",
	"textType": "plain",
	"api-version": "3.0"
});

req.headers({
	"x-rapidapi-host": "microsoft-translator-text.p.rapidapi.com",
	"x-rapidapi-key": "afa3404f83mshf2743be05f8bfeap15b74ejsn3b8517cde47b",
	"content-type": "application/json",
	"accept": "application/json",
	"useQueryString": true
});

req.type("json");
req.send([
	{
		"Text": "I would really like to drive your car around the block a few times."
	}
]);

req.end(function (res) {
	if (res.error) throw new Error(res.error);

	console.log(res.body);
});
