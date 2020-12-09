// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyBvyL_gT41XrGlHDlM4QJxOw3MwT89qlOI",
    authDomain: "sensepi-4e031.firebaseapp.com",
    databaseURL: "https://sensepi-4e031.firebaseio.com",
    projectId: "sensepi-4e031",
    storageBucket: "sensepi-4e031.appspot.com",
    messagingSenderId: "1015238253763",
    appId: "1:1015238253763:web:c77b7ccf3cd67bb3725676"
};

firebase.initializeApp(firebaseConfig);

// Get a reference to the file storage service
const storage = firebase.storage();
// Get a reference to the database service
const database = firebase.database();

// Create camera database reference
const camRef = database.ref("file");

// Sync on any updates to the DB. THIS CODE RUNS EVERY TIME AN UPDATE OCCURS ON THE DB.
camRef.limitToLast(1).on("value", function(snapshot) {
  snapshot.forEach(function(childSnapshot) {
    const image = childSnapshot.val()["image"];
    const time = childSnapshot.val()["timestamp"];
    const storageRef = storage.ref(image);

    storageRef
      .getDownloadURL()
      .then(function(url) {
        console.log(url);
        document.getElementById("photo").src = url;
        document.getElementById("time").innerText = time;
      })
      .catch(function(error) {
        console.log(error);
      });
  });
});