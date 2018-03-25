var https = require('https');
var request = require('request');
var stringJSON = require('string-to-json');
var moment = require('moment-timezone');
var weather = require('weather-js');

const url1 = 'https://traffic.cit.api.here.com/traffic/6.1/flow.json?prox=12.826700%2C80.041540%2C100&app_id=qkQovEQUeFxQwAen1ysA&app_code=LTyJ6M-OkB1kRKIfxoh9Mw';
const url2 = 'https://traffic.cit.api.here.com/traffic/6.1/flow.json?prox=13.046592%2C80.255311%2C100&app_id=qkQovEQUeFxQwAen1ysA&app_code=LTyJ6M-OkB1kRKIfxoh9Mw';
const url3 = 'https://traffic.cit.api.here.com/traffic/6.1/flow.json?prox=13.046587%2C80.190868%2C100&app_id=qkQovEQUeFxQwAen1ysA&app_code=LTyJ6M-OkB1kRKIfxoh9Mw';

const bodyParser = require('body-parser');
const fs = require('fs');

var day,skycode;

function getTraffic(){

weather.find({search: "Chennai,India", degreeType: 'F'}, function(err, result) {
  if(err) throw err;
  
  skycode = parseInt(result[0].current.skycode);
});

https.get(url1, (resp) => {
  let data = '';
 
  // A chunk of data has been received.
  resp.on('data', (chunk) => {
    data += chunk;
  });
 
  // The whole response has been received. Print out the result.
  resp.on('end', () => {
    var JSONdata = JSON.parse(data);
	var time = moment(JSONdata.CREATED_TIMESTAMP).tz("Asia/Kolkata").format();
	var gettingday = new Date(time);
	var day = gettingday.getDay();
	time = Math.floor((new Date()).getTime() / 1000)
	JSONdata.CREATED_TIMESTAMP = time;
	var obj1 = {};
	obj1["Area"]=1;
	obj1["Date and Time"]=JSONdata.CREATED_TIMESTAMP;
	obj1["Day"]=day;
	obj1["Weather"]=skycode;
	obj1["Jam Factor"]=JSONdata.RWS[0].RW[0].FIS[0].FI[0].CF[0].JF;
	
	fs.appendFile('data.txt', JSON.stringify(obj1), (err) => {  
    if (err) throw err;
	console.log("The data has been updated");
});
    console.log("Road: "+JSONdata.RWS[0].RW[0].DE);
	console.log("Area: "+JSONdata.RWS[0].RW[0].FIS[0].FI[0].TMC.DE);
	console.log("Average Speed: "+JSONdata.RWS[0].RW[0].FIS[0].FI[0].CF[0].SU);
	console.log("Free Flow Speed: "+JSONdata.RWS[0].RW[0].FIS[0].FI[0].CF[0].FF);
	console.log("Jam Factor: "+JSONdata.RWS[0].RW[0].FIS[0].FI[0].CF[0].JF);
	console.log("Date and Time: "+JSONdata.CREATED_TIMESTAMP);
	console.log("Day: "+day);
  });
   
}).on("error", (err) => {
  console.log("Error: " + err.message);
}).end();

https.get(url2, (resp) => {
  let data = '';
 
  // A chunk of data has been received.
  resp.on('data', (chunk) => {
    data += chunk;
  });
 
  // The whole response has been received. Print out the result.
  resp.on('end', () => {
    var JSONdata = JSON.parse(data);
    var time = moment(JSONdata.CREATED_TIMESTAMP).tz("Asia/Kolkata").format();
	var gettingday = new Date(time);
	var day = gettingday.getDay();
	time = Math.floor((new Date()).getTime() / 1000)
	JSONdata.CREATED_TIMESTAMP = time;
	var obj2 = {};
	obj2["Area"]=2;
	obj2["Date and Time"]=JSONdata.CREATED_TIMESTAMP;
	obj2["Day"]=day;
	obj2["Weather"]=skycode;
	obj2["Jam Factor"]=JSONdata.RWS[0].RW[0].FIS[0].FI[0].CF[0].JF;
	
	fs.appendFile('data.txt', JSON.stringify(obj2), (err) => {  
    if (err) throw err;
	console.log("The data has been updated");
});
    console.log("Road: "+JSONdata.RWS[0].RW[0].DE);
	console.log("Intersection: "+JSONdata.RWS[0].RW[0].FIS[0].FI[0].TMC.DE);
	console.log("Average Speed: "+JSONdata.RWS[0].RW[0].FIS[0].FI[0].CF[0].SU);
	console.log("Free Flow Speed: "+JSONdata.RWS[0].RW[0].FIS[0].FI[0].CF[0].FF);
	console.log("Jam Factor: "+JSONdata.RWS[0].RW[0].FIS[0].FI[0].CF[0].JF);
	console.log("Date and Time: "+JSONdata.CREATED_TIMESTAMP);
	console.log("Day: "+day);
  });
   
}).on("error", (err) => {
  console.log("Error: " + err.message);
}).end();

https.get(url3, (resp) => {
  let data = '';
 
  // A chunk of data has been received.
  resp.on('data', (chunk) => {
    data += chunk;
  });
 
  // The whole response has been received. Print out the result.
  resp.on('end', () => {
    var JSONdata = JSON.parse(data);
	var time = moment(JSONdata.CREATED_TIMESTAMP).tz("Asia/Kolkata").format();
	var gettingday = new Date(time);
	var day = gettingday.getDay();
	time = Math.floor((new Date()).getTime() / 1000)
	JSONdata.CREATED_TIMESTAMP = time;
	var obj3 = {};
	obj3["Area"]=3;
	obj3["Date and Time"]=JSONdata.CREATED_TIMESTAMP;
	obj3["Day"]=day;
	obj3["Weather"]=skycode;
	obj3["Jam Factor"]=JSONdata.RWS[0].RW[0].FIS[0].FI[0].CF[0].JF;
	
	fs.appendFile('data.txt', JSON.stringify(obj3), (err) => {  
    if (err) throw err;
	console.log("The data has been updated");
});
    console.log("Road: "+JSONdata.RWS[0].RW[0].DE);
	console.log("Intersection: "+JSONdata.RWS[0].RW[0].FIS[0].FI[0].TMC.DE);
	console.log("Average Speed: "+JSONdata.RWS[0].RW[0].FIS[0].FI[0].CF[0].SU);
	console.log("Free Flow Speed: "+JSONdata.RWS[0].RW[0].FIS[0].FI[0].CF[0].FF);
	console.log("Jam Factor: "+JSONdata.RWS[0].RW[0].FIS[0].FI[0].CF[0].JF);
	console.log("Date and Time: "+JSONdata.CREATED_TIMESTAMP);
	console.log("Day: "+day);
  });
   
}).on("error", (err) => {
  console.log("Error: " + err.message);
}).end();
}

setInterval(getTraffic,600000);