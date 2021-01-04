'use strict';
var wia = require('wia')('d_sk_256g88JjwMoHJwHKreawliex');
var util = require('util')
var nodeimu  = require('nodeimu');
var IMU = new nodeimu.IMU();
var tic = new Date();
var callback = function (error, data) {
 var toc = new Date();
 if (error) {
   console.log(error);
   return;
 }
 // Send temperature data
 wia.events.publish({
   name: "temperature",
   data: data.temperature.toFixed(5) // data received from temperature sensor
 });
 setTimeout(function() { tic = new Date(); IMU.getValue(callback); } , 250 - (toc - tic));
}
// Using the MQTT stream
wia.stream.on('connect', function() {
 IMU.getValue(callback);
});
wia.stream.connect();
