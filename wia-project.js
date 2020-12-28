// Create an instance of Wia
// Replace 'd_sk_abcdef' with your device secret key
var wia = require('wia')('d_sk_256g88JjwMoHJwHKreawliex');

// Listen for a successful connection to the MQTT API
wia.stream.on('connect', function() {
  // Publish an event
  wia.events.publish({
    name: 'temperature',
    data: 21.5
  });
});

// Connect to the MQTT API
wia.stream.connect();
