// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth, onAuthStateChanged } from 'firebase/auth';
import { getDocs, getFirestore } from 'firebase/firestore';

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries


const firebaseConfig = {
  apiKey: "AIzaSyDzAiFIeETyKG6yeIjRAnWV24l42Xz3kvM",
  authDomain: "toys-for-friends.firebaseapp.com",
  projectId: "toys-for-friends",
  storageBucket: "toys-for-friends.appspot.com",
  messagingSenderId: "819032599696",
  appId: "1:819032599696:web:b54dd03b1f0448a8ee7c15",
  measurementId: "G-3ZQ9Z64V1G"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(firebaseApp);

auth.onAuthStateChanged(USER => {

});

// onAuthStateChanged(auth, user => {
//     if(user != null ) {
//         console.log('loggeed in!');
//     } else {

//     }
// })

// Get a list of toys from your database
async function getToys(db) {
    const toysCol = collection(db, 'toys');
    const toySnapshot = await getDocs(toysCol);
    const toyList = toySnapshot.docs.map(doc => doc.data());
    return toyList;
}
