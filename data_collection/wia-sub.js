// Create an instance of Wia
// Replace 'd_sk_abcdef' with your device secret key
var wia = require('wia')('dev_lqhDeyAi');

// Subscribe to all events for a device
// Replace 'dev_abc123' with your device ID
wia.events.subscribe({
  device: 'dev_lqhDeyAi'
}, function(event) {
  console.log(event);
});

// Connect to the MQTT API
wia.stream.connect();
