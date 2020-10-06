import pyrebase

config = {
  "apiKey": "AIzaSyCqgIMdBH-r6WBIRc1aWcCcxFNzD2bqYoA",
  "authDomain": "todoapp-763d0.firebaseapp.com",
  "databaseURL": "https://todoapp-763d0.firebaseio.com",
  "projectId": "todoapp-763d0",
  "storageBucket": "todoapp-763d0.appspot.com",
  "messagingSenderId": "937562843838",
  "appId": "1:937562843838:web:8c450948aab53ab6024cef",
  "measurementId": "G-WG32Z0K8TC"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()