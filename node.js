const axios = require("axios");

axios({
    "method":"POST",
    "url":"https://microsoft-translator-text.p.rapidapi.com/translate",
    "headers":{
    "content-type":"application/json",
    "x-rapidapi-host":"microsoft-translator-text.p.rapidapi.com",
    "x-rapidapi-key":"afa3404f83mshf2743be05f8bfeap15b74ejsn3b8517cde47b",
    "accept":"application/json",
    "useQueryString":true
    },"params":{
    "profanityAction":"NoAction",
    "textType":"plain",
    "api-version":"3.0"
    },"data":[{
    "Text":"I would really like to drive your car around the block a few times."
    }]
    })
    .then((response)=>{
      console.log(response)
    })
    .catch((error)=>{
      console.log(error)
    })